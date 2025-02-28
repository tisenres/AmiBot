import datetime
import re
from dataclasses import dataclass
import ssl
import certifi
import http.client

import requests
import http.client
import urllib3

HOST = 's.amizone.net'
DATE_FORMAT_STRING = "%Y-%m-%d"


# @dataclass
# class Tokens:
#     auth_token: str = None
#
#
# __tokens = [
#     Tokens.auth_token,
#     Tokens.auth_token,
#     Tokens.auth_token,
#     Tokens.auth_token,
# ]


def get_auth(host: str, username: str, password: str):
    url = f'https://{host}/'
    
    if username == "" or password == "":
        raise Exception("Fill password and username")
    
    # First stage
    result = requests.get(url)

    request_verification_token_value = get_param_from_body(result = result, param = "__RequestVerificationToken")
    salt_value = get_param_from_body(result = result, param = "Salt")
    secret_value = get_param_from_body(result = result, param = "SecretNumber")
    signature_value = get_param_from_body(result = result, param = "Signature")
    challenge_value = get_param_from_body(result = result, param = "Challenge")

    # Second stage
    fields = {
        "__RequestVerificationToken": request_verification_token_value,
        "Salt": salt_value,
        "SecretNumber": secret_value,
        "Signature": signature_value,
        "Challenge": challenge_value,
        "_UserName": username,
        "_Password": password,
    }

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    ssl_context.load_verify_locations("amizone.crt")  # Load the Amizone certificate

    multipart_body, multipart_header = urllib3.encode_multipart_formdata(fields)
    conn = http.client.HTTPSConnection(host, context=ssl_context)
    
    headers = {
        'Content-Type': multipart_header,
        'Cookie': f'__RequestVerificationToken={result.cookies.get("__RequestVerificationToken")}; Path=/; HttpOnly;',
    }
    conn.request("POST", "/", multipart_body, headers)
    res = conn.getresponse()
    auth_header_bundle = res.getheader("Set-Cookie")
    
    regex = ".ASPXAUTH=; expires=.+?(.ASPXAUTH=.+?path=/)"
    arr = re.findall(regex, auth_header_bundle)
    try:
        auth_token = arr[0]
    except IndexError:
        raise ConnectionError
    
    return auth_token


def get_param_from_body(result, param):
    regex = f".+<input.+name=\"{param}\" type=\"hidden\" value=\"(.+?)\".+"
    arr = re.findall(regex, result.text)
    param_value = arr[0]

    return param_value


def get_schedule(auth_token: str, host: str, start_day: datetime, end_day: datetime):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    ssl_context.load_verify_locations("amizone.crt")  # Load the Amizone certificate

    json_conn = http.client.HTTPSConnection(host, context=ssl_context)

    json_headers = {
        "Cookie": str(auth_token),
        "referer": f"https://{host}/"
    }

    try:
        json_conn.request("GET", f"/Calendar/home/GetDiaryEvents?start={start_day.strftime(DATE_FORMAT_STRING)}"
                                 f"&end={end_day.strftime(DATE_FORMAT_STRING)}&_=1667584748354",
                          None,
                          json_headers)
    except TypeError as e:
        print(f"TypeError occurred: {e}")  # For debugging
        raise ConnectionError
    except ssl.SSLCertVerificationError as e:
        print(f"SSL Verification Error: {e}")  # For debugging
        raise ConnectionError
    
    json_res = json_conn.getresponse()
    json_data = json_res.read()
    
    return json_data.decode("utf-8")

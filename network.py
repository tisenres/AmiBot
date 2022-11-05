import datetime
import re
from dataclasses import dataclass

import requests
import http.client
import urllib3

HOST = 's.amizone.net'
DATE_FORMAT_STRING = "%Y-%m-%d"


@dataclass
class Tokens:
    auth_token: str = None


def get_auth(host: str, username: str, password: str):
    
    url = f'https://{host}/'
    
    if username == "" or password == "":
        raise Exception("Fill password and username")
    
    # First stage
    get_result = requests.get(url)
    
    regex = ".+name=\"loginform\"><input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"(.+?)\".+"
    arr = re.findall(regex, get_result.text)
    form_token = arr[0]
    cookie_token = get_result.cookies.get("__RequestVerificationToken")
    
    # Second stage
    fields = {
        "__RequestVerificationToken": form_token,
        "_UserName": username,
        "_Password": password,
    }
    
    multipart_body, multipart_header = urllib3.encode_multipart_formdata(fields)
    conn = http.client.HTTPSConnection(host)
    
    headers = {
        'Content-Type': multipart_header,
        'Cookie': f'__RequestVerificationToken={cookie_token}; Path=/; HttpOnly;',
    }
    conn.request("POST", "/", multipart_body, headers)
    res = conn.getresponse()
    auth_header_bundle = res.getheader("Set-Cookie")
    
    regex = ".ASPXAUTH=; expires=.+?(.ASPXAUTH=.+?path=/)"
    arr = re.findall(regex, auth_header_bundle)
    auth_token = arr[0]
    
    return auth_token


def get_schedule(auth_token: str, host: str, start_day: datetime, end_day: datetime):
    url = f'https://{host}/'
    
    json_headers = {
        "Cookie": auth_token,
        "referer": url
    }

    json_conn = http.client.HTTPSConnection(host)
    json_conn.request("GET", f"/Calendar/home/GetDiaryEvents?start={start_day.strftime(DATE_FORMAT_STRING)}"
                             f"&end={end_day.strftime(DATE_FORMAT_STRING)}&_=1667584748354",
                      None,
                      json_headers)
    json_res = json_conn.getresponse()
    json_data = json_res.read()
    
    return json_data.decode("utf-8")

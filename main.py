from create_bot import dp
from aiogram.utils import executor
import re
import requests
import http.client

from handlers import start_help, choose_sections, others, show_schedule, show_tmr, show_week

start_help.register_start_help_handler(dp)
choose_sections.register_handlers_choose_sections(dp)
show_schedule.register_handlers_show_schedule(dp)
show_tmr.register_handlers_show_tmr(dp)
show_week.register_handlers_show_week(dp)
others.register_handlers_others(dp)


def request_test():
    report_day = "2022-11-03"
    host = 's.amizone.net'
    url = f'https://{host}/'
    boundary = "12345"
    username = ""
    password = ""
    
    if username == "" or password == "":
        raise Exception("Fill password and username")
    
    # First stage
    get_result = requests.get(url)

    regex = ".+name=\"loginform\"><input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"(.+?)\".+"
    arr = re.findall(regex, get_result.text)
    form_token = arr[0]
    cookie_token = get_result.cookies.get("__RequestVerificationToken")
    
    # Second stage
    conn = http.client.HTTPSConnection(host)
    payload = f"--{boundary}\n" \
              f"Content-Disposition: form-data; name=\"__RequestVerificationToken\"\n" \
              f"Content-Type: text/plain\n\n" \
              f"{form_token}\n" \
              f"--{boundary}\n" \
              f"Content-Disposition: form-data; name=\"_UserName\"\n" \
              f"Content-Type: text/plain\n\n" \
              f"{username}\n" \
              f"--{boundary}\n" \
              f"Content-Disposition: form-data; name=\"_Password\"\n" \
              f"Content-Type: text/plain\n\n" \
              f"{password}\n" \
              f"--{boundary}--\n"
    headers = {
        'Content-Type': f'multipart/form-data; boundary={boundary}',
        'Cookie': f'__RequestVerificationToken={cookie_token}; Path=/; HttpOnly;',
    }
    conn.request("POST", "/", payload, headers)
    res = conn.getresponse()
    auth_header_bundle = res.getheader("Set-Cookie")

    regex = ".ASPXAUTH=; expires=.+?(.ASPXAUTH=.+?path=/)"
    arr = re.findall(regex, auth_header_bundle)
    auth_token = arr[0]
    
    # Third stage
    json_headers = {
        "Cookie": auth_token,
        "referer": url
    }
    
    json_conn = http.client.HTTPSConnection(host)
    json_conn.request("GET", f"/Calendar/home/GetDiaryEvents?start={report_day}&end={report_day}&_=1667584748354",
                      None,
                      json_headers)
    json_res = json_conn.getresponse()
    json_data = json_res.read()
    
    print(f'The form token is \"{form_token}\"')
    print(f'The cookie token is \"{cookie_token}\"')
    print(f'The main auth token is \"{auth_token}\"')

    print(json_data.decode("utf-8"))
    

if __name__ == '__main__':
    # executor.start_polling(dp, skip_updates=True)
    request_test()
    
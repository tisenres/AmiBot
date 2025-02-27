import datetime
import json
import os
from dataclasses import dataclass
from email.policy import default
from enum import Enum

# from requests import JSONDecodeError
# from decoder import JSONDecodeError
from json import JSONDecodeError

import network


@dataclass
class Credential:
    username: str
    password: str

username = os.environ.get("section1_username", "default_username")
password = os.environ.get("section1_password", "default_password")

__credentials = [
    Credential(username=username, password=password),
    None,
    None,
    None
]


class PeriodType(Enum):
    TODAY = "Today"
    TOMORROW = "Tomorrow"
    WEEK = "Current week"
    
    def get_period(self) -> (datetime, datetime):
        match self:
            case PeriodType.TODAY:
                day = datetime.datetime.today()
                return day, day
            case PeriodType.TOMORROW:
                tomorrow = datetime.datetime.today() + datetime.timedelta(1)
                return tomorrow, tomorrow
            case PeriodType.WEEK:
                delta = datetime.datetime.today().weekday()
                today = datetime.datetime.today()
                start = today + datetime.timedelta(0 - delta)
                end = today + datetime.timedelta(6 - delta)
                return start, end
        
    @staticmethod
    def get_by_value(string_value: str):
        match string_value:
            case PeriodType.TODAY.value:
                return PeriodType.TODAY
            case PeriodType.TOMORROW.value:
                return PeriodType.TOMORROW
            case PeriodType.WEEK.value:
                return PeriodType.WEEK
            case _:
                return None
            

def get_schedule(section_num: int, period_type: PeriodType):
    json_data: str
    start_day, end_day = period_type.get_period()
    
    if section_num > len(__credentials):
        raise NotImplementedError
    
    cred = __credentials[section_num-1]
    if cred is None:
        raise NotImplementedError
    
    try:
        json_data = network.get_schedule(network.__tokens[section_num-1], network.HOST, start_day, end_day)
        json.loads(json_data)
    # except ConnectionError or JSONDecodeError:
    except JSONDecodeError:
        auth = network.get_auth(network.HOST, cred.username, cred.password)
        network.__tokens[section_num-1] = auth
        json_data = network.get_schedule(network.__tokens[section_num-1], network.HOST, start_day, end_day)
    except IndexError:
        raise ConnectionError
    except Exception as err:
        print("Error " + err)
    
    return json_data

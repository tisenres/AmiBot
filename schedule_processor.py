import datetime
import os
from dataclasses import dataclass
from enum import Enum

import network


@dataclass
class Credential:
    username: str
    password: str


__credentials = [
    Credential(username=os.environ["section1_username"], password=os.environ["section1_password"]),
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


def get_schedule(section_num: int, period_type: PeriodType):
    json_data: str
    start_day, end_day = period_type.get_period()
    
    if section_num >= len(__credentials):
        return "[]"
    
    cred = __credentials[section_num-1]
    if cred is None:
        return "[]"
    
    if network.Tokens.auth_token is not None:
        json_data = network.get_schedule(network.Tokens.auth_token, network.HOST, start_day, end_day)
    else:
        auth = network.get_auth(network.HOST, cred.username, cred.password)
        network.Tokens.auth_token = auth
        json_data = network.get_schedule(network.Tokens.auth_token, network.HOST, start_day, end_day)
    return json_data

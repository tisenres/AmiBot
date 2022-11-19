from datetime import datetime

from vo.DateConstants import Constants


class Lesson:
    __title: str
    __date: datetime
    __start_time: datetime
    __end_time: datetime
    
    def __init__(self, title: str, date: str, start_time: str, end_time: str):
        self.__title = title
        self.__date = datetime.strptime(date, Constants.FORMATTER)
        self.__start_time = datetime.strptime(start_time, Constants.FORMATTER)
        self.__end_time = datetime.strptime(end_time, Constants.FORMATTER)
    
    def __str__(self) -> str:
        return self.__title
    
    def get_key(self) -> str:
        return datetime.strftime(self.__date, Constants.FULL_DATE_FORMATTER)
    
    def get_short_start_time(self) -> str:
        return datetime.strftime(self.__start_time, Constants.SHORT_TIME_FORMATTER)
    
    def get_short_end_time(self) -> str:
        return datetime.strftime(self.__end_time, Constants.SHORT_TIME_FORMATTER)
    
    def get_title(self) -> str:
        return self.__title

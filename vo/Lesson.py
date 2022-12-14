from datetime import datetime

from vo.DateConstants import Constants


class Lesson:
    __title: str
    __date: datetime
    __start_time: datetime
    __end_time: datetime
    __faculty_name: str
    __room_no: str
    
    def __init__(self, title: str, date: str, start_time: str, end_time: str, faculty_name: str, room_no: str):
        self.__title = title
        self.__date = datetime.strptime(date, Constants.PARSE_FORMAT)
        self.__start_time = datetime.strptime(start_time, Constants.PARSE_FORMAT)
        self.__end_time = datetime.strptime(end_time, Constants.PARSE_FORMAT)
        self.__faculty_name = faculty_name
        self.__room_no = room_no
    
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
    
    def get_faculty_name(self) -> str:
        return self.__faculty_name
    
    def get_room_no(self) -> str:
        return self.__room_no
    

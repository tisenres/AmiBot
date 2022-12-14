from datetime import datetime
from typing import List

from vo.DateConstants import Constants
from vo.Lesson import Lesson


class Day:
    __date: datetime
    __weekday: str
    __lessons: List[Lesson]
    
    def __init__(self, date: str, lessons: [Lesson]):
        self.__date = datetime.strptime(date, Constants.PARSE_FORMAT)
        self.__weekday = datetime.strptime(date, Constants.PARSE_FORMAT).strftime("%A")
        self.__lessons = lessons
    
    def get_weekday(self) -> str:
        return self.__weekday
    
    def get_date(self) -> str:
        return self.__date.strftime(Constants.FULL_DATE_FORMATTER)
    
    def get_short_date(self) -> str:
        return self.__date.strftime(Constants.SHORT_DATE_FORMATTER)
    
    def append_lesson(self, lesson: Lesson) -> None:
        self.__lessons.append(lesson)
    
    def get_lessons(self) -> List[Lesson]:
        return self.__lessons


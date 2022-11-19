from typing import List, Dict

from vo.Day import Day
from vo.Lesson import Lesson


def group_lessons_by_day(array: [str]) -> Dict[str, Day]:
    groups: Dict[str, Day] = {}
    
    for item in array:
        lesson = Lesson(item['title'],
                        item['start'],
                        item['start'],
                        item['end'])
        key = lesson.get_key()
        
        try:
            groups[key].append_lesson(lesson)
        except KeyError:
            lessons = [lesson]
            day = Day(item['start'], lessons)
            groups.update({key: day})
        
    return groups


def format_message(groups: Dict[str, Day]) -> List[str]:
    list_of_lessons: List[str] = []
    
    for key, day in groups.items():
        one_day = [f'<b>{day.get_short_date()} — {day.get_weekday()}</b>\n']
        for lesson in day.get_lessons():
            one_day.append(
                f'<b>{lesson.get_short_start_time()}</b>   {lesson.get_title()}')
        list_of_lessons.append('\n'.join(one_day))
        
    return list_of_lessons

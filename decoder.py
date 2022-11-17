import re

from schedule_processor import PeriodType

DATE_EXTEND = "\\d{4}/\\d{2}/\\d{2}"
TIME_SIMPLE = "\\d{2}:\\d{2}"


def decode_json(array: [], period: str):
    list_of_lessons = []
    
    match PeriodType.get_by_value(period):
        case PeriodType.TODAY:
            list_of_lessons = decode_oneday_format(array)
        case PeriodType.TOMORROW:
            list_of_lessons = decode_oneday_format(array)
        case PeriodType.WEEK:
            list_of_lessons = decode_week_format(array)
    
    return list_of_lessons


def decode_oneday_format(array: []):
    one_day_list = []
    list_of_lessons = []
    
    for item in array:
        
        start_time = re.findall(TIME_SIMPLE, item["start"])[0]
        end_time = re.findall(TIME_SIMPLE, item["end"])[0]
        
        one_day_list.append(f'<b>{start_time} - {end_time}</b>   {item["title"]}')
        
    list_of_lessons.append('\n'.join(one_day_list))
    return list_of_lessons


def decode_week_format(array: []):
    one_day_list = []
    list_of_lessons = []
    previous_date = re.findall(DATE_EXTEND, array[0]['start'])
    
    for i in range(len(array)):
        
        item = array[i]
        
        current_date = re.findall(DATE_EXTEND, item['start'])
        start_time = re.findall(TIME_SIMPLE, item["start"])[0]
        end_time = re.findall(TIME_SIMPLE, item["end"])[0]
        
        if previous_date != current_date:
            
            previous_date = re.findall(DATE_EXTEND, item['start'])
            list_of_lessons.append('\n'.join(one_day_list))
            one_day_list = []
            
        one_day_list.append(f'<b>{start_time} - {end_time}</b>   {item["title"]}')
        
    list_of_lessons.append('\n'.join(one_day_list))
    return list_of_lessons

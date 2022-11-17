from schedule_processor import PeriodType


def decode_json(array, period):
    list_of_lessons = []
    
    match PeriodType.get_by_value(period):
        case PeriodType.TODAY:
            list_of_lessons = decode_oneday_format(array)
        case PeriodType.TOMORROW:
            list_of_lessons = decode_oneday_format(array)
        case PeriodType.WEEK:
            list_of_lessons = decode_week_format(array)
    
    return list_of_lessons


def decode_oneday_format(array):
    one_day_list = []
    list_of_lessons = []
    for item in array:
        one_day_list.append(f'<b>{item["start"]}</b> — <b>{item["title"]}</b>')
    list_of_lessons.append('\n'.join(one_day_list))
    return list_of_lessons


def decode_week_format(array):
    return []

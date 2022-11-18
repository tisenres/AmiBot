from datetime import datetime


def get_date_time_weekday(input_date_time: str):
    date_time_weekday = datetime.strptime(input_date_time, "%Y/%m/%d %I:%M:%S %p")
    
    time = date_time_weekday.strftime("%H:%M")
    date = date_time_weekday.strftime("%d %B")
    weekday = date_time_weekday.strftime("%A")
    
    return time, date, weekday


def decode_json(array: []):
    one_day_list = []
    list_of_lessons = []
    
    previous_start_date = get_date_time_weekday(array[0]["start"])[1]
    weekday = get_date_time_weekday(array[0]["start"])[2]
    title_of_list_of_lessons = f'<b>{previous_start_date} — {weekday}</b>\n\n'
    
    for item in array:
    
        start_time = get_date_time_weekday(item["start"])[0]
        end_time = get_date_time_weekday(item["end"])[0]
    
        start_date = get_date_time_weekday(item["start"])[1]
    
        title_of_lesson = item["title"]
    
        if start_date != previous_start_date:
    
            list_of_lessons.append(title_of_list_of_lessons + '\n'.join(one_day_list))
            one_day_list = []
            previous_start_date = start_date
            
            weekday = get_date_time_weekday(item["start"])[2]
            title_of_list_of_lessons = f'<b>{start_date} — {weekday}</b>\n\n'
    
        one_day_list.append(f'<b>{start_time} - {end_time}</b>   {title_of_lesson}')
    
    if len(one_day_list) != 0:
        list_of_lessons.append(title_of_list_of_lessons + '\n'.join(one_day_list))
    
    return list_of_lessons

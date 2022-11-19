import json
import re

from aiogram import types

import decoder
import schedule_processor
from create_bot import bot
from design.HtmlDecorator import bold
from handlers import other_handler
from schedule_processor import PeriodType

SECTION_ACRONYM = 'Sec'
BUTTON_TITLE_FORMAT = '%s %s %s'


def create_period_regex():
    enum_values = []
    for enum_value in PeriodType:
        enum_values.append(enum_value.value)
    
    period_types_string = "|".join(enum_values)
    return f'^({period_types_string})\\s{SECTION_ACRONYM}\\s(\\d+)$'


async def create_period_markup(chat_id: int, section: str):
    period_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for period_type in PeriodType:
        button = types.KeyboardButton(BUTTON_TITLE_FORMAT % (period_type.value, SECTION_ACRONYM, section))
        period_markup.insert(button)
    
    await bot.send_message(chat_id, 'Choose period', reply_markup=period_markup)


async def handle_period_button(message: types.Message):
    period_and_section = re.findall(create_period_regex(), message.text)
    if len(period_and_section) != 1 and len(period_and_section[0]) != 1:
        await other_handler.process_other_message(message)
        return
    
    period = PeriodType.get_by_value(period_and_section[0][0])
    section_num = int(period_and_section[0][1])
    
    try:
        json_schedule = schedule_processor.get_schedule(section_num, period)
    except NotImplementedError:
        await bot.send_message(message.from_user.id, f'Non implemented section {bold(f"{section_num}")}\n\n',
                               parse_mode='html')
        return
    
    array = json.loads(json_schedule)
    
    if len(array) > 0:
        schedule_dict = decoder.group_lessons_by_day(array)
        message_list = decoder.format_message(schedule_dict)
        
        await bot.send_message(message.from_user.id, f'Your Schedule for {bold(period.value)}\n\n',
                               parse_mode='html')
        for message_text in message_list:
            await bot.send_message(message.from_user.id, message_text,
                                   parse_mode='html')
    else:
        await bot.send_message(message.from_user.id, f'No schedule for {bold(period.value)}\n\n',
                               parse_mode='html')

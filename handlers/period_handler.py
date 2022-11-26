import json
import re
from typing import Dict

from aiogram import types, Dispatcher

import decoder
import schedule_processor
from create_bot import bot
from design.HtmlDecorator import bold
from handlers import other_handler, start_help_handler
from schedule_processor import PeriodType

SECTION_ACRONYM: str = 'Sec'
BUTTON_TITLE_FORMAT: str = '%s %s %s'
schedule_dict: Dict[str, decoder.Day] = {}


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

    waiting_for_request_message = await bot.send_message(message.from_user.id, bold('Waiting for request🕓'),
                                                         parse_mode='html')
    waiting_for_request_message_id = waiting_for_request_message['message_id']
    
    if len(period_and_section) != 1 and len(period_and_section[0]) != 1:
        await other_handler.process_other_message(message)
        
        return
    
    period = PeriodType.get_by_value(period_and_section[0][0])
    section_num = int(period_and_section[0][1])
    
    try:
        json_data = schedule_processor.get_schedule(section_num, period)
        array = json.loads(json_data)
    except NotImplementedError:
        await bot.send_message(message.from_user.id, f'Non implemented section {bold(f"{section_num}")}\n\n',
                               parse_mode='html')
        await bot.delete_message(message.from_user.id, waiting_for_request_message_id)
        
        return
    
    except ConnectionError:
        await bot.send_message(message.from_user.id, "Sorry, I can't reach the server because of technical problems😓",
                               parse_mode='html')
        await bot.delete_message(message.from_user.id, waiting_for_request_message_id)
        
        return
    
    if len(array) > 0:
        global schedule_dict
        schedule_dict = decoder.group_lessons_by_day(array)
        message_list = decoder.format_schedule_message(schedule_dict)
        await bot.send_message(message.from_user.id, f'Your Schedule for {bold(period.value)}\n\n',
                               parse_mode='html')
        
        for i in range(len(message_list)):
            show_add_info = types.InlineKeyboardMarkup(row_width=1)
            add_info_button = types.InlineKeyboardButton(text='Additional info', callback_data=list(schedule_dict)[i])
            show_add_info.add(add_info_button)
            await bot.send_message(message.from_user.id, message_list[i],
                                   reply_markup=show_add_info,
                                   parse_mode='html')
    else:
        await bot.send_message(message.from_user.id, f'No schedule for {bold(period.value)}\n\n',
                               parse_mode='html')

    await bot.delete_message(message.from_user.id, waiting_for_request_message_id)


# TODO implement this method
async def handle_additional_button(callback_data: types.CallbackQuery):
    await bot.answer_callback_query(callback_data.id)
    

def register_period_handler(dp: Dispatcher):
    global schedule_dict
    for key in schedule_dict:
        dp.register_callback_query_handler(handle_additional_button, text=f'{key}')

    
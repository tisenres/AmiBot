import json
import re
from typing import List

from aiogram import types

import decoder
import schedule_processor
from create_bot import bot
from design.HtmlDecorator import bold
from handlers import other_handler
from schedule_processor import PeriodType

SECTION_ACRONYM: str = 'Sec'
BUTTON_TITLE_FORMAT: str = '%s %s %s'


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
        await bot.delete_message(message.from_user.id, waiting_for_request_message_id)
        array = json.loads(json_data)
    except NotImplementedError:
        await bot.delete_message(message.from_user.id, waiting_for_request_message_id)
        await bot.send_message(message.from_user.id, f'Non implemented section {bold(f"{section_num}")}\n\n',
                               parse_mode='html')
        
        return
    
    except ConnectionError:
        await bot.delete_message(message.from_user.id, waiting_for_request_message_id)
        await bot.send_message(message.from_user.id, "Sorry, I can't reach the server because of technical problems😓",
                               parse_mode='html')
        
        return
    
    if len(array) > 0:
        
        id_list_messages: List[str] = []
        
        schedule_dict = decoder.group_lessons_by_day(array)
        message_list = decoder.format_schedule_message(schedule_dict)
        
        await bot.send_message(message.from_user.id, f'Your Schedule for {bold(period.value)}\n\n',
                               parse_mode='html')
        
        for i in range(len(message_list)):
            if i == (len(message_list) - 1):
                
                add_info_markup = types.InlineKeyboardMarkup(row_width=1)
                button = types.InlineKeyboardButton(text='Additional info', callback_data='Additional info')
                add_info_markup.add(button)
                sent_message = await bot.send_message(message.from_user.id, message_list[i],
                                                      reply_markup=add_info_markup,
                                                      parse_mode='html')
            else:
                
                sent_message = await bot.send_message(message.from_user.id, message_list[i],
                                                      parse_mode='html')
            
            sent_message_id = sent_message['message_id']
            id_list_messages.append(sent_message_id)
            
    else:
        await bot.send_message(message.from_user.id, f'No schedule for {bold(period.value)}\n\n',
                               parse_mode='html')


# TODO implement additional_button method
async def handle_additional_button(callback_data: types.CallbackQuery):
    await bot.send_message(callback_data.message.chat.id, 'Feature development in process🛠')
    await bot.answer_callback_query(callback_data.id)
    
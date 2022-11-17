import os
from random import randint
from create_bot import bot
from aiogram import types, Dispatcher
from handlers import period_handler

sections = [
    '1',
    '2',
    '3',
    '4',
]


async def show_intro_message(message: types.Message):
    choose_section = types.InlineKeyboardMarkup(row_width=2)
    for section in sections:
        button = types.InlineKeyboardButton(f'Section {section}', callback_data=f'{section}')
        choose_section.insert(button)
    
    if message.text == '/start':
        
        sticker = open(random_sticker('welcome_stickers'), "rb")
        await bot.send_sticker(message.chat.id, sticker)
        
        await bot.send_message(message.chat.id,
                               f"<b>Hello, {message.from_user.first_name}! 👋\n</b>My name is AmiBot!\n"
                               "I can show You the schedule of lessons of Amity University!",
                               parse_mode='html',
                               reply_markup=choose_section)
    
    elif message.text == '/help':
        
        await bot.send_message(message.chat.id,
                               'This bot helps You to check lessons schedule at Amity University. \n'
                               'Click on the button <b>below↓</b>',
                               parse_mode='html',
                               reply_markup=choose_section)


async def handler_section_button(callback_data: types.CallbackQuery):
    await period_handler.create_period_markup(callback_data.message.chat.id, callback_data.data)
    await bot.answer_callback_query(callback_data.id)


def register_start_help_handler(dp: Dispatcher):
    dp.register_message_handler(show_intro_message, commands=['start', 'help'])
    for section in sections:
        dp.register_callback_query_handler(handler_section_button, text=f'{section}')
        
    dp.register_message_handler(period_handler.handle_period_button, regexp=period_handler.create_period_regex())


def random_sticker(directory_path):
    number_of_files = os.listdir(path=".")
    return directory_path + '/' + str(randint(1, len(number_of_files) - 1)) + '.tgs'

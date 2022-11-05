import os
from random import randint

from create_bot import bot
from aiogram import types, Dispatcher


async def process_start_help_commands(message: types.Message):
    show_schedule = types.InlineKeyboardMarkup()
    schedule = types.InlineKeyboardButton('Show schedule', callback_data='show_schedule')
    show_schedule.add(schedule)
    
    if message.text == '/start':
        
        sticker = open(random_sticker('welcome_stickers'), "rb")
        await bot.send_sticker(message.chat.id, sticker)
        
        await bot.send_message(message.chat.id,
                               "<b>Hello, %s! 👋\n</b>My name is AmiBot!\nI can show You the schedule of lessons of Amity University!" % message.from_user.first_name,
                               parse_mode='html', reply_markup=show_schedule)
    
    elif message.text == '/help':
        
        await bot.send_message(message.chat.id,
                               'This bot helps You to check lessons schedule at Amity University. \nClick on the button <b>below↓</b>',
                               parse_mode='html',
                               reply_markup=show_schedule)


def register_start_help_handler(dp: Dispatcher):
    dp.register_message_handler(process_start_help_commands, commands=['start', 'help'])


def random_sticker(directory_path):
    files = os.listdir(path=".")
    return directory_path + '/' + str(randint(1, len(files))) + '.tgs'

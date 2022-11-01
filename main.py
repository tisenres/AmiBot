from random import randint
from datetime import datetime

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def process_start_help_commands(message: types.Message):
    
    show_schedule = types.InlineKeyboardMarkup()
    schedule = types.InlineKeyboardButton('Show schedule', callback_data='show_schedule')
    show_schedule.add(schedule)
    
    if message.text == '/start':
    
        sticker = open("welcome_stickers/%d.tgs" % randint(1, 4), "rb")
        await bot.send_sticker(message.chat.id, sticker)
        
        await bot.send_message(message.chat.id,
                               "<b>Hello, %s! 👋\n</b>My name is AmiBot!\nI can show You the schedule of lessons of Amity University!" % message.from_user.first_name,
                               parse_mode='html', reply_markup=show_schedule)
        
    elif message.text == '/help':
        
        await bot.send_message(message.chat.id, 'This bot helps You to check lessons schedule at Amity University. \nClick on the button <b>below↓</b>', parse_mode='html',
                               reply_markup=show_schedule)


@dp.callback_query_handler(text='show_schedule')
async def show_schedule(callback: types.CallbackQuery):
    choose_section = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    section1 = types.KeyboardButton('Section 1')
    section2 = types.KeyboardButton('Section 2')
    section3 = types.KeyboardButton('Section 3')
    section4 = types.KeyboardButton('Section 4')
    choose_section.add(section1, section2, section3, section4)

    await bot.send_message(callback.message.chat.id, 'Choose <b>the section</b>', parse_mode='html', reply_markup=choose_section)
    await bot.answer_callback_query(callback.id)
    
@dp.message_handler(text='Section 1')
async def process_section1_message(message: types.Message):
    weekday = datetime.today().strftime('%A')
    show_week_markup = types.InlineKeyboardMarkup()
    show_week = types.InlineKeyboardButton('Show week', callback_data='show_week_sec1')
    show_week_markup.add(show_week)
    
    await bot.send_message(message.from_user.id, 'THIS IS YOUR SCHEDULE FOR <b>%s</b>' % weekday, parse_mode='html', reply_markup=show_week_markup)


@dp.message_handler(text='Section 2')
async def process_section2_message(message: types.Message):
    weekday = datetime.today().strftime('%A')
    show_week_markup = types.InlineKeyboardMarkup()
    show_week = types.InlineKeyboardButton('Show week', callback_data='show_week_sec2')
    show_week_markup.add(show_week)
    
    await bot.send_message(message.from_user.id, 'THIS IS YOUR SCHEDULE FOR <b>%s</b>' % weekday, parse_mode='html',
                           reply_markup=show_week_markup)


@dp.message_handler(text='Section 3')
async def process_section3_message(message: types.Message):
    weekday = datetime.today().strftime('%A')
    show_week_markup = types.InlineKeyboardMarkup()
    show_week = types.InlineKeyboardButton('Show week', callback_data='show_week_sec3')
    show_week_markup.add(show_week)
    
    await bot.send_message(message.from_user.id, 'THIS IS YOUR SCHEDULE FOR <b>%s</b>' % weekday, parse_mode='html',
                           reply_markup=show_week_markup)


@dp.message_handler(text='Section 4')
async def process_section4_message(message: types.Message):
    weekday = datetime.today().strftime('%A')
    show_week_markup = types.InlineKeyboardMarkup()
    show_week = types.InlineKeyboardButton('Show week', callback_data='show_week_sec4')
    show_week_markup.add(show_week)
    
    await bot.send_message(message.from_user.id, 'THIS IS YOUR SCHEDULE FOR <b>%s</b>' % weekday, parse_mode='html',
                           reply_markup=show_week_markup)
    
@dp.callback_query_handler(text='show_week_sec1')
async def show_week_schedule_sec1(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, 'All week schedule for section 1', parse_mode='html')
    await bot.answer_callback_query(callback.id)
    
@dp.callback_query_handler(text='show_week_sec2')
async def show_week_schedule_sec2(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, 'All week schedule for section 2', parse_mode='html')
    await bot.answer_callback_query(callback.id)
    
@dp.callback_query_handler(text='show_week_sec3')
async def show_week_schedule_sec3(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, 'All week schedule for section 3', parse_mode='html')
    await bot.answer_callback_query(callback.id)
    
@dp.callback_query_handler(text='show_week_sec4')
async def show_week_schedule_sec3(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, 'All week schedule for section 4', parse_mode='html')
    await bot.answer_callback_query(callback.id)

@dp.message_handler()
async def process_schedule_message(message: types.Message):
    await bot.send_message(message.from_user.id, "Sorry, I didn't understand Your request😢. Send command /help")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
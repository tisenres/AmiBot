from random import randint

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
    weekday = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    monday = types.KeyboardButton('Monday')
    tuesday = types.KeyboardButton('Tuesday')
    wednesday = types.KeyboardButton('Wednesday')
    thursday = types.KeyboardButton('Thursday')
    friday = types.KeyboardButton('Friday')
    weekday.add(monday, tuesday, wednesday, thursday, friday)

    await bot.send_message(callback.message.chat.id, 'Choose <b>weekday</b>', parse_mode='html', reply_markup=weekday)
    await bot.answer_callback_query(callback.id)
    
@dp.message_handler(text='Monday')
async def process_monday_message(message: types.Message):
    choose_section = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    section1 = types.KeyboardButton('Section 1')
    section2 = types.KeyboardButton('Section 2')
    section3 = types.KeyboardButton('Section 3')
    section4 = types.KeyboardButton('Section 4')
    choose_section.add(section1, section2, section3, section4)
    
    await bot.send_message(message.from_user.id, 'Choose <b>the section</b>', parse_mode='html', reply_markup=choose_section)


@dp.message_handler(text='Tuesday')
async def process_monday_message(message: types.Message):
    choose_section = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    section1 = types.KeyboardButton('Section 1')
    section2 = types.KeyboardButton('Section 2')
    section3 = types.KeyboardButton('Section 3')
    section4 = types.KeyboardButton('Section 4')
    choose_section.add(section1, section2, section3, section4)
    
    await bot.send_message(message.from_user.id, 'Choose <b>the section</b>', parse_mode='html',
                           reply_markup=choose_section)


@dp.message_handler(text='Wednesday')
async def process_monday_message(message: types.Message):
    choose_section = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    section1 = types.KeyboardButton('Section 1')
    section2 = types.KeyboardButton('Section 2')
    section3 = types.KeyboardButton('Section 3')
    section4 = types.KeyboardButton('Section 4')
    choose_section.add(section1, section2, section3, section4)
    
    await bot.send_message(message.from_user.id, 'Choose <b>the section</b>', parse_mode='html',
                           reply_markup=choose_section)


@dp.message_handler(text='Thursday')
async def process_monday_message(message: types.Message):
    choose_section = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    section1 = types.KeyboardButton('Section 1')
    section2 = types.KeyboardButton('Section 2')
    section3 = types.KeyboardButton('Section 3')
    section4 = types.KeyboardButton('Section 4')
    choose_section.add(section1, section2, section3, section4)
    
    await bot.send_message(message.from_user.id, 'Choose <b>the section</b>', parse_mode='html',
                           reply_markup=choose_section)


@dp.message_handler(text='Friday')
async def process_monday_message(message: types.Message):
    choose_section = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    section2 = types.KeyboardButton('Section 2')
    choose_section.add(section2)
    
    await bot.send_message(message.from_user.id, 'Choose <b>the section</b>', parse_mode='html',
                           reply_markup=choose_section)

@dp.message_handler()
async def process_schedule_message(message: types.Message):
    await bot.send_message(message.from_user.id, "Sorry, I didn't understand Your request😢. Send command /help")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
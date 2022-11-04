from datetime import datetime
from create_bot import bot, dp
from aiogram import types, Dispatcher


# @dp.message_handler(text='Section 1')
async def process_section1_message(message: types.Message):
    weekday = datetime.today().strftime('%A')
    show_markup = types.InlineKeyboardMarkup()
    show_week = types.InlineKeyboardButton('Show week', callback_data='show_week_sec1')
    show_tmr = types.InlineKeyboardButton('Show tomorrow', callback_data='show_tmr_sec1')
    show_markup.add(show_week, show_tmr)
    
    await bot.send_message(message.from_user.id, 'THIS IS YOUR SCHEDULE FOR <b>%s</b>' % weekday, parse_mode='html',
                           reply_markup=show_markup)


# @dp.message_handler(text='Section 2')
async def process_section2_message(message: types.Message):
    weekday = datetime.today().strftime('%A')
    show_markup = types.InlineKeyboardMarkup()
    show_week = types.InlineKeyboardButton('Show week', callback_data='show_week_sec2')
    show_tmr = types.InlineKeyboardButton('Show tomorrow', callback_data='show_tmr_sec2')
    show_markup.add(show_week, show_tmr)
    
    await bot.send_message(message.from_user.id, 'THIS IS YOUR SCHEDULE FOR <b>%s</b>' % weekday, parse_mode='html',
                           reply_markup=show_markup)


# @dp.message_handler(text='Section 3')
async def process_section3_message(message: types.Message):
    weekday = datetime.today().strftime('%A')
    show_markup = types.InlineKeyboardMarkup()
    show_week = types.InlineKeyboardButton('Show week', callback_data='show_week_sec3')
    show_tmr = types.InlineKeyboardButton('Show tomorrow', callback_data='show_tmr_sec3')
    show_markup.add(show_week, show_tmr)
    
    await bot.send_message(message.from_user.id, 'THIS IS YOUR SCHEDULE FOR <b>%s</b>' % weekday, parse_mode='html',
                           reply_markup=show_markup)


# @dp.message_handler(text='Section 4')
async def process_section4_message(message: types.Message):
    weekday = datetime.today().strftime('%A')
    show_markup = types.InlineKeyboardMarkup()
    show_week = types.InlineKeyboardButton('Show week', callback_data='show_week_sec4')
    show_tmr = types.InlineKeyboardButton('Show tomorrow', callback_data='show_tmr_sec4')
    show_markup.add(show_week, show_tmr)
    
    await bot.send_message(message.from_user.id, 'THIS IS YOUR SCHEDULE FOR <b>%s</b>' % weekday, parse_mode='html',
                           reply_markup=show_markup)
    
def register_handlers_choose_sections(dp : Dispatcher):
    dp.register_message_handler(process_section1_message, text='Section 1')
    dp.register_message_handler(process_section2_message, text='Section 2')
    dp.register_message_handler(process_section3_message, text='Section 3')
    dp.register_message_handler(process_section4_message, text='Section 4')
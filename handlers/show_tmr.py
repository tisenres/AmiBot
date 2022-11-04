from create_bot import bot, dp
from aiogram import types, Dispatcher

# @dp.callback_query_handler(text='show_tmr_sec1')
async def show_tmr_schedule_sec1(callback: types.CallbackQuery):
    show_markup = types.InlineKeyboardMarkup()
    show_tmr = types.InlineKeyboardButton('Show week', callback_data='show_week_sec1')
    show_markup.add(show_tmr)
    await bot.send_message(callback.message.chat.id, 'All week schedule for section 1', parse_mode='html', reply_markup=show_markup)
    await bot.answer_callback_query(callback.id)


# @dp.callback_query_handler(text='show_tmr_sec2')
async def show_tmr_schedule_sec2(callback: types.CallbackQuery):
    show_markup = types.InlineKeyboardMarkup()
    show_tmr = types.InlineKeyboardButton('Show week', callback_data='show_week_sec2')
    show_markup.add(show_tmr)
    await bot.send_message(callback.message.chat.id, 'All week schedule for section 2', parse_mode='html', reply_markup=show_markup)
    await bot.answer_callback_query(callback.id)


# @dp.callback_query_handler(text='show_tmr_sec3')
async def show_tmr_schedule_sec3(callback: types.CallbackQuery):
    show_markup = types.InlineKeyboardMarkup()
    show_tmr = types.InlineKeyboardButton('Show week', callback_data='show_week_sec3')
    show_markup.add(show_tmr)
    await bot.send_message(callback.message.chat.id, 'All week schedule for section 3', parse_mode='html', reply_markup=show_markup)
    await bot.answer_callback_query(callback.id)


# @dp.callback_query_handler(text='show_tmr_sec4')
async def show_tmr_schedule_sec4(callback: types.CallbackQuery):
    show_markup = types.InlineKeyboardMarkup()
    show_tmr = types.InlineKeyboardButton('Show week', callback_data='show_week_sec4')
    show_markup.add(show_tmr)
    await bot.send_message(callback.message.chat.id, 'All week schedule for section 4', parse_mode='html', reply_markup=show_markup)
    await bot.answer_callback_query(callback.id)
    
def register_handlers_show_tmr(dp : Dispatcher):
    dp.register_callback_query_handler(show_tmr_schedule_sec1, text='show_tmr_sec1')
    dp.register_callback_query_handler(show_tmr_schedule_sec2, text='show_tmr_sec2')
    dp.register_callback_query_handler(show_tmr_schedule_sec3, text='show_tmr_sec3')
    dp.register_callback_query_handler(show_tmr_schedule_sec4, text='show_tmr_sec4')
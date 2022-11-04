from create_bot import bot, dp
from aiogram import types, Dispatcher

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
async def show_week_schedule_sec4(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, 'All week schedule for section 4', parse_mode='html')
    await bot.answer_callback_query(callback.id)
    
def register_handlers_show_week(dp : Dispatcher):
    dp.register_callback_query_handler(show_week_schedule_sec1, text='show_week_sec1')
    dp.register_callback_query_handler(show_week_schedule_sec2, text='show_week_sec2')
    dp.register_callback_query_handler(show_week_schedule_sec3, text='show_week_sec3')
    dp.register_callback_query_handler(show_week_schedule_sec4, text='show_week_sec4')
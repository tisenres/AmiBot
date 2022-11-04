from create_bot import bot, dp
from aiogram import types, Dispatcher

# @dp.callback_query_handler(text='show_schedule')
async def show_schedule(callback: types.CallbackQuery):
    choose_section = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1, )
    section1 = types.KeyboardButton('Section 1')
    section2 = types.KeyboardButton('Section 2')
    section3 = types.KeyboardButton('Section 3')
    section4 = types.KeyboardButton('Section 4')
    choose_section.add(section1, section2, section3, section4)
    
    await bot.send_message(callback.message.chat.id, 'Choose <b>the section</b>', parse_mode='html',
                           reply_markup=choose_section)
    await bot.answer_callback_query(callback.id)
    
def register_handlers_show_schedule(dp : Dispatcher):
    dp.register_callback_query_handler(show_schedule, text='show_schedule')

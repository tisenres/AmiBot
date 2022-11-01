from main import bot, dp
from aiogram import types


@dp.callback_query_handlers(text='show_schedule')
async def show_schedule(callback: types.CallbackQuery):
    weekday = types.InlineKeyboardMarkup()
    monday = types.InlineKeyboardButton('Monday', callback_data='monday')
    tuesday = types.InlineKeyboardButton('Tuesday', callback_data='tuesday')
    wednesday = types.InlineKeyboardButton('Wednesday', callback_data='wednesday')
    thursday = types.InlineKeyboardButton('Thursday', callback_data='thursday')
    friday = types.InlineKeyboardButton('Friday', callback_data='friday')
    weekday.add(monday, tuesday, wednesday, thursday)

    await bot.send_message(callback.message.chat.id, 'Choose <b>weekday</b>', parse_mode='html', reply_markup=weekday)
    await bot.answer_callback_query(callback.id)


@dp.callback_query_handlers(text='monday')
async def show_schedule(callback: types.CallbackQuery):
    section_num = types.InlineKeyboardMarkup()
    sec1 = types.InlineKeyboardButton('Section 1', callback_data='sec1mon')
    sec2 = types.InlineKeyboardButton('Section 2', callback_data='sec2mon')
    sec3 = types.InlineKeyboardButton('Section 3', callback_data='sec3mon')
    sec4 = types.InlineKeyboardButton('Section 4', callback_data='sec4mon')
    section_num.add(sec1, sec2, sec3, sec4)

    await bot.send_message(callback.message.chat.id, 'Choose <b>the section</b>', parse_mode='html',
                           reply_markup=section_num)
    await bot.answer_callback_query(callback.id)


@dp.callback_query_handlers(text='tuesday')
async def show_schedule(callback: types.CallbackQuery):
    section_num = types.InlineKeyboardMarkup()
    sec1 = types.InlineKeyboardButton('Section 1', callback_data='sec1tues')
    sec2 = types.InlineKeyboardButton('Section 2', callback_data='sec2tues')
    sec3 = types.InlineKeyboardButton('Section 3', callback_data='sec3tues')
    sec4 = types.InlineKeyboardButton('Section 4', callback_data='sec4tues')
    section_num.add(sec1, sec2, sec3, sec4)

    await bot.send_message(callback.message.chat.id, 'Choose <b>the section</b>', parse_mode='html',
                           reply_markup=section_num)
    await bot.answer_callback_query(callback.id)


@dp.callback_query_handlers(text='wednesday')
async def show_schedule(callback: types.CallbackQuery):
    section_num = types.InlineKeyboardMarkup()
    sec1 = types.InlineKeyboardButton('Section 1', callback_data='sec1wed')
    sec2 = types.InlineKeyboardButton('Section 2', callback_data='sec2wed')
    sec3 = types.InlineKeyboardButton('Section 3', callback_data='sec3wed')
    sec4 = types.InlineKeyboardButton('Section 4', callback_data='sec4wed')
    section_num.add(sec1, sec2, sec3, sec4)

    await bot.send_message(callback.message.chat.id, 'Choose <b>the section</b>', parse_mode='html',
                           reply_markup=section_num)
    await bot.answer_callback_query(callback.id)


@dp.callback_query_handlers(text='thursday')
async def show_schedule(callback: types.CallbackQuery):
    section_num = types.InlineKeyboardMarkup()
    sec1 = types.InlineKeyboardButton('Section 1', callback_data='sec1thur')
    sec2 = types.InlineKeyboardButton('Section 2', callback_data='sec2thur')
    sec3 = types.InlineKeyboardButton('Section 3', callback_data='sec3thur')
    sec4 = types.InlineKeyboardButton('Section 4', callback_data='sec4thur')
    section_num.add(sec1, sec2, sec3, sec4)

    await bot.send_message(callback.message.chat.id, 'Choose <b>the section</b>', parse_mode='html',
                           reply_markup=section_num)
    await bot.answer_callback_query(callback.id)


@dp.callback_query_handlers(text='friday')
async def show_schedule(callback: types.CallbackQuery):
    section_num = types.InlineKeyboardMarkup()
    sec1 = types.InlineKeyboardButton('Section 1', callback_data='sec1fri')
    sec2 = types.InlineKeyboardButton('Section 2', callback_data='sec2fri')
    sec3 = types.InlineKeyboardButton('Section 3', callback_data='sec3fri')
    sec4 = types.InlineKeyboardButton('Section 4', callback_data='sec4fri')
    section_num.add(sec1, sec2, sec3, sec4)

    await bot.send_message(callback.message.chat.id, 'Choose <b>the section</b>', parse_mode='html',
                           reply_markup=section_num)
    await bot.answer_callback_query(callback.id)

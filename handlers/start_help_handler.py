import os
from random import randint

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import bold

from create_bot import bot
from handlers import period_handler

router = Router()

sections = ['1', '2', '3', '4']

def get_section_keyboard():
    keyboard = [
        [InlineKeyboardButton(text=f'Section {section}', callback_data=f'section_{section}')]
        for section in sections
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

@router.message(Command("start"))
async def show_start_message(message: types.Message):
    sticker_path = random_sticker()
    await message.answer_sticker(sticker=types.FSInputFile(sticker_path))

    await message.answer(
        f"{bold(f'Hello, {message.from_user.first_name}! 👋')}\n"
        "My name is AmiBot!\n"
        "I can show You the schedule of lessons of Amity University!",
        reply_markup=get_section_keyboard()
    )

@router.message(Command("help"))
async def show_help_message(message: types.Message):
    await message.answer(
        f'This bot helps You to check lessons schedule at Amity University. \n'
        f'Click on the button {bold("below↓")}',
        reply_markup=get_section_keyboard()
    )

@router.callback_query(F.data.startswith("section_"))
async def handle_section_button(callback: types.CallbackQuery):
    section = callback.data.split("_")[1]
    await callback.answer()

    waiting_message = await callback.message.answer(bold('Waiting for request🕓'))
    await waiting_message.delete()

    await period_handler.create_period_markup(callback.message.chat.id, section)

def random_sticker():
    directory_path = 'welcome_stickers'
    number_of_files = len(os.listdir(directory_path))
    return f"{directory_path}/{randint(1, number_of_files)}.tgs"

def register_handlers(dp):
    dp.include_router(router)
    # Include period_handler router
    dp.include_router(period_handler.router)
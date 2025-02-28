import os
from random import randint

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import bold
from typing_extensions import Optional

from domain.generate_section_data import generate_section_data
from handlers import period_handler
from vo.Section import Section

router = Router()
departments = generate_section_data()

def get_departments_keyboard():
    keyboard = [
        [InlineKeyboardButton(text=f'Department {department}', callback_data=f'department_{department}')]
        for department in departments
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


@router.message(Command("start"))
async def show_start_message(message: types.Message):
    # sticker_path = random_sticker()
    # await message.answer_sticker(sticker=types.FSInputFile(sticker_path))

    await message.answer(
        f"**Hello, {message.from_user.first_name}! 👋**\n"
        "Here you can see the timetable in Amity University!",
        parse_mode="Markdown",
        reply_markup=get_departments_keyboard()
    )


@router.message(Command("help"))
async def show_help_message(message: types.Message):
    await message.answer(
        f'The bot will help you view your Amity University class schedule. \n'
        f'Click on the button {bold("below↓")}',
        reply_markup=get_departments_keyboard()
    )


@router.callback_query(F.data.startswith("department_"))
async def handle_department_keyboard(callback: types.CallbackQuery):
    await callback.answer()
    department_name = callback.data.split("_")[1]

    batches = next((dept.batches for dept in departments if dept.title == department_name), None)

    if not batches:
        await callback.message.answer("No batches found.")
        return

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f'Batch {batch.title}',
                                  callback_data=f'batch_{department_name}_{batch.title}')]
            for batch in batches
        ]
    )

    await callback.message.edit_text(
        f"Select a batch in {department_name}:",
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("batch_"))
async def handle_batch_keyboard(callback: types.CallbackQuery):
    await callback.answer()
    callback_data = callback.data.split("_")
    department_name = callback_data[1]
    batch_name = callback_data[2]

    sections = next(
        (batch.sections for dept in departments if dept.title == department_name
         for batch in dept.batches if batch.title == batch_name),
        None
    )

    if not sections:
        await callback.message.answer("No batches found.")
        return

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f'Section {section.title}',
                                  callback_data=f'section_{department_name}_{batch_name}_{section.title}')]
            for section in sections
        ]
    )

    await callback.message.edit_text(
        f"Select a section in {batch_name}:",
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("section_"))
async def handle_section_keyboard(callback: types.CallbackQuery):
    callback_data = callback.data.split("_")
    department_name = callback_data[1]
    batch_name = callback_data[2]
    section_name = callback_data[3]

    current_section: Optional[Section] = None

    for dept in departments:
        if dept.title == department_name:
            for batch in dept.batches:
                if batch.title == batch_name:
                    for section in batch.sections:
                        if section.title == section_name:
                            section_name = section.title
                            current_section = section

    await callback.answer()

    waiting_message = await callback.message.answer(bold('Waiting for request... 🕓'))
    await waiting_message.delete()

    await period_handler.create_period_markup(callback.message, current_section)


def random_sticker():
    directory_path = 'welcome_stickers'
    number_of_files = len(os.listdir(directory_path))
    return f"{directory_path}/{randint(1, number_of_files)}.tgs"


def register_handlers(dp):
    dp.include_router(router)
    dp.include_router(period_handler.router)

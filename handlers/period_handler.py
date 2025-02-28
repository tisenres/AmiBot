import json
import re
from typing import Optional

from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import bold

from domain import schedule_processor, decoder
from domain.schedule_processor import PeriodType
from vo.Section import Section

router = Router()

SECTION_ACRONYM: str = 'Sec'
BUTTON_TITLE_FORMAT: str = '%s %s %s'
selected_section: Optional[Section] = None


def create_period_regex():
    enum_values = [enum_value.value for enum_value in PeriodType]
    period_types_string = "|".join(enum_values)
    return f'^({period_types_string})\\s{SECTION_ACRONYM}\\s(\\w+)$'


async def create_period_markup(message: types.Message, section: Section):
    global selected_section
    selected_section = section

    buttons = [
        [KeyboardButton(text=BUTTON_TITLE_FORMAT % (period_type.value, SECTION_ACRONYM, section.title))]
        for period_type in PeriodType
    ]
    period_markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    await message.bot.send_message(
        message.chat.id,
        'Choose period',
        reply_markup=period_markup,
    )


@router.message(lambda message: re.match(create_period_regex(), message.text))
async def handle_period_button(message: types.Message):
    period_and_section = re.findall(create_period_regex(), message.text)[0]

    waiting_for_request_message = await message.answer(text='Waiting for request... 🕓')

    # if len(period) != 2:
    #     await other_handler.process_other_message(message)
    #     return

    # section = message.reply_parameters.get("selected_section")
    period = PeriodType.get_by_value(period_and_section[0])

    try:
        json_data = schedule_processor.get_schedule(selected_section, period)
        await waiting_for_request_message.delete()
        array = json.loads(json_data)
    except NotImplementedError:
        await waiting_for_request_message.delete()
        await message.answer(f'Non implemented section {bold(f"{selected_section}")}\n\n')
        return
    except ConnectionError:
        await waiting_for_request_message.delete()
        await message.answer("Sorry, I can't reach the server because of technical problems😓")
        return
    # except JSONDecodeError:
    #     await waiting_for_request_message.delete()
    #     await message.answer("Sorry, 😓")

    if array:
        schedule_dict = decoder.group_lessons_by_day(array)
        message_list = decoder.format_schedule_message(schedule_dict)

        await message.answer(f'Your Schedule for {bold(period.value)}\n\n')

        for i, msg in enumerate(message_list):
            if i == len(message_list) - 1:
                add_info_markup = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Additional info', callback_data='Additional info')]
                ])
                await message.answer(msg, reply_markup=add_info_markup)
            else:
                await message.answer(msg)
    else:
        await message.answer(f'No schedule for {bold(period.value)}\n\n')


@router.callback_query(F.data == "Additional info")
async def handle_additional_button(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Feature development in process🛠')

from create_bot import bot
from aiogram import types, Dispatcher, Router

router = Router()

@router.message()
async def process_other_message(message: types.Message):
    await bot.send_message(message.from_user.id, "Sorry, I didn't understand your request 😢. Send command /help")
    

def register_other_handler(dp: Dispatcher):
    dp.include_router(router)
from create_bot import bot, dp
from aiogram import types, Dispatcher

# @dp.message_handler()
async def process_others_message(message: types.Message):
    await bot.send_message(message.from_user.id, "Sorry, I didn't understand Your request😢. Send command /help")
    
def register_handlers_others(dp : Dispatcher):
    dp.register_message_handler(process_others_message)
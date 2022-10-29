from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply("Hello, %s!\nWelcome to test bot! \nThis bot shows the list of lessons (schedule) for Amity students!" % message.from_user.first_name)


@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message)
                        

executor.start_polling(dp)
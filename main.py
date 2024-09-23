import asyncio
from aiogram import Bot, Dispatcher
from create_bot import bot
from handlers import start_help_handler, period_handler


async def main():
    dp = Dispatcher()

    # Register handlers from both modules
    start_help_handler.register_handlers(dp)
    # period_handler is now included via start_help_handler.register_handlers

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
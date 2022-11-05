from create_bot import dp
from aiogram.utils import executor

from handlers import start_help_handler, other_handler

start_help_handler.register_start_help_handler(dp)
other_handler.register_other_handler(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

from create_bot import dp
from aiogram.utils import executor

from handlers import start_help, choose_sections, others, show_schedule, show_tmr, show_week

start_help.register_start_help_handler(dp)
choose_sections.register_handlers_choose_sections(dp)
show_schedule.register_handlers_show_schedule(dp)
show_tmr.register_handlers_show_tmr(dp)
show_week.register_handlers_show_week(dp)
others.register_handlers_others(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
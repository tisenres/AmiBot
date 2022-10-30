from random import randint

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


number_of_sections = 4


@dp.message_handler(commands=['start', 'help'])
async def process_start_help_commands(message: types.Message):
    
    # Create common Markup to SHOW SCHEDULE (for both START and HELP)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    schedule = types.KeyboardButton('Show schedule')
    markup.add(schedule)

    
    # Do some actions in case START or HELP
    
    
    if message.text == '/start':
    
        # Send welcome sticker
        
        sticker = open('welcome_stickers/%d.tgs' % randint(1, 4), 'rb')
        await bot.send_sticker(message.chat.id, sticker)

        # Send welcome message
        
        await bot.send_message(message.chat.id,
                               "<b>Hello, %s! 👋\n</b>My name is AmiBot!\nI can show You the schedule of lessons of Amity University!" % message.from_user.first_name,
                               parse_mode='html', reply_markup=markup)
        
    elif message.text == '/help':
        
        # Send help message
        
        await bot.send_message(message.chat.id, 'Click on the button <b><u>Show schedule</u></b> ↓', parse_mode='html',
                               reply_markup=markup)


@dp.message_handler(content_types=['text'])
async def process_schedule_message(message: types.Message):
    
    # Do some actions in case SHOW SCHEDULE or UNKNOWN TEXT
    
    if message.text == 'Show schedule':
    
        # Create Markup to CLARIFY SCHEDULE SEARCH
        
        buttons_of_sections = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=number_of_sections)
        
        # Create LOOP and fill our markup with BUTTONS. Number of buttons depends on number_of_sections variable
        
        for i in range(number_of_sections):
            button = types.KeyboardButton(str(i + 1) + ' section')
            buttons_of_sections.row(button)
            
        # Send clarifying message and show SECTIONS BUTTONS to user
        
        await bot.send_message(message.from_user.id, '<b>Choose the section</b> ↓', parse_mode='html',
                               reply_markup=buttons_of_sections)
        
    else:
        
        # Send special message for unknown text
        
        await bot.send_message(message.from_user.id, "Sorry, I didn't understand Your request😢. Send command /start")
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

import telebot
import asyncio
import threading

API_TOKEN = '7787566059:AAERi_p07C7EFHvywTR3YwIqgtiAFoQZ6_c'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='1 минута', callback_data='1min')
    button2 = telebot.types.InlineKeyboardButton(text='5 минут', callback_data='5min')
    button3 = telebot.types.InlineKeyboardButton(text='10 минут', callback_data='10min')
    button4 = telebot.types.InlineKeyboardButton(text='15 минут', callback_data='15min')

    keyboard.add(button1, button2)
    keyboard.add(button3, button4)
    bot.send_message(message.chat.id, "Я бот таймер! выбери нужное время:", reply_markup=keyboard)

async def time_out_send(call):
    chat_id = call.message.chat.id
    
    if call.data == '1min':
        await asyncio.sleep(60) 
        bot.send_message(chat_id, '1 минута прошла!')
    elif call.data == '5min':
        await asyncio.sleep(300)
        bot.send_message(chat_id, '5 минут прошло')
    elif call.data == '10min':
        await asyncio.sleep(600)
        bot.send_message(chat_id, '10 минут прошло')
    elif call.data == '15min':
        await asyncio.sleep(900)
        bot.send_message(chat_id, '15 минут прошло')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    def run_async():
        asyncio.run(time_out_send(call))
    
    threading.Thread(target=run_async).start()
    bot.answer_callback_query(call.id, "Таймер запущен!")


bot.polling(non_stop=True)
import telebot

bot = telebot.TeleBot('1099782868:AAGWpSTmV8i9FyTkrnfo2aWzjOYgyB-ZtQ4')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


bot.polling()

import telebot
import psycopg2

bot = telebot.TeleBot('1099782868:AAGWpSTmV8i9FyTkrnfo2aWzjOYgyB-ZtQ4')


DATABASE_URL = os.environ['DATABASE_URL']

con = psycopg2.connect(DATABASE_URL, sslmode='require')

print("Database opened successfully")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler()
def start_message(message):
    #bot.send_message(message.chat.id, 'Привет, ты написал мне /start')э
    s = str(message.text)
    print(s)

    try:
        cur = con.cursor()
        cur.execute(s)
        ans = cur.fetchall()
        con.commit()
        ans_m = ''
        for row in ans:
            gg = str(row)
            while gg.find('  ') != -1:
                gg = gg.replace('  ', ' ')
            ans_m += gg + '\n'
        print(ans_m)
        if ans_m != '':
            bot.send_message(message.chat.id, ans_m)
    except Exception as e:
        bot.send_message(message.chat.id, 'ну ты обосрался леха')
        bot.send_message(message.chat.id, e)
        con.commit()


bot.polling(none_stop=True)

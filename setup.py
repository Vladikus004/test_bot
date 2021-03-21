import telebot
import psycopg2

bot = telebot.TeleBot('1099782868:AAGWpSTmV8i9FyTkrnfo2aWzjOYgyB-ZtQ4')

DATABASE_URL = 'postgres://qaqopfmrjyeqgf:c8d7ea9b7ac4e482e15d5b9806650b9439590105946b06fd766d878e5672ffb6@ec2-63-34-97-163.eu-west-1.compute.amazonaws.com:5432/d826n89f0qe5qq'
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

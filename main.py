import telebot
import config
import os
from time import sleep
import time

import requests

bot = telebot.TeleBot(config.token)

# echo bot function   /  функция эхо
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#     bot.send_message(message.chat.id, message.text)



@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/'+file, 'rb')
            print(f)
            msg = bot.send_voice(message.chat.id, f, None)
            # А теперь отправим вслед за файлом его file_id  (* msg.voice.file_id)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)


if __name__ == '__main__':
    bot.polling(none_stop=True)











# работаяюща функции из предыдущего лессона
# URL = 'https://api.telegram.org/bot' + constants.token + '/'
# def get_updates():
#     url = URL + 'getupdates'
#     r = requests.get(url)
#     return r.json()
# print(get_updates())

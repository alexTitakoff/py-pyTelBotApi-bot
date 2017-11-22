import telebot
import constants
import requests

bot = telebot.TeleBot(constants.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)


# работаяюща функции из предыдущего лессона
# URL = 'https://api.telegram.org/bot' + constants.token + '/'
# def get_updates():
#     url = URL + 'getupdates'
#     r = requests.get(url)
#     return r.json()
# print(get_updates())

import time
from pprint import pprint

import telebot

# API_KEY = 'https://api.telegram.org/bot5239855839:AAGpK1VN7Lr2LDkq0WRC4onTLbYTWyrcc3g/'
token = '5239855839:AAGpK1VN7Lr2LDkq0WRC4onTLbYTWyrcc3g'
bot = telebot.TeleBot(token)
chat_id = -1001634300078


def send_post(media: list, caption):
    time.sleep(2)

    f1 = open(media[0].split('/')[1] + '/' + media[0].split('/')[2], 'rb')
    f1 = f1.read()
    f2 = open(media[1].split('/')[1] + '/' + media[1].split('/')[2], 'rb')
    f2 = f2.read()
    f3 = open(media[2].split('/')[1] + '/' + media[2].split('/')[2], 'rb')
    f3 = f3.read()
    bot.send_media_group(chat_id=chat_id, media=[
        telebot.types.InputMediaPhoto(f1, caption=caption),
        telebot.types.InputMediaPhoto(f2),
        telebot.types.InputMediaPhoto(f3),
    ])
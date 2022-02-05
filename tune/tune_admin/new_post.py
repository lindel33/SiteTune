from pprint import pprint

import telebot

API_KEY = 'https://api.telegram.org/bot5292093759:AAEV6_CcQveXLkgLeVO47Fg6MrJJ4cLVl8E/'
token = '5292093759:AAEV6_CcQveXLkgLeVO47Fg6MrJJ4cLVl8E'
bot = telebot.TeleBot(token)
chat_id = -1001392557374


def send_post(media: list, caption):
    pprint(media)
    f1 = open('media/' + media[0], 'rb')
    f1 = f1.read()
    f2 = open('media/' + media[1], 'rb')
    f2 = f2.read()
    f3 = open('media/' + media[2], 'rb')
    f3 = f3.read()
    bot.send_media_group(chat_id=chat_id, media=[
        telebot.types.InputMediaPhoto(f1, caption=caption),
        telebot.types.InputMediaPhoto(f2),
        telebot.types.InputMediaPhoto(f3),

    ])
# -*- coding: utf-8 -*-
import time
from pprint import pprint
import telebot
from data import get_category, get_products, get_detail_product

API_KEY = 'https://api.telegram.org/bot5292093759:AAHrxxCOr58zIQzmzaxZ98-IYucJE4pmFWs/'
token = '5292093759:AAHrxxCOr58zIQzmzaxZ98-IYucJE4pmFWs'
client = telebot.TeleBot(token)
chat_id = -1001392557374

category = get_category()
category_all = [x for x in category]
categories = [[x[1]] for x in category]
category_list = [x[1] for x in category]


@client.message_handler(commands=['start'])
def start_message(message):
    keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_category.keyboard = categories
    client.send_message(chat_id=message.chat.id,
                        text='Что хотите найти?',
                        reply_markup=keyboard_category)


@client.message_handler(content_types=['text'])
def get_all_product(message):
    if message.text in category_list:
        idc = [x[0] for x in category_all if x[1] == message.text][0]
        products = [[x[0]] for x in get_products(idc)]
        if products:
            keyboard_products = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard_products.keyboard = products
            client.send_message(chat_id=message.chat.id,
                                text='Ищу: ' + message.text,
                                reply_markup=keyboard_products)
            return 0
        else:
            time.sleep(2)
            keyboard_products = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard_products.keyboard = products
            client.send_message(chat_id=message.chat.id,
                                text='Сейчас в этой категории пусто 😔 ',
                                reply_markup=keyboard_products)
    else:
        try:
            detail_product = get_detail_product(message.text)

            if detail_product[1] != 'default.jpg':
                f1 = open(detail_product[1], 'rb')
                f1 = f1.read()
                f2 = open(detail_product[2], 'rb')
                f2 = f2.read()
                f3 = open(detail_product[3], 'rb')
                f3 = f3.read()
            else:
                f1, f2, f3 = open('default.jpg', 'rb'), open('default.jpg', 'rb'), open('default.jpg', 'rb')
                f1, f2, f3 = f1.read(), f2.read(), f3.read()
            client.send_media_group(chat_id=message.chat.id, media=[
            telebot.types.InputMediaPhoto(f1, caption=detail_product[8]),
            telebot.types.InputMediaPhoto(f2),
            telebot.types.InputMediaPhoto(f3),

            ])
        except:
            client.send_message(chat_id=message.chat.id,
                                text='Не нашел ничего 🙄',
                                )
            keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard_category.keyboard = categories
            client.send_message(chat_id=message.chat.id,
                                text='Найдём что-то другое? 🙃',
                                reply_markup=keyboard_category)
            return 0

        keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_category.keyboard = categories
        client.send_message(chat_id=message.chat.id,
                            text='Что ещё посмотрим? 🤗',
                            reply_markup=keyboard_category)
        return 0
    keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_category.keyboard = categories
    client.send_message(chat_id=message.chat.id,
                        text='Что ещё посмотрим? ',
                        reply_markup=keyboard_category)

client.polling(none_stop=True)
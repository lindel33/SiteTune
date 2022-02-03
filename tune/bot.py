# -*- coding: utf-8 -*-
import telebot
from data import get_category, get_products

API_KEY = 'https://api.telegram.org/bot5292093759:AAEV6_CcQveXLkgLeVO47Fg6MrJJ4cLVl8E/'
token = '5292093759:AAEV6_CcQveXLkgLeVO47Fg6MrJJ4cLVl8E'
bot = telebot.TeleBot(token)
chat_id = -1001392557374


category = get_category()
category_all = [x for x in category]
categories = [[x[1]] for x in category]
category_list = [x[1] for x in category]


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_category.keyboard = categories
    bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard_category)


@bot.message_handler(content_types=['text'])
def get_all_product(message):
    if message.text in category_list:
        idc = [x[0] for x in category_all if x[1] == message.text][0]
        products = [[x[0]] for x in get_products(idc)]
        keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_category.keyboard = products
        bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard_category)
    if message.text.lower() == 'назад':
        start_message()

bot.polling()
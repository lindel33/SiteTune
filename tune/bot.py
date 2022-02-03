# -*- coding: utf-8 -*-
import json
from pprint import pprint

import telebot
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from data import get_category

API_KEY = 'https://api.telegram.org/bot5292093759:AAEV6_CcQveXLkgLeVO47Fg6MrJJ4cLVl8E/'
token = '5292093759:AAEV6_CcQveXLkgLeVO47Fg6MrJJ4cLVl8E'
bot = telebot.TeleBot(token)
chat_id = -1001392557374


pprint(get_category())

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Товары', 'Проверить наличие', )
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('1', '2', '3')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def get_all_product(message):
    if message.text.lower() == 'проверить наличие':
        bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard2)


bot.polling()
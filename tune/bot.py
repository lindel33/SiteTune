import time
from pprint import pprint
import requests

import telebot
from data import (get_category, get_products,
                  get_detail_product, get_series,
                  get_current_product, get_all_products)

# TELEGRAM_URL = 'https://api.telegram.org/bot5239855839:AAGpK1VN7Lr2LDkq0WRC4onTLbYTWyrcc3g'
TOKEN = '5239855839:AAGpK1VN7Lr2LDkq0WRC4onTLbYTWyrcc3g'
URL_BITRIX = 'https://im.bitrix.info/imwebhook/eh/cde3fe41e972cc1f1501bbd0a6d330a11644378495/'
client = telebot.TeleBot(TOKEN)


def send_keyboard_category(message, current_category):
    text = message.text.split()[1]  # Получаем категорию без картинки
    category = [[x[0]] for x in get_series(text) if x[0] in current_category]
    if category == []:
        start_message(message,
                      text='В этой категори сейчас пусто😔\n'
                           'Актуальные новости у нас в канале!)')
        return 0
    category.append(['Назад'])
    print(1)
    keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_category.keyboard = category
    client.send_message(chat_id=message.chat.id,
                        text='Ищу: ' + message.text,
                        reply_markup=keyboard_category)


@client.message_handler(commands=['start'])
def start_message(message, text='Что хотите найти?'):
    category = get_category()
    categories = [[x[1]] for x in category]
    categories.insert(0, ['Купить новое устройство'])
    keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_category.keyboard = categories
    client.send_message(chat_id=message.chat.id,
                        text=text,
                        reply_markup=keyboard_category)


@client.message_handler(content_types=['text'])
def get_products_ctg(message):
    try:
        x = ['⌨️ Доп. устройства', '⌚️ Apple Watch',
             '💻 MacBook', '🎧 AirPods', '📲 iPad', '📱 iPhone']
        models = ['Доп. устройства', 'Apple Watch',
                  'MacBook', 'AirPods', 'iPad', 'iPhone']
        current_category = list(set([x[1] for x in get_current_product()]))

        category = []
        all_products = [x[0] for x in get_all_products()]

        if message.text.lower() == 'назад':
            start_message(message)
        elif message.text in x:

            send_keyboard_category(message, current_category)


        elif message.text in current_category \
                or message.text.split()[2] in models:
            text = message.text
            try:
                if message.text.split()[2] in models:
                    text = message.text.split()[2]
                    print('-----', text)
                    for icon in x:
                        if icon.split()[1] == text:
                            text = icon
            except:
                pass
            print('+++++', text)
            products = [[x[1]] for x in get_products(text)]
            products.append(['Назад к ' + text])
            keyboard_products = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard_products.keyboard = products
            client.send_message(chat_id=message.chat.id,
                                text='Ищу: ' + text,
                                reply_markup=keyboard_products)

        elif message.text in all_products:
            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard.keyboard = [['Забронировать\n' + message.text], ['Назад']]
            detail_product = get_detail_product(message.text)
            f1, f2, f3 = open(detail_product[1], 'rb'), open(detail_product[2], 'rb'), open(detail_product[3], 'rb')
            f1, f2, f3 = f1.read(), f2.read(), f3.read()
            client.send_media_group(chat_id=message.chat.id, media=[
                telebot.types.InputMediaPhoto(f1, caption=detail_product[6]),
                telebot.types.InputMediaPhoto(f2),
                telebot.types.InputMediaPhoto(f3), ])
            client.send_message(chat_id=message.chat.id,
                                text='Хотите забронировать эту модель?',
                                reply_markup=keyboard)

        else:
            try:
                jsn = message.__dict__.get('json')
                ts = {'update_id': 287246100,
                      'message': {'message_id': jsn['message_id'],
                                  'from': {'id': jsn['from']['id'],
                                           'is_bot': False,
                                           'first_name': jsn['from']['first_name'],
                                           'language_code': jsn['from']['language_code']},
                                  'chat': {'id': jsn['chat']['id'],
                                           'first_name': jsn['chat']['first_name'],
                                           'type': jsn['chat']['type']},
                                  'date': jsn['date'],
                                  'text': jsn['text']}}

                requests.post(URL_BITRIX, json=ts)
                if message.text.lower().split()[0] == 'забронировать' or \
                        message.text.lower() == 'купить новое устройство':
                    start_message(message, text='Ваш запрос получен 👍 \n'
                                                'Менеджер уже в пути 🐌')
            except Exception as _:
                jsn = message.__dict__.get('json')
                ts = {'update_id': 287246100,
                      'message': {'message_id': jsn['message_id'],
                                  'from': {'id': jsn['from']['id'],
                                           'is_bot': False,
                                           'first_name': jsn['from']['first_name'],
                                           'language_code': jsn['from']['language_code']},
                                  'chat': {'id': jsn['chat']['id'],
                                           'first_name': jsn['chat']['first_name'],
                                           'type': jsn['chat']['type']},
                                  'date': jsn['date'],
                                  'text': jsn['text']}}

                requests.post(URL_BITRIX, json=ts)
                start_message(message, text='Я вас не понимаю 🙄\n'
                                            'Напишите еще раз')
    except:
        start_message(message, text='Произошла ошибка Телеграмма😥\n'
                                    'Попробуйте написать через 5 минут\n'
                                    'Или напишите нашему менеджеру\n'
                                    '— Виктории @VasViktory ☝️👍')


while True:
    try:
        client.polling(none_stop=True)

    except Exception as e:
        client.delete_webhook()
        time.sleep(15)

import time
from pprint import pprint
import requests

import telebot
from data import (get_category, get_products,
                  get_detail_product, get_series,
                  get_current_product, get_all_products, get_not_category)

# TELEGRAM_URL = 'https://api.telegram.org/bot5239855839:AAGpK1VN7Lr2LDkq0WRC4onTLbYTWyrcc3g'
TOKEN = '5239855839:AAGpK1VN7Lr2LDkq0WRC4onTLbYTWyrcc3g'
URL_BITRIX = 'https://im.bitrix.info/imwebhook/eh/cde3fe41e972cc1f1501bbd0a6d330a11644378495/'
client = telebot.TeleBot(TOKEN)


def bitrix_client(message):
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


def send_keyboard_category(message, current_category):
    """
    Отправка клавиатуры моделей iPhone 11 / iPhone 12 / iPhone 13
    :param message:
    :param current_category:
    :return:
    """

    text = message.text.split()[1]  # Получаем категорию без картинки
    category = [[x[0]] for x in get_series(text) if x[0] in current_category]
    if category == []:
        start_message(message,
                      text='В этой категори сейчас пусто😔\n'
                           'Актуальные новости у нас в канале!)')
        return 0
    category.append(['Назад'])
    keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_category.keyboard = category
    client.send_message(chat_id=message.chat.id,
                        text='Ищу: ' + message.text,
                        reply_markup=keyboard_category)


def send_keyboard_product(message, text):
    """
    Отправка клавиатуры наличия моделей по выброной модели/ серии
    :param message:
    :param text:
    :return:
    """
    products = [x[1] for x in get_products(text)]
    products.sort()
    products = [[x] for x in products]
    if message.text.split()[1].lower() == 'watch':
        products.append(['Назад к Watch'])
    else:
        products.append(['Назад к ' + text.split()[0]])
    keyboard_products = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_products.keyboard = products
    client.send_message(chat_id=message.chat.id,
                        text='Ищу: ' + text,
                        reply_markup=keyboard_products)


def send_keyboard_pay(message):
    """
    Отправить сообщение
    :param message:
    :return:
    """
    name = message.text.split()
    name = name[0] + ' ' + name[1]
    products = [x[1] for x in get_products(name)]
    if message.text in products:
        products.remove(message.text)
    products.sort()
    products = [[x] for x in products]
    products.append(['Забронировать\n' + message.text])
    pprint(message.text)
    if message.text.split()[1].lower() == 'watch':
        products.append(['Назад к Watch'])
    elif message.text.split()[0] in get_not_category():
        pprint(message.text)
        products.append(['Назад к Доп. устройствам'])
    else:
        products.append(['Назад к ' + message.text.split()[0]])
        pprint(message.text.split()[0].lower())

    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.keyboard = products
    detail_product = get_detail_product(message.text)
    f1, f2, f3 = open('media/' + detail_product[1], 'rb'), \
                 open('media/' + detail_product[2], 'rb'), \
                 open('media/' + detail_product[3], 'rb')
    f1, f2, f3 = f1.read(), f2.read(), f3.read()

    client.send_media_group(chat_id=message.chat.id, media=[
        telebot.types.InputMediaPhoto(f1, caption=detail_product[6]),
        telebot.types.InputMediaPhoto(f2),
        telebot.types.InputMediaPhoto(f3), ])
    client.send_message(chat_id=message.chat.id,
                        text='Хотите забронировать эту модель?',
                        reply_markup=keyboard)


@client.message_handler(commands=['start'])
def start_message(message, text='Что хотите найти?'):
    category = get_category()
    categories = [[x[1]] for x in category]
    categories.insert(0, ['Мой бюджет'])
    categories.insert(1, ['Купить новое устройство'])

    keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_category.keyboard = categories
    client.send_message(chat_id=message.chat.id,
                        text=text,
                        reply_markup=keyboard_category)


@client.message_handler(func=lambda message: message.text == 'Мой бюджет')
def filter_price(message):
    pprint('Бюджет')
    keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_category.keyboard = [
        ['Бюджет на iPhone'],
        ['Бюджет на iPad'],
        ['Бюджет на MacBook'],
        ['Бюджет на AirPods'],
        ['Бюджет на Watch'],
        ['Бюджет на Доп. устройства'],

    ]
    client.send_message(chat_id=message.chat.id,
                        text='Что посмотрим?',
                        reply_markup=keyboard_category)


@client.message_handler(func=lambda message: message.text.split()[0] == 'Бюджет')
def filter_price(message):

    keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_category.keyboard = [['']]
    # [
    #     ['До 10_000 на ' + message.text.split()[2]],
    #     ['До 20_000 на ' + message.text.split()[2]],
    #     ['До 40_000 на ' + message.text.split()[2]],
    #     ['До 60_000 на ' + message.text.split()[2]],
    #     ['От 60_000 на ' + message.text.split()[2]],
    #
    # ]
    client.send_message(chat_id=message.chat.id,
                        text='ЭЭЭЭЭ ТЫ че в бюджет зашел?\nПиши /start чтобы начать опять',
                        reply_markup=keyboard_category)


@client.message_handler(func=lambda message: message.text.split()[0] == 'До ')
def filter_price(message):
    keyboard_category = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_category.keyboard = [
        [''],

    ]
    client.send_message(chat_id=message.chat.id,
                        text='Вот что есть:',
                        reply_markup=keyboard_category)


@client.message_handler(content_types=['text'])
def get_products_ctg(message):
    pprint(message.text)
    try:

        menu = ['Мой бюджет', '📱 iPhone', '📲 iPad', '💻 MacBook',
                '🎧 AirPods', '⌚️ Watch',
                '⌨️ Доп. устройства']

        current_category = list(set([x[1] for x in get_current_product()]))

        category = []
        all_products = [x[0] for x in get_all_products()]
        tmp_text = []

        if len(message.text.split()) > 2:
            tmp_text = [x for x in menu if x.split()[1] == message.text.split()[2]]

        if message.text.lower() == 'назад':
            start_message(message)

        if message.text in menu:
            send_keyboard_category(message, current_category)

        elif len(tmp_text) != 0 and tmp_text[0] in menu:
            if tmp_text[0] in menu:
                message.text = tmp_text[0]
                send_keyboard_category(message, current_category)

        if message.text in current_category:
            text = message.text
            send_keyboard_product(message, text)

        elif message.text in all_products:
            send_keyboard_pay(message)

        else:
            if message.text not in menu:
                if message.text.lower() != 'назад':
                    bitrix_client(message)
    except:
        start_message(message, text='Произошла ошибка Телеграмма😥\n'
                                    'Попробуйте написать через 5 минут\n'
                                    'Или напишите нашему менеджеру\n'
                                    '— Виктории @VasViktory ☝️👍')


while True:
    try:
        client.polling(none_stop=True)

    except Exception as e:
        # client.delete_webhook()
        time.sleep(1)

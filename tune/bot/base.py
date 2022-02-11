import telebot

from tune.bot.bot import start_message
from tune.bot.data import get_series, get_products, get_detail_product

TOKEN = '5239855839:AAGpK1VN7Lr2LDkq0WRC4onTLbYTWyrcc3g'
URL_BITRIX = 'https://im.bitrix.info/imwebhook/eh/cde3fe41e972cc1f1501bbd0a6d330a11644378495/'
client = telebot.TeleBot(TOKEN)

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

    if message.text.split()[1].lower() == 'watch':
        products.append(['Назад к Watch'])
    else:
        products.append(['Назад к ' + message.text.split()[0]])

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


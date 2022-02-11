import requests

from tune.bot.bot import start_message

TOKEN = '5239855839:AAGpK1VN7Lr2LDkq0WRC4onTLbYTWyrcc3g'
URL_BITRIX = 'https://im.bitrix.info/imwebhook/eh/cde3fe41e972cc1f1501bbd0a6d330a11644378495/'


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

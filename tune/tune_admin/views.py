import json
import os

import requests
# from django.http import JsonResponse
from django.http import JsonResponse
from django.views import View

TELEGRAM_URL = 'https://api.telegram.org/bot5292093759:AAESSHDmWbSDQHBMZepHbtVDrzFHGD-IfhM'
TUTORIAL_BOT_TOKEN = '5292093759:AAESSHDmWbSDQHBMZepHbtVDrzFHGD-IfhM'
URL_BITRIX = 'https://im.bitrix.info/imwebhook/eh/1e5c42e147576675852ed3db477de7f71644288985/'


class TutorialBotView(View):
    def get(self, request, *args, **kwargs):
        json_client = {'update_id': 287246100, 'message': {'message_id': 2145, 'from': {'id': 572982939, 'is_bot': False, 'first_name': 'Sergey', 'language_code': 'en'}, 'chat': {'id': 572982939, 'first_name': 'Sergey', 'type': 'private'}, 'date': 1644330637, 'text': 'sddsds'}}
        requests.post(url=URL_BITRIX, json=json_client)

    @staticmethod
    def send_message(message, chat_id):
        pass
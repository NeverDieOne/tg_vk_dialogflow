from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from dotenv import load_dotenv
import requests


def start(bot, update):
    update.message.reply_text('Здравствуйте')


def dialog_reply(bot, update):
    # TODO добавить проверку на ошибки запроса
    base_url = 'https://api.dialogflow.com/v1/query'
    params = {
        'v': '20150910',
        'query': update.message.text,
        'lang': 'ru',
        'sessionId': update.message.chat_id
    }
    headers = {
        'Authorization': f'Bearer {os.getenv("DF_TOKEN")}'
    }
    response = requests.get(base_url, headers=headers, params=params)
    reply = response.json()['result']['fulfillment']['speech']
    update.message.reply_text(reply)


if __name__ == '__main__':
    load_dotenv()

    updater = Updater(os.getenv('TG_TOKEN'))
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, dialog_reply))

    updater.start_polling()


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from dotenv import load_dotenv
import requests
import my_logging



def start(bot, update):
    update.message.reply_text('Здравствуйте')


def dialog_reply(bot, update):
    base_url = 'https://api.dialogflow.com/v1/query'
    params = {
        'v': '20150910',
        'query': update.message.text,
        'lang': 'ru',
        'sessionId': update.message.chat_id
    }
    headers = {
        'Authorization': f'Bearer {os.environ["DF_TOKEN"]}'
    }
    response = requests.get(base_url, headers=headers, params=params)
    response.raise_for_status()

    reply = response.json()['result']['fulfillment']['speech']
    update.message.reply_text(reply)


if __name__ == '__main__':
    load_dotenv()

    logger = my_logging.logging.getLogger('TG Logger')

    updater = Updater(os.environ['TG_TOKEN'])
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, dialog_reply))

    try:
        updater.start_polling()
    except requests.exceptions.HTTPError as err:
        logger.warning(f'TG Bot\nЧто-то пошло не так!\n{err}')

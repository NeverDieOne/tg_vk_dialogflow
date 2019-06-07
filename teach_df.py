import json
import requests
import os
from dotenv import load_dotenv
import argparse
import logging


def teach_dialogflow(file):
    with open(file, 'r') as _file:
        qa = json.load(_file)

    url = 'https://api.dialogflow.com/v1/intents'
    headers = {
        'Authorization': f'Bearer {os.getenv("DF_TOKEN")}',
        'Content-Type': 'application/json'
    }

    for topic, data in qa.items():
        data = {
            'lang': 'ru',
            'v': '20150910',
            'auto': True,
            'contexts': [],
            'name': topic,
            'responses': [
                {
                    'messages': [
                        {
                            'speech': data['answer'],
                            'type': 0
                        }
                    ]
                }
            ],
            'userSays': [{'data': [{'text': info}]} for info in data['questions']]
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()


if __name__ == '__main__':
    load_dotenv()

    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger('Teach Logger')

    parser = argparse.ArgumentParser(description='Обучение DialogFlow')
    parser.add_argument('json', help='Файл с данными')
    args = parser.parse_args()

    try:
        teach_dialogflow(args.json)
    except requests.exceptions.HTTPError as err:
        logger.warning(f'Что-то пошло не так!\n{err}')

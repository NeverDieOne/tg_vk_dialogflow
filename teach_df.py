import json
import requests
import os
from dotenv import load_dotenv

# TODO add argparse


def teach_dialogflow(file):
    with open(file, 'r') as _file:
        questions = json.load(_file)

    url = 'https://api.dialogflow.com/v1/intents'
    headers = {
        'Authorization': f'Bearer {os.getenv("DF_TOKEN")}',
        'Content-Type': 'application/json'
    }

    for topic, data in questions.items():
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
        requests.post(url, headers=headers, json=data)


if __name__ == '__main__':
    load_dotenv()

    teach_dialogflow('questions.json')

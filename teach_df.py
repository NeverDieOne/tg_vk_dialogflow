import json
import requests
import os


def teach_dialogflow(file):
    with open(file, 'r') as questions_file:
        questions = json.load(questions_file)

    url = 'https://api.dialogflow.com/v1/intents'
    headers = {
        'Authorization': f'Bearer {os.getenv("DF_TOKEN")}',
        'Content-Type': 'application/json'
    }
    data = {
        'lang': 'ru',
        'v': '20150910',
        'auto': True,
        'contexts': [],
        'name': 'Устройство на работу',
        'responses': [
            {
                'messages': [
                    {
                        'speech': questions['Устройство на работу']['answer'],
                        'type': 0
                    }
                ]
            }
        ],
        'userSays': [{'data': [{'text': info}]} for info in questions['Устройство на работу']['questions']]
    }
    requests.post(url, headers=headers, json=data)


if __name__ == '__main__':
    teach_dialogflow('questions.json')

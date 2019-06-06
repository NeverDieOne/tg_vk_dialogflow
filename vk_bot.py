import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os
from dotenv import load_dotenv
import random
import requests
import my_logging
import logging


def echo(event, vk_api):
    base_url = 'https://api.dialogflow.com/v1/query'
    params = {
        'v': '20150910',
        'query': event.text,
        'lang': 'ru',
        'sessionId': event.user_id
    }
    headers = {
        'Authorization': f'Bearer {os.environ["DF_TOKEN"]}'
    }
    response = requests.get(base_url, headers=headers, params=params)
    response.raise_for_status()

    reply = response.json()['result']['fulfillment']['speech']
    if response.json()['result']['metadata']['isFallbackIntent'] == 'true':
        pass
    else:
        vk_api.messages.send(
            user_id=event.user_id,
            message=reply,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    load_dotenv()

    logger = logging.getLogger('VK Logger')
    logger.warning('It starts')

    vk_session = vk_api.VkApi(token=os.environ['VK_TOKEN'])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            try:
                echo(event, vk_api)
            except requests.exceptions.HTTPError as err:
                logger.warning(f'VK Bot\nЧто-то пошло не так!\n{err}')

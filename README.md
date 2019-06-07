# Бот-помощник для ответа на звонки службы поддержки

Бот для ответов на частозадаваемые вопросы.

## Как установить

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей.
`pip install -r requirements.txt`

Параметры `TG_TOKEN`, `DF_TOKEN`, `VK_TOKEN` и `CHAT_ID` должны находится в файле `.env` рядом со скриптом.
`CHAT_ID` можно узнать у специального бота `@userinfobot`.

Бот обучаемый и можно ему "скормить" ещё вопросов и ответов.
Пример обучения:
`python teach_df.py question.json`.

[Гайд по развертыванию ботов на платформе Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)

## Пример запуска на локальной машине

Перед запуском на локальной машине убедитесь, что у Вас работает VPN (могут быть проблемы с запуском Telegram Bot)

1. Копируем к себе данный репозиторий:
`git clone https://github.com/NeverDieOne/tg_vk_dialogflow.git`.
2. Устанавливаем все зависимости: 
`pip install -r requirements.txt`
3. Создаем файл `.env` и помещаем в него `TG_TOKEN`, `DF_TOKEN`, `VK_TOKEN` и `CHAT_ID`:
    * `TG_TOKEN` можно узнать у специального бота `@botfather`.
    * `DF_TOKEN` можно узнать в настройках своего аккаунта DialogFlow.
    * `VK_TOKEN` можно узнать в настройках группы ВК.
    * `CHAT_ID` можно узнать у специального бота `@userinfobot`.
4. С помощью команд `python tg_bot.py` и `python vk_bot.py` запускаем ботов.

## Пример использования ботов

![Sample](https://media.giphy.com/media/VfKyIZFXfcUFkX4jYJ/giphy.gif)

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Dvmn.org](https://dvmn.org/modules/)
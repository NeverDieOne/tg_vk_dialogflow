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

## Пример использования ботов

![Sample](https://media.giphy.com/media/VfKyIZFXfcUFkX4jYJ/giphy.gif)

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Dvmn.org](https://dvmn.org/modules/)
import logging
from dotenv import load_dotenv
import os
import telegram

load_dotenv()


class MyLogsHandler(logging.Handler):

    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(chat_id=os.environ['CHAT_ID'],
                              text=log_entry)


bot = telegram.Bot(token=os.environ['TG_TOKEN'])

logger = logging.getLogger('Logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(MyLogsHandler(bot))

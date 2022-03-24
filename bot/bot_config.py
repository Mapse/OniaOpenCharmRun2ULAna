# !pip install python-telegram-bot
import telegram
from telegram.ext import *


def bot_message(message):

    token = '5179895518:AAED9UEdn77LHaMXX7rmYeAcRcGzSYcnFPc'
    bot = telegram.Bot(token=token)

    # Check the bot credentials
    print(f"Bot informations: {bot.get_me()}" )

    # How to get chat id
    # https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
    chat_id = 1075324946

    bot.send_message(chat_id=chat_id, text=message)






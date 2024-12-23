import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from datetime import datetime, timezone
import pytz
import telebot

from telebot.types import *

from webdav import append_to_file

load_dotenv()

TOKEN = getenv('TG_BOT_TOKEN')



bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(func=lambda message: True)
def echo_all(message:Message):
    bot.reply_to(message, message.text)    
    if message.from_user.id != 468174277:
        pass
    # Преобразуем Unix-время в datetime с указанием временной зоны UTC
    sent_time_utc = datetime.fromtimestamp(message.date, tz=timezone.utc)

    # Конвертируем время в часовой пояс Europe/Moscow
    local_timezone = pytz.timezone("Europe/Moscow")
    sent_time_local = sent_time_utc.astimezone(local_timezone)

    # Сохраняем данные в файл
    append_to_file(sent_time_local, message.text)



if __name__ == "__main__":
    bot.infinity_polling()
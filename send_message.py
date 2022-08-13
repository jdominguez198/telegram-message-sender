from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from random import randint
from time import sleep
from os import getenv

if __name__ == '__main__':
    API_ID = getenv('TELEGRAM_API_ID')
    API_HASH = getenv('TELEGRAM_API_HASH')
    API_SESSION = getenv('TELEGRAM_API_SESSION')
    TELEGRAM_USER_TO = getenv('TELEGRAM_USER_TO')
    TELEGRAM_MESSAGE = getenv('TELEGRAM_MESSAGE')
    SLEEP_RANDOM_SECONDS_BEFORE_MESSAGE = getenv('SLEEP_RANDOM_SECONDS_BEFORE_MESSAGE', 1)
    with TelegramClient(StringSession(API_SESSION), API_ID, API_HASH) as client:
        if int(SLEEP_RANDOM_SECONDS_BEFORE_MESSAGE) > 0:
            sleep(randint(1, int(SLEEP_RANDOM_SECONDS_BEFORE_MESSAGE)))
        client.send_message(TELEGRAM_USER_TO, TELEGRAM_MESSAGE)
        print(f"Message '{TELEGRAM_MESSAGE}' was sent to '{TELEGRAM_USER_TO}' successfully!")

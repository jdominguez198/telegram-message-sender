from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from os import getenv

if __name__ == '__main__':
    API_ID = getenv('TELEGRAM_API_ID')
    API_HASH = getenv('TELEGRAM_API_HASH')
    with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        print(f"Your session string is: '{client.session.save()}'")
        print("")
        print("Keep it safe! Anyone with this session string could use Telegram as you")

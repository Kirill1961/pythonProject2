"""
* Извлечение из источника текстовых файлов с поиском по ключевым словам

connect() подключиться
        │
        ▼
extract_messages() получить сообщения
        │
        ▼
parse_message() сделать MessageMetadata
        │
        ▼
save_message() записать в DuckDB
        │
        ▼
"""

import asyncio
import re

from dataclasses import dataclass
from datetime import datetime

import duckdb

from telethon import TelegramClient
from telethon.tl.types import (
    Message,
    MessageMediaDocument,
    DocumentAttributeFilename,
)
from dotenv import load_dotenv
import os


@dataclass
class MessageMetadata:
    vacancy_name: str
    rate: str
    location: str
    channel_name: str
    resume_link: str
    message_date: datetime





load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

CHANNELS = {
    "Мой канал": "@Kirill_50plus_DS",
    "Тёмная Башня": "@tbaudiobook",
    "Работа и вакансии в IT": "@proglib_jobs"
}

SESSION_NAME = "vacancy_parser"

client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH,
)


PREFIX = [
    'python',
    'vacancy',
    'job',
    'ваканс',
    'удалён',
    'удален',
    'remote',
    'datanalyst',
    'analys',
    'datas',
    'scientist',
    'стажё',
    'стаже',
    'jun',
    'intern',
    'аналит'
]

# mb = {'CHANNEL_NAME': [ "jun", "intern", "стаже", "стажё"],
#  'LOCATION': [ 'удалён', 'remote'],
#  'MESSAGE_DATE':  message.datetime,
#  'RATE':  ["jun", "intern", "стаже", "стажё"],
#  'RESUME_LINK': CHANNELS.value(),
#  'VACANCY_NAME': CHANNELS.key()}

RATE = ["jun", "intern", "стаже", "стажё"]
VACANCY_NAME = ["datanalyst", "analys", "datas", "scientist", "аналит"]
LOCATION = ['удалён', 'remote']
MESSAGE_DATE = str()
RESUME_LINK = str()
CHANNEL_NAME = str()

async def extract_messages(chanel):
    async for msg in client.iter_messages(chanel, limit=3, reverse=False):
        # print(msg)
        yield msg


async def main():
    await client.start()

    me = await client.get_me()

    print(f"Подключение успешно.")
    print(f"Имя: {me.first_name}")
    print(f"ID: {me.id}")

    # async for message in extract_messages(CHANNELS):
    #     print(message.id)
    n = 0
    for name, link in CHANNELS.items():
        print(f"{name} : {link}")

        # Вызов генератора
        async for message in extract_messages(link):
            n += 1

            if isinstance(message.text, str):
                # print(message)
                texts = message.text.lower().split()

                for word_text in texts:
                    word_list = re.findall(r"\w+", word_text)

                    for word in word_list:

                        for pref in PREFIX:

                            if word.startswith(pref):

                                # print(n, pref, word)

                                w = word if pref in RATE else ""
                                # vc = word if pref in VACANCY_NAME else ""

                                print(n, w)
            else:
                print(" No messages")
                        # if w.startswith(word) == True:

                            # print(n, word, message.id, w)
            # print((re.findall(r"\D+", channel.text)))

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

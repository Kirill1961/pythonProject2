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
    grade: str
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

#  Префиксы общие
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

#  Префиксы по группам
metadata = {
    # 'VACANCY_NAME': ["datanalyst", "analys", "datas", "scientist", "аналит"],
     'GRADE':  ["jun", "intern", "стаже", "стажё"]
    , 'LOCATION': ['удалён', 'remote']
    # , 'CHANNEL_NAME': []
    # , 'MESSAGE_DATE':  []
    # , 'RESUME_LINK': []

      }

# GRADE = ["jun", "intern", "стаже", "стажё"]
# VACANCY_NAME = ["datanalyst", "analys", "datas", "scientist", "аналит"]
# LOCATION = ['удалён', 'remote']
# MESSAGE_DATE = str()
# RESUME_LINK = str()
# CHANNEL_NAME = str()

# TODO Ответ от источника надо ждать поэтому async
async def extract_messages(chanel):
    async for msg in client.iter_messages(chanel, limit=3, reverse=False):
        # print(msg)
        yield msg

# TODO Ответ ждать не надо поэтому не async
def comparison(num_msg, word):
    # for pref in PREFIX:
    for name_mdata, pref_total in metadata.items():
        for pref in pref_total:

            if word.startswith(pref):
                value_metadata = word
                print(num_msg, name_mdata, pref, value_metadata)


async def main():
    await client.start()

    me = await client.get_me()

    print(f"Подключение успешно.")
    print(f"Имя: {me.first_name}")
    print(f"ID: {me.id}")

    # async for message in extract_messages(CHANNELS):
    #     print(message.id)
    num_msg = 0
    for name, link in CHANNELS.items():
        print(f"{name} : {link}")

        # Вызов генератора
        async for message in extract_messages(link):
            num_msg += 1

            if isinstance(message.text, str):
                # print(message)
                texts = message.text.lower().split()

                for word_text in texts:
                    word_list = re.findall(r"\w+", word_text)

                    for words in word_list:
                        comparison(num_msg, words)




            else:
                print(" No messages")
                        # if w.startswith(word) == True:

                            # print(n, word, message.id, w)
            # print((re.findall(r"\D+", channel.text)))

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

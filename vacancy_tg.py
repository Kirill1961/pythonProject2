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
    channel_name: str
    message_date: datetime
    vacancy_name: str
    resume_link: str


load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

CHANNELS = {
    "Kirill": "@Kirill_50plus_DS",
    "Old Tower": "@tbaudiobook"
}

SESSION_NAME = "vacancy_parser"

client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH,
)

WORDS = [
'#python',
 '#vacancy',
 '#job',
 '#вакансия',
 '#удалённая',
 'работа',
 '#remote',
 '#DataAnalyst',
 '#DataScience',
 '#удалёнка',
 '#работа',
 '#удалённо',
 '#стажёр',
 'стажёр',
 '#junior',
 'junior'
]
async def extract_messages(chanel):
    async for msg in client.iter_messages(chanel, limit=10, reverse=False):
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
    for name, link in CHANNELS.items():
        print(name)
        # Вызов генератора
        async for message in extract_messages(link):
            if isinstance(message.text, str):
                texts = message.text.lower()
                word = [w for w in texts.split(" ")]
                print(word)
            # print((re.findall(r"\D+", channel.text)))

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

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


@dataclass
class MessageMetadata:
    channel_name: str
    message_date: datetime
    vacancy_name: str
    resume_link: str


API_ID = 32818677
API_HASH = "e77003c295d40288e495464e52d7d41e"

SESSION_NAME = "vacancy_parser"

client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH,
)

async def main():

    await client.start()

    me = await client.get_me()

    print(f"Подключение успешно.")
    print(f"Имя: {me.first_name}")
    print(f"ID: {me.id}")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
"""
client — это клиент, через которого мы общаемся с Telegram.
message — это конкретное сообщение, которое мы получили от Telegram.
Библиотеки для приложений Telethon, duckdb, boto3, loguru, pydantic, prefect, python-dotenv
Архитектура Моя :
Telegram канал
       │
       ▼
client.iter_messages(...)
       │
       ▼
Message
       │
       ▼
extract_metadata()
       │
       ▼
yield ChapterMetadata(...)
       │
       ▼
process_chapter_batch_task(...)
       │
       ▼
DuckDB
===========================================
Архитектура Урока:
                 main.py
                    │
      ┌─────────────┼──────────────┐
      │             │              │
      ▼             ▼              ▼
 config.py     extractor.py    database.py
      │             │              │
      │             │              │
      ▼             ▼              ▼
  setting    ChapterMetadata   init_database()
                    │
                    ▼
             extract_metadata()
                    │
                    ▼
              storage.py
                    │
                    ▼
             get_storage()
======================================
            Блок Схема::
            Extract
            ──────────────
            extractor.py
            Telethon
            iter_messages()

            ↓

            Transform
            ──────────────
            ChapterMetadata

            ↓

            Load
            ──────────────
            storage.py

            ↓

            database.py
            DuckDB
"""

from typing import AsyncGenerator
import telethon.tl.types
from telethon import TelegramClient
from telethon.tl.types import (MessageMediaDocument,
                               MessageMediaPhoto,
                               DocumentAttributeAudio,
                                DocumentAttributeFilename
                               )
import asyncio
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

# CHANNEL = "t.me/Kirill_50plus_DS"
CHANNEL = "https://t.me/tbaudiobook"

# Создали клиента
client = TelegramClient(
    "telegram_session",
    API_ID,
    API_HASH
)

# async def main():
#
#     await client.start()
#
#     print("Подключение к Telegram успешно!")
#
#     async for message in client.iter_messages(
#         CHANNEL,
#         limit=4000
#     ):
#
#         print(
#             message.id,
#             message.date,
#             message.text,
#             message.file
#         )
#         if message.file:
#             print(
#                 "НАЙДЕН ФАЙЛ:",
#                 message.file.name,
#                 message.file.size
#             )
#
#     # await main()
# asyncio.run(main())




@dataclass
class ChapterMetadata:
    book_name: str
    chapter_number: int
    file_extension: str
    message_id: int

async def extract_metadata(max_book: int=0) -> AsyncGenerator[ChapterMetadata, None]:
    """
    Вытаскиваем файлы из источника
    """
    await client.start()  # Подключились к Telegram

    print("Подключение к Telegram успешно!")

    def sanitize_book_name(text):
        """
        Проверка Имени книги, если text - фото, то это обложка
        """
        text = "Темная башня"
        return text

    current_book = 'Неизвестная книга'
    chapter_num = 0
    books_with_chapters = 0

    async for msg in client.iter_messages(  # Получаем сообщения
        CHANNEL,
        reverse=True,
        limit=10
    ):
        # Проверка объектов message и photo - если фото значит обложка.
        is_cover = msg.message and msg.photo
        if is_cover:
            #  Если current_book - обложка, то № главы = 0
            current_book = sanitize_book_name(msg.message)
            chapter_num = 0

            # Вытаскиваем атрибуты проверяем на mp3
        if msg.media and isinstance(msg.media, MessageMediaDocument):
            is_audio = any(isinstance(attr, DocumentAttributeAudio) for attr in msg.media.document.attributes)

            if is_audio:
                for attr in msg.media.document.attributes:
                    if isinstance(attr, DocumentAttributeFilename):
                        ext = attr.file_name.split('.')[-1].lower()  # Расширение
                        break
                chapter_num += 1
                yield ChapterMetadata(
                    book_name=current_book,
                    chapter_number=chapter_num,
                    file_extension=ext,
                    message_id=msg.id
                )

        # print(
        #     "ID:", message.id,
        #     "| Дата:", message.date,
        #     "| Текст:", message.text,
        #     "| Файл:", message.file
        # )
# TODO Вывод Типов
        # print("=" * 10)
        #
        # # сам объект Message
        # print("Тип msg:", type(msg))
        #
        # # ID сообщения
        # print("ID:", msg.id)
        #
        # # дата
        # print("Дата:", msg.date)
        #
        # # 1. Текст сообщения
        # if msg.message:
        #     print("Текст:", msg.message)

        # TODO 2. Проверяем media
        if msg.media:
            ...
            # print("Тип media:", type(msg.media))

            # Документ (файл)
            if isinstance(msg.media, MessageMediaDocument):
                ...
                # print("Это документ!")
                #
                # print("Имя файла:", msg.file.name)
                #
                # print("Размер:", msg.file.size)


            # Фото
            elif isinstance(msg.media, MessageMediaPhoto):
                ...
                # print("Это фотография!")


        else:
            ...
            # print("Вложения нет")

# maun - Отвечает за оркестрацию
async def main():

    async for chapter in extract_metadata(10):
        ...
        # print(chapter)

if __name__ == "__main__":
    asyncio.run(main())
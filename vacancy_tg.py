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

import duckdb

from telethon import TelegramClient
from telethon.tl.types import (
    Message,
    MessageMediaDocument,
    DocumentAttributeFilename,
)
from dotenv import load_dotenv
import os
from pydantic import BaseModel, ConfigDict
from collections import defaultdict

from datetime import date, datetime, timedelta


# @dataclass
class MessageMetadata(BaseModel):
    model_config = ConfigDict(frozen=True)
    """Модель для таблицы метаданных."""
    # model_config = ConfigDict(frozen=True)
    message_date: str
    grade: str
    id: int
    # vacancy_name: str
    # location: str
    # channel_name: str
    # resume_link: str

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
pref_metadata = {
    'VACANCY_NAME': ["datanalyst", "analys", "datas", "scientist", "data scientist", "аналит", "разраб"],
    'GRADE': ["jun", "intern", "стаже", "стажё", "middle"]
    , 'LOCATION': ['удалён', 'remote', 'удален']
    # , 'CHANNEL_NAME': []
    , 'MESSAGE_DATE': []
    , "ID": []
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



def metadata_messages(id, mtd_dict):

    print(id, mtd_dict)

    metadata = MessageMetadata(
        message_date=mtd_dict.get("MESSAGE_DATE"),
        grade=mtd_dict.get("GRADE"),
        id=id
    )

    # print("METADATA:", metadata)

    return id, metadata

# d = defaultdict(set)

# TODO создаём словарь словарей, для этого defaultdict(set) оборачиваем в функцию
#  lambda не вызывается скобками а просто обращается к ячейке,
# d = defaultdict(lambda: defaultdict(set))

d = {}  # Словарь для заполнения метадатой

# TODO Ответ ждать не надо поэтому не async
def comparison(msg_id, word, meta_date):
    """
    * msg_id - нужен для группировки метадаты
    """
    for name_mdata, pref_total in pref_metadata.items():

        for pref in pref_total:

            # if name_mdata in ['CHANNEL_NAME', 'MESSAGE_DATE', 'RESUME_LINK']:

            if word.startswith(pref):
                value_metadata = word

                # d[msg_id][name_mdata].add(value_metadata)  # msg_id нужен для группировки метадаты

                d.setdefault(msg_id, {}).setdefault('MESSAGE_DATE', meta_date.date().strftime("%Y-%m-%d"))

                d[msg_id].update({name_mdata: value_metadata})

                if d[msg_id].get("GRADE"):
                    # print(d[msg_id])
                    # metadt = metadata_messages(d, msg_id)

                    return d[msg_id]


async def main():
    await client.start()

    me = await client.get_me()

    print(f"Подключение успешно.")
    print(f"Имя: {me.first_name}")
    print(f"ID: {me.id}")

    num_msg = 0
    dict_mdata = {}  # Словарь Для последней строки
    metadata_list = []
    for name, link in CHANNELS.items():
        print(f"{name} : {link}")

        # Вызов генератора
        async for message in extract_messages(link):
            num_msg += 1
            # print(message)

            if isinstance(message.text, str):
                # print(message.date.date())
                texts = message.text.lower().split()

                # Сохраняем две даты для вывода в строчном формате и для метадаты для в питоновском datetime.datetime
                # date_temporary = message.date.date().strftime('%Y-%m-%d')

                date_metadata = message.date
                for word_text in texts:
                    word_list = re.findall(r"\w+", word_text)

                    for words in word_list:

                        compar = comparison(message.id, words, date_metadata)

                        if compar:
                            # dict_mdata[message.id] = compar
                            #
                            # print(dict_mdata[message.id])
                            # print(compar)


                            metadt = metadata_messages(message.id, compar)

                            # if metadt:

                            metadata_list.append(metadt)




            else:
                print(" No messages")

    print(metadata_list)

    await client.disconnect()
    return dict_mdata


if __name__ == "__main__":
    print(asyncio.run(main()))

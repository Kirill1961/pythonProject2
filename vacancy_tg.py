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

Архитектура проекта:

project/
├── src/
├── data/
│   └── metadata.duckdb
├── .env
└── ...

src - организационная папка для исходного кода проекта.
│
├── config      → настройки
├── extractor   → получить данные
├── processor   → обработать
├── storage     → сохранить
├── database    → работать с БД
└── pipeline    → запустить весь процесс

"""

import asyncio
import re

import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

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

from pathlib import Path

from prefect import flow, task

__doc__ = """
@task          @task
  ↓              ↓
extract       save
     \          /
      \        /
       @flow
      pipeline
"""

DB_PATH = Path("data/metadata.duckdb")

# TODO exist_ok=True - если директория уже существует, то новая не создаётся
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def init_database():
    """
    Если будет ошибка, то finally гарантирует закрытие соединения в любом случае.
    id INTEGER PRIMARY KEY - вариант для контроля дубликатов id сообщений
    """

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = duckdb.connect(str(DB_PATH))

    # TODO Однократное удаление БД
    # conn.execute("""
    # DROP TABLE metadata;
    # """)

    try:
        conn.execute("""
                    CREATE TABLE IF NOT EXISTS metadata (
                        id INTEGER,
                        message_date DATE,
                        grade VARCHAR,
                        vacancy_name VARCHAR,
                        location VARCHAR,
                        channel_name VARCHAR,
                        channel_link VARCHAR,
                        PRIMARY KEY (channel_link, id)
                    )
                """)

        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_metadata_id
            ON metadata(id)
        """)



    finally:
        conn.close()


# TODO Порядок расстановки в классе определит порядок в выводе
# @dataclass
class MessageMetadata(BaseModel):
    """ Модель для таблицы метаданных.
        str | None = None   ---  это говорит что значение может быть строкой или None
    """
    model_config = ConfigDict(frozen=True)

    id: int
    message_date: str | None = None
    grade: str | None = None
    vacancy_name: str | None = None
    location: str | None = None
    channel_name: str | None = None
    channel_link: str | None = None


load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

CHANNELS = {
    # "Мой канал": "@Kirill_50plus_DS",
    # "Тёмная Башня": "@tbaudiobook",
    "Работа и вакансии в IT": "@proglib_jobs",
    "Доска AI-объявлений": "@DS_avitotech",
    "Вакансии ИТ": "@prog_itjobs",
    "Machine Learning Jobs": "@Machinelearning_Jobs",
    "Data Science Jobs": "@datascienceml_jobs",
    "ML & Data Science Jobs": "https://t.me/+dJGMlUsazwU4NGRi",
    "Data jobs": "@datajob",
    "ML / DS_Jobs": "@ml_data_science_job",
    "Data Analyst/Science Jobs": "@data_analyst_science_jobs",
    "Data science: Remote job of the day": "@data_science_remote_jobs",
    "Data Science jobs": "https://t.me/datascience_job",
    "getmatch": "https://t.me/g_jobbot",
    "Python Django Jobs": "@python_django_work",
    "Python Jobs": "@python_djangojobs",
    "Ит Вакансии ": "@hr_itwork",
    "fFinder1": "@theyseeku",
    "fFinder2": "@finder",
    "fFinder3": "@finderwork"

}

SESSION_NAME = "vacancy_parser"

client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH,
)

#  Префиксы по группам
pref_metadata = {
    'VACANCY_NAME': ["datanalyst", "analys", "datas", "scientist", "data scientist", "аналит", "разраб"],
    'GRADE': [
        "jun",
        "intern",
        "стаже",
        "стажё",
        # "middle",
        "стажир"
    ]
    , 'LOCATION': [
        "удалён",
        "remote",
        "удален"
    ]
    , 'CHANNEL_NAME': []
    , 'MESSAGE_DATE': []
    , "ID": []

}

# @task
# TODO Ответ от источника надо ждать поэтому async
async def extract_messages(chanel):
    async for msg in client.iter_messages(chanel, limit=100, reverse=False):
        # print(msg)
        yield msg

# @task
def metadata_messages(id, compar, chanel_name, chanel_link):
    # print(compar.get("VACANCY_NAME"))

    metadata = MessageMetadata(
        id=id
        , message_date=compar.get("MESSAGE_DATE")
        , grade=compar.get("GRADE")
        , vacancy_name=compar.get("VACANCY_NAME")
        , location=compar.get("LOCATION")
        , channel_name=chanel_name
        , channel_link=chanel_link
    )

    # print("METADATA:", metadata)

    return metadata


# d = defaultdict(set)

# TODO создаём словарь словарей, для этого defaultdict(set) оборачиваем в функцию
#  lambda не вызывается скобками а просто обращается к ячейке,
# d = defaultdict(lambda: defaultdict(set))

dict_metadata = {}  # Словарь для заполнения метадатой


# TODO Ответ ждать не надо поэтому не async
# @task
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

                dict_metadata.setdefault(msg_id, {}).setdefault('MESSAGE_DATE', meta_date.date().strftime("%Y-%m-%d"))

                dict_metadata[msg_id].update({name_mdata: value_metadata})

                if dict_metadata[msg_id].get("GRADE"):
                    # print(d[msg_id])
                    # metadt = metadata_messages(d, msg_id)

                    return dict_metadata[msg_id]

# @task
def save_metadata(metadata):
    """
    ON CONFLICT (id) DO NOTHING - вариант для отказ записи Дубликата
    Перед заполнением таблицы очищаем данные
    """
    conn = duckdb.connect(str(DB_PATH))

    try:
        conn.execute("""
        TRUNCATE TABLE metadata;
        """)
        for content in metadata.values():
            conn.execute("""
                    INSERT INTO metadata
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT (channel_link, id) DO NOTHING
                """, (
                content.id,
                content.message_date,
                content.grade,
                content.vacancy_name,
                content.location,
                content.channel_name,
                content.channel_link,
            ))

    finally:
        conn.close()


# @task
def table_data():
    """
    Три варианта вывода таблицы
    """

    conn = duckdb.connect(str(DB_PATH))

    # TODO Вариант 1
    # table = conn.execute("""
    #     select *
    #     from metadata
    # """).fetchall()

    # print(table)

    # TODO Вариант 2

    table = conn.sql("""
        SELECT *
        FROM metadata
        where message_date >= CURRENT_DATE - INTERVAL '2 months'
        order by message_date
    """)

    print(table.show(max_rows=1000))

    # TODO Вариант 3

    # table = conn.execute("""
    #         SELECT *
    #         FROM metadata
    #     """).fetchdf()
    #
    # print(table)

    # TODO Вариант 4
    # pd.set_option('display.max_columns', None)
    #
    # df_mdata = pd.DataFrame(table.show(max_rows=1000), columns=table.columns)
    #
    # print(df_mdata)

    # TODO Проверка типа даты
    # typed = conn.sql("""
    #    SELECT pg_typeof(message_date)
    #    FROM metadata
    #    """)
    # print(typed)

    conn.close()
    # return table


# @flow
async def main():
    init_database()

    await client.start()

    me = await client.get_me()

    print(f"Подключение успешно.")
    print(f"Имя: {me.first_name}")
    print(f"ID: {me.id}")

    num_msg = 0
    dict_mdata = {}  # Словарь Для последней строки
    # metadata_list = []
    for chanel_name, chanel_link in CHANNELS.items():
        print(f"{chanel_name} : {chanel_link}")

        # Вызов генератора
        async for message in extract_messages(chanel_link):
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

                            dict_mdata[message.id] = metadata_messages(message.id, compar, chanel_name, chanel_link)

                            # if metadt:

                            # metadata_list.append(metadt)




            else:
                print(" No messages")

    # print(dict_mdata)

    await client.disconnect()

    save_metadata(dict_mdata)

    table_data()

    return dict_mdata


if __name__ == "__main__":
    # main()
    asyncio.run(main())

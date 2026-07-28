'''
client — это клиент, через которого мы общаемся с Telegram.
message — это конкретное сообщение, которое мы получили от Telegram.
'''
import asyncio

from telethon import TelegramClient


# API_ID = 123
# API_HASH = "..."

API_ID = 328186771928
API_HASH = "e77003c295d40288e495464e52d7d41e1961km1"

# CHANNEL = "t.me/Kirill_50plus_DS"
CHANNEL = "https://t.me/tbaudiobook"

# Создали клиента
client = TelegramClient(
    "telegram_session",
    API_ID,
    API_HASH
)

async def main():

    await client.start()

    print("Подключение к Telegram успешно!")

    async for message in client.iter_messages(
        CHANNEL,
        limit=4000
    ):

        print(
            message.id,
            message.date,
            message.text,
            message.file
        )
        if message.file:
            print(
                "НАЙДЕН ФАЙЛ:",
                message.file.name,
                message.file.size
            )

    # await main()
asyncio.run(main())

# async def main():
#
#     await client.start()  # Подключились к Telegram
#
#     print("Подключение к Telegram успешно!")
#
#     async for message in client.iter_messages(  # Получаем сообщения
#         CHANNEL,
#         limit=4000
#     ):
#
#         print(
#             "ID:", message.id,
#             "| Дата:", message.date,
#             "| Текст:", message.text,
#             "| Файл:", message.file
#         )
#
#
# asyncio.run(main())
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from seleniumwire import webdriver # Используем selenium-wire вместо обычного webdriver
import json
from blinker import _saferef
import requests
from bs4 import BeautifulSoup
import blinker

print(_saferef)


# TODO Отладочный код
# url = "https://e-disclosure.ru/api/events/page?companyId=402&year=2005"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
# }
#
# response = requests.get(url, headers=headers)
#
# # Проверяем HTTP-статус
# print(f"HTTP-статус: {response.status_code}")
#
# # Выводим содержимое ответа для отладки
# print("Тело ответа:")
# print(response.text)  # Выводим текст ответа сервера
#
# # Проверяем, можно ли распарсить JSON
# try:
#     data = response.json()
#     print("JSON-данные:", data)
# except requests.exceptions.JSONDecodeError:
#     print("Ошибка декодирования JSON")


# TODO  Перехватить запрос в Selenium


# URL API для компании с ID 402 и годом 2005
url = "https://e-disclosure.ru/api/events/page?companyId=402&year=2005"

# Настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Без интерфейса

# Запуск браузера
driver = webdriver.Chrome(options=options)

# Открываем страницу
# Подождите, пока страница полностью загрузится
driver.get("https://e-disclosure.ru/portal/company.aspx?id=402&year=2005")
time.sleep(5)  # Дайте странице время для полной загрузки

# Перехватываем запросы к API
for request in driver.requests:
    print(f"Запрос к URL: {request.url}")  # Выводим URL запроса
    if "api/events/page" in request.url:
        print("Найден API запрос!")  # Лог для отладки
        response = request.response
        if response and response.status_code == 200:
            try:
                data = json.loads(response.body)
                for event in data.get("events", []):
                    print("Название события:", event["eventName"].strip())
                    print("Дата публикации:", event["pubDate"])
            except json.JSONDecodeError as e:
                print("Ошибка при декодировании JSON:", e)



# Закрываем браузер
driver.quit()



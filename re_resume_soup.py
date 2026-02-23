import re
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import random
import pprint
import csv


# TODO получение  data из сайта . . .
# URL сайта
url = "https://itresume.ru/problems/selection-sql"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
}

# Отправляем GET-запрос
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)


# TODO просмотр всех тегов 'a'
for i in soup.find_all("a"):
    ...
    # print(i)

# TODO просмотр всех классов
for i in soup.find_all("div"):
    ...
    # print(i.get('class'))

# TODO prettify() Выведет весь HTML-код страницы
# print(soup.prettify())  # Выведет весь HTML-код страницы


# TODO Поиск через href всех тегов <a> внутри блока задач
tasks = soup.find_all("a", href=True)
# print(tasks, 'taskstaskstaskstaskstaskstasks', '\n')


# TODO a["href"] - используется для получения значения атрибута href у тега <a>
# Фильтрация задач по ссылкам, относящимся к разделу задач
task_links = [a.text.strip() for a in tasks if "/problems/selection-" in a["href"]]

print(task_links, '\n')


# TODO Поиск через КЛАССЫ всех тегов <a> внутри блока ВКЛАДОК
bookmark = soup.find_all("a", class_=True)
# print(bookmark, 'taskstaskstaskstaskstaskstasks', '\n')


# Фильтрация задач по ссылкам, относящимся к ВКЛАДКАМ
task_links = ' '.join([a.text for a in bookmark])
print(task_links, '\n')




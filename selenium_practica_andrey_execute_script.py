from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup

# TODO c GitHub Eduson
# years_company_urls = []
# driver = webdriver.Chrome()
# # driver = webdriver.Firefox()
#
# #Метод, который создает экземпляр веб-драйвера для браузера Chrome.
# #Если вы хотите использовать другой браузер, вам нужно будет изменить эту строку на соответствующий метод (например, webdriver.Firefox() для Firefox).
# for u in range (400, 403):
#     url0 = "https://e-disclosure.ru/portal/company.aspx?id=" + str(u)
#     driver.get(url0)
#     driver.implicitly_wait(30)  # Время ожидания открытия сайта 30сек.
#     years = []  # Инициализируем переменную years
#     try:
#         years = driver.execute_script('return edCompanyEventList._data["years"]')  # ТУТ МЫ ПРОХОДИМСЯ ПО ГОДАМ
#     except Exception as e:
#         print(f"Ошибка при получении данных для id {u}: {e}")  # Логируем ошибку
#     if years:
#         for year in years:
#             if years != 0:
#                 res = 'https://e-disclosure.ru/Event/Page?companyId=' + str(u) + "&year=" + str(year) + "&attempt=1"
#                 years_company_urls.append(res)
#
# years_company_urls
#
# driver.quit()  # Закрываем веб-драйвер


# TODO Исправленный код Куратора
years_company_urls = []
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

for u in range(401, 402):
    url0 = "https://e-disclosure.ru/portal/company.aspx?id=" + str(u)
    driver.get(url0)
    driver.implicitly_wait(30)  # Время ожидания открытия сайта 30сек.

    years = []  # Инициализируем переменную years

    try:
        # TODO аргументы в execute_script:
        #  edCompanyEventList - нет в JS,  querySelectorAll - есть в JS
        years = driver.execute_script(
            # 'return edCompanyEventList._data["years"]'   # Не получаем данные о годах тк edCompanyEventList не существует

            # TODO jQuery["event"] - переменная существует
            'return  jQuery["event"]'  # Получаем данные о событиях но без дат, jQuery["event"] - существует

            # 'return Array.from(document.querySelectorAll("a")).map(a => a.href);'  # АЛ Получаем ссылки из Тега "а"

            # TODO пример из GPT, querySelectorAll — позволяет находить элементы на странице по CSS-селектору.
            # 'return document.querySelectorAll("div.event-list-item")'
        )
    except Exception as e:
        print(f"Ошибка при получении данных для id {u}: {e}")  # Логируем ошибку

    if years:  # Проверяем, что years не пустой
        for year in years:
            if year != 0:  # Проверяем, что год не равен 0
                res = 'https://e-disclosure.ru/Event/Page?companyId=' + str(u) + "&year=" + str(year) + "&attempt=1"
                years_company_urls.append(res)

print(years_company_urls)  # Выводим собранные URL

driver.quit()  # Закрываем веб-драйвер

# TODO Перехват AJAX
# ajax_url = "https://e-disclosure.ru/portal/company.aspx?id=400"  # Узнай URL в DevTools
# response = requests.get(ajax_url, headers={"User-Agent": "Mozilla/5.0"})
# print(response.json())  # Если ответ в JSON


# TODO Вариант GPT -> возращает В64, JAVA
# url = "https://e-disclosure.ru/portal/company.aspx?id=400"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
#     "Referer": "https://www.google.com/",  # Подделываем источник запроса
# }
#
# response = requests.get(url, headers=headers)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     print(soup.prettify())  # Проверяем содержимое страницы
# else:
#     print(f"Ошибка: {response.status_code}")

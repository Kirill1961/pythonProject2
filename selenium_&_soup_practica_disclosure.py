import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs


# Настройки Chrome
options = Options()
options.add_argument("--headless")  # Убираем графический интерфейс (можно убрать)
options.add_argument("--disable-blink-features=AutomationControlled")  # Маскируем Selenium
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# Установка драйвера и Запуск браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


# Открываем страницу
url = "https://e-disclosure.ru/portal/company.aspx?id=402"
# url = "https://e-disclosure.ru/portal/company.aspx?id="
driver.get(url)

# Ждём загрузки JS
driver.implicitly_wait(5)


# ajax_url = "https://kraken.rambler.ru/cnt/v2/"  # Узнай URL в DevTools
# response = requests.get(ajax_url, headers={"User-Agent": "Mozilla/5.0"})
# print(response.json())  # Если ответ в JSON

# TODO Разбираем URL Извлекаем query-параметры
# # Разбираем URL
# parsed_url = urlparse(url)
#
# # Извлекаем query-параметры
# query_params = parse_qs(parsed_url.query)
#
# print(query_params)  # {'id': ['401']}

# TODO Вставить итерацию сайтов
# years = []
# years = driver.execute_script('return edCompanyEventList._data["years"]') # execute_script - возвращает спсисок
# print(years)


#  TODO Извлекаем код страницы через BeautifulSoup
# Получаем HTML после выполнения JS
html = driver.page_source
# print(html)

# TODO Парсим через BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
#
# # Проверяем, что получилось
# # print(soup.prettify())
#
# # TODO Для понимания что и где брать просмотр всех классов
# # for i in soup.find_all("div"):
# #     print(i.get('class'))
#
# # TODO Для понимания что и где брать просмотр всех тегов 'p'
# # for i in soup.find_all("p"):
# #     print(i)
#
# # TODO просмотр всех тегов 'a'
# for i in soup.find_all("a"):
#     print(i)
#
# # TODO извлекаем Даты Событий
# dt = soup.find_all('span', class_='date')
# print(dt)

# TODO Вывод содержимого из тегов "а"
a_tag = soup.find_all("a", href=True)
href_val = [link.get('href') for link in a_tag]
# print(href_val)

# TODO Вывод только ссылок только https из тегов "а"
# a_tag = soup.find_all("a", href=True)
# href_link = [link['href'] for link in a_tag if link['href'].startswith('https')]
# print(href_link)

# TODO Извлекаем заданные тексты
event = soup.find_all('a', href=True)

for link in event:
    # if link.text == 'Решения, принятые советом директоров (наблюдательным советом)'in link.get('href'):
    print(link.text)


# for text_event in event:
#     if text_event.text == 'Решения общих собраний участников (акционеров)':
#         print(text_event)




# Закрываем браузер
driver.quit()


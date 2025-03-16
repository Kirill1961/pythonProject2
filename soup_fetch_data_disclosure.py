
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# # Настройки браузера
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Без GUI
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
#
# # Запуск браузера
# service = Service("chromedriver.exe")  # Укажи путь к chromedriver, если нужно
# driver = webdriver.Chrome(service=service, options=chrome_options)
#
# # Открываем страницу
# url = "https://e-disclosure.ru/portal/company.aspx?id=401"
# driver.get(url)
#
# # Даем время на загрузку JavaScript (можно заменить на WebDriverWait)
# driver.implicitly_wait(5)
#
# # Получаем HTML после выполнения JS
# html = driver.page_source
#
# # Закрываем браузер
# driver.quit()



url = "https://e-disclosure.ru/portal/company.aspx?id=402"

headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-kl-ajax-request": "Ajax_Request",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://e-disclosure.ru/portal/company.aspx?id=401",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
print(response.status_code)
# Парсим HTML с BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
# Ищем input с id="EventsYears"

# for i in soup.find_all("div"):
#     print(i.get('class'))

tag = soup.find_all('td', {'class':'field-name'})
# print(tag)
tag_total = [link.text + ' ' + '-' + ' ' + link.find_next_sibling('td').text for link in tag]
print(tag_total)
# if input_tag:
#     years = input_tag["value"].split(",")
#     print("Доступные годы:", years)
# else:
#     print("Поле 'EventsYears' не найдено!")



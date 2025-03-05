from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Настройки браузера
chrome_options = Options()
chrome_options.add_argument("--headless")  # Без GUI
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Запуск браузера
service = Service("chromedriver.exe")  # Укажи путь к chromedriver, если нужно
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открываем страницу
url = "https://e-disclosure.ru/portal/company.aspx?id=401"
driver.get(url)

# Даем время на загрузку JavaScript (можно заменить на WebDriverWait)
driver.implicitly_wait(5)

# Получаем HTML после выполнения JS
html = driver.page_source

# Парсим HTML с BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Ищем input с id="EventsYears"
input_tag = soup.find("input", {"id": "EventsYears"})

if input_tag:
    years = input_tag["value"].split(",")
    print("📅 Доступные годы:", years)
else:
    print("⚠️ Поле 'EventsYears' не найдено!")

# Закрываем браузер
driver.quit()

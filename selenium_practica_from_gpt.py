from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs

# URL страницы
url = "https://e-disclosure.ru/portal/company.aspx?id=401"

# Настройки браузера
options = Options()
options.add_argument("--headless")  # Без интерфейса
options.add_argument("--disable-blink-features=AutomationControlled")  # Маскировка Selenium
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# Запуск Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Открываем страницу
driver.get(url)

# Ожидание загрузки страницы и выполнения JS
try:
    # print(driver.page_source)  # Выведет весь HTML, который видит Selenium
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "ctl00_MainContent_lbEmittentName"))
    )
    print("Страница загружена, пробуем получить данные...")
except:
    print("Ошибка: страница не загрузилась.")
    driver.quit()
    exit()

# TODO Попробуем выполнить JavaScript для получения лет событий,
#  edCompanyEventList - отсутствует в JS, поэтому ошибка
try:
    years = driver.execute_script("return window.edCompanyEventList ? edCompanyEventList._data['years'] : null;")

    if years:
        print("Найденные года событий:", years)
    else:
        print("Не удалось получить года событий.")
except Exception as e:
    print("Ошибка выполнения JavaScript:", e)

# Закрываем браузер
driver.quit()

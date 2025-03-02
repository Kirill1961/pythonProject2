from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# TODO Открываем браузер
driver = webdriver.Chrome()  # Запускает Chrome
driver.get("https://www.google.com")  # Открывает страницу
# driver.get('http://radar.oreilly.com/2010/06/what-is-data-science.html')  # Открывает страницу

# TODO Находим элемент на странице
search_box = driver.find_element(By.NAME, "q")  # Поле поиска Google
search_box.send_keys("Selenium Python")  # Вводим текст
search_box.submit()  # Нажимаем Enter

# TODO Ждём загрузки страницы
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)

# TODO Парсим содержимое (с помощью BeautifulSoup)
html = driver.page_source  # Получаем HTML
soup = BeautifulSoup(html, "html5lib")  # Создаём объект BeautifulSoup
print(soup)
# TODO Закрываем браузер
driver.quit()
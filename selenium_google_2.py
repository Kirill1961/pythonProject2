from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка WebDriver (автоматическая установка ChromeDriver)
# TODO создаём объект options, который содержит настройки для браузера Chrome при запуске через Selenium.
#  объект options содержит настройки для браузера Chrome при запуске через Selenium.
options = webdriver.ChromeOptions()

# TODO Пример настроек options
# options.add_argument("--headless")  # Запуск без графического интерфейса
# options.add_argument("--disable-gpu")  # Отключение аппаратного ускорения
# options.add_argument("--start-maximized")  # Открытие окна в максимальном размере
# options.add_argument("--incognito")  # Запуск в режиме инкогнито
# options.add_argument("user-agent=Mozilla/5.0 (...)")  # Изменение User-Agent



# TODO "--headless" это задание режима работы браузера, а именно отключение отображения на экране
# options.add_argument("--headless")  # Запуск без графического интерфейса (если не нужен)

# TODO ЯВНОЕ отключение отображения браузера на экране
options.headless = False

# TODO Создаём экземпляр WebDriver, который управляет браузером Chrome.
#  WebDriver - позволяет Selenium отправлять команды браузеру (открывать страницы, кликать, вводить текст и т. д.).
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # 1. Открываем Google
    driver.get("https://www.google.com")

    # 2. Находим поле поиска и вводим запрос
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)

    # 3. Ждём загрузки результатов
    time.sleep(10)

    # 4. Получаем заголовки результатов поиска
    results = driver.find_elements(By.CSS_SELECTOR, "h3")

    print("\n🔹 Результаты поиска:")
    for i, result in enumerate(results[:5], 1):  # Выводим первые 5 заголовков
        print(f"{i}. {result.text}")

finally:
    # 5. Закрываем браузер
    driver.quit()

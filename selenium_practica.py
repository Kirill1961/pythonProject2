from selenium import webdriver

# Создаём экземпляр веб-драйвера
driver = webdriver.Chrome()

# Открываем страницу c id=403
url = "https://e-disclosure.ru/portal/company.aspx?id=403"
driver.get(url)

# Ожидаем загрузку страницы
driver.implicitly_wait(10)

#TODO Выполняем JavaScript-код для получения всех ссылок на странице
links = driver.execute_script(
    # здесь мы получаем все ссылки по тегу а на странице и
    # и возвращаем их ввиде массива строка в links
    # 'return Array.from(document.querySelectorAll("a")).map(a => a.href);'
    'return edCompanyEventList._data["years"];'
)

# Выводим список ссылок
for link in links:
    print(link)

# Закрываем браузер
driver.quit()

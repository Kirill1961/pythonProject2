from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# years_company_urls = []
# driver = webdriver.Chrome()
# #Метод, который создает экземпляр веб-драйвера для браузера Chrome.
# #Если вы хотите использовать другой браузер, вам нужно будет изменить эту строку на соответствующий метод (например, webdriver.Firefox() для Firefox).
# for u in range (400, 403):
#     url0 = "https://e-disclosure.ru/portal/company.aspx?id=" + str(u)
#     driver.get(url0)
#     driver.implicitly_wait(30)
#     years = []
#     try:
#         years = driver.execute_script('return edCompanyEventList._data["years"]') # ТУТ МЫ ПРОХОДИМСЯ ПО ГОДАМ
#     except:
#         pass
#     if years:
#         for year in years:
#             if years != 0:
#                 res = 'https://e-disclosure.ru/Event/Page?companyId=' + str(u) + "&year=" + str(year) + "&attempt=1"
#                 years_company_urls.append(res)
#
# years_company_urls

# Создаем пустой список для хранения URL
years_company_urls = []
# Создаем экземпляр веб-драйвера для браузера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Перебираем диапазон значений
for u in range(400, 403):
    url0 = "<https://e-disclosure.ru/portal/company.aspx?id=> " + str(u)
    driver.get(url0)
    try:
        # Ждем, пока JavaScript переменная будет доступна
        WebDriverWait(driver, 10).until(lambda d: d.execute_script('return typeof edCompanyEventList !== "undefined"'))
        years = driver.execute_script('return edCompanyEventList._data["years"]')
        # Убедимся, что переменная `years`определена и является списком
        if years and isinstance(years, list):
            for year in years:
                if year != 0: # Проверяем значение year
                    res = f'<https://e-disclosure.ru/Event/Page?companyId={u}&year={year}&attempt=1>'
                    years_company_urls.append(res)
    except Exception as e:
        print(f"Error fetching years for company {u}: {e}")
# Закрываем веб-драйвер
driver.quit()
# Выводим результаты
print(years_company_urls)



years_company_urls = []
driver = webdriver.Chrome()
#Метод, который создает экземпляр веб-драйвера для браузера Chrome.
#Если вы хотите использовать другой браузер, вам нужно будет изменить эту строку на соответствующий метод (например, webdriver.Firefox() для Firefox).
for u in range (400, 420):
    url0 = "https://e-disclosure.ru/portal/company.aspx?id=" + str(u)
    driver.get(url0)
    driver.implicitly_wait(30)
    try:
        years = driver.execute_script('return edCompanyEventList._data["years"]') # ТУТ МЫ ПРОХОДИМСЯ ПО ГОДАМ
    except:
        pass
    if years:
        for year in years:
            if years != 0:
                res = 'https://e-disclosure.ru/Event/Page?companyId=' + str(u) + "&year=" + str(year) + "&attempt=1"
                years_company_urls.append(res)

years_company_urls



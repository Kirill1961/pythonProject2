import pandas as pd
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import re

url = "https://e-disclosure.ru/api/events/page?companyId=401&year=2016"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
}


# years_company_urls = []
# driver = webdriver.Chrome()
#Метод, который создает экземпляр веб-драйвера для браузера Chrome.
#Если вы хотите использовать другой браузер, вам нужно будет изменить эту строку на соответствующий метод (например, webdriver.Firefox() для Firefox).
# for u in range (400, 402):
#     url0 = "https://e-disclosure.ru/api/events/page?companyId=" + str(u) + '&year=2016'
    # time.sleep(5)
    # driver.get(url0)
    # driver.implicitly_wait(30)
    # years = driver.execute_script('return eventDate')
    # print(url0)
    # years_company_urls.append(url0)
# print(years_company_urls)

respons = requests.get(url)
soup = BeautifulSoup(respons.text, 'lxml')
r = soup.find('input', id="EventsYears")
print(r)


for i in soup.find_all("div"):

    print(i.get('class'))


# df = pd.DataFrame(columns = ['URL', 'ID', 'YEAR'])
# i = 0
# for url in years_company_urls:
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, 'lxml')
#     for link in soup.find_all('a'):
#         if link.text == 'Решения общих собраний участников (акционеров)' or link.text == 'Решения совета директоров (наблюдательного совета)' in link.get('href'):
#             #if i >= 10:
#             #   print("break")
#             #    break
#             a = re.split(r'==([^<>]+)&', url.replace("&year=", "=="))
#             b = re.split(r'=([^<>]+)==', url.replace("&year=", "=="))
#             df = df.append({'URL' : link.get('href'), 'ID' : b[1], 'YEAR' : a[1]},ignore_index = True)
#             i += 1
#             print(i)
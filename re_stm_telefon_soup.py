from bs4 import BeautifulSoup
import requests
import re

url = "https://stmgroup.ru/?ysclid=m7k9au82m338007291"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
}


# TODO prettify() Выведет весь HTML-код страницы
# print(soup.prettify())  # Выведет весь HTML-код страницы

container = requests.get(url, headers=headers).text
# print(container)

soup = BeautifulSoup(container, "html.parser")
# print(soup)


# TODO Для понимания что и где брать просмотр всех тегов 'a'
# for i in soup.find_all("a"):
    # print(i)

# TODO Для понимания что и где брать просмотр всех классов
# for i in soup.find_all("div"):
    # print(i.get('class'))


# TODO Для понимания что и где брать просмотр всех тегов 'p'
# for i in soup.find_all("p"):
#     print(i)


# TODO select_one Вывод текста из одного Тега
p_tag = soup.select_one('p').text
print(f'Вывод текста из одного Тега -> {p_tag}', '\n')


# TODO вывод номенклатуры каталога, по тегу 'p'
p_tag = soup.find_all('p', class_="card__title card-title")
# print(p_tag)

category = [elem.text for elem in p_tag]
print(category, '\n')




# TODO Каскад из трёх запросов - Вывод адреса и телефонов, НЕ рационально
divs = soup.find("p", class_="main-title").text
# print(divs)

divs1 = soup.find("p", class_="main-title").find_next_sibling('p').text
# print(divs1)

divs2 = soup.find("p", class_="main-title").find_next_sibling('p').find_next_sibling('p').text.strip()
print(divs, divs1, divs2)


# TODO Как вариант очистка с stripped_strings - генератор, работает только с ОБ BeautifulSoup
strip_str = soup.find("p", class_="main-title").find_next_sibling('p')
r = [i for i in strip_str.stripped_strings]
# print(r)


# TODO Пример из GPT

html = """
<p class="main-title">Центральный склад</p>
<p>Воронежская обл., Рамонский р-н, Айдаровское сельское поселение, ул. Промышленная, зона 5, участок 8, стр. 1</p>
<p>пн-пт: 9:00-18:00, сб: 9:00-14:00</p>
<p><a href="tel:+74732070057">+7 (473) 207-00-57</a></p>
"""

soup = BeautifulSoup(html, "html.parser")

# Находим первый нужный <p>
start_p = soup.find("p", class_="main-title")

# Собираем все следующие <p>, кроме последнего (с телефоном)
texts = [p.text.strip() for p in start_p.find_all_next("p")[:-1]]

print(texts)

# adr = soup.find_all("p")
# print(adr)
#
# for ad in adr:
#     print(ad.text)

# adr1 = soup.find("p", {"class": "main-title"})
# print(adr1)
#
# adr2 = soup.find("p")
# print(adr2)


respons_js = requests.get(url)
try:
    js = respons_js.json()
    print(js)
except:
    print('Error')
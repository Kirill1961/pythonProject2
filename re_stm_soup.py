'''
Извлечение и Вывод с сайта СТМ - Воронеж позиций и ссылки на них
'''

from bs4 import BeautifulSoup
import requests
import re

url = "https://stmgroup.ru/?ysclid=m7k9au82m338007291"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
}

# Отправляем GET-запрос
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup)


# TODO просмотр всех тегов 'a'
# for i in soup.find_all("a"):
#     ...
    # print(i)

# TODO просмотр всех классов
# for i in soup.find_all("div"):
#     ...
    # print(i.get('class'))

# TODO prettify() Выведет весь HTML-код страницы
# print(soup.prettify())  # Выведет весь HTML-код страницы


# URL главной страницы компании
base_url = "https://stmgroup.ru/?ysclid=m7k9au82m338007291"  # Замени на реальный адрес сайта

# Делаем запрос к главной странице
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

# Ищем ссылку на прайс-лист
price_link = soup.find("a", class_="site-nav__link price-list-link")

if price_link and "href" in price_link.attrs:

# TODO  Формируем полный URL, присоединяем url главной страницы к ссылке на прайс
    price_url = base_url + price_link["href"]

    # Делаем запрос к прайс-листу
    price_response = requests.get(price_url)

    # Выводим содержимое страницы прайс-листа
    # print(price_response.text)
    print("Ссылка на прайс-лист найдена.")
else:
    print("Ссылка на прайс-лист не найдена.")

# TODO Извлечение Категорий из прайса
categories = soup.find_all("li", class_="side-catalog__item")
# print(categories, '>>>>>>>>>>>>>>>>')

# TODO i.stripped_strings - вариант удаления html символов на лету неочень правильный
# text_vs_category = [list(i.stripped_strings) for i in categories]
# print(text_vs_category)


# TODO Заготовка для корректного вывода инф. -> Ссылки на каталог + наименование товарной группы
name_and_reference = soup.find_all('a', class_="side-catalog__link", href=True)
# print(name_and_reference)


# TODO Два варианта Извлечения 'href' -> i.get и i['href']
link_get = [i.get('href') for i in name_and_reference]
# print(link_get)
link_href = [i['href'] for i in name_and_reference]
# print(link_href)


# TODO text_vs_category - подготовка для удаления html символов
text_vs_category = [i.text for i in categories]
# print(text_vs_category)

# TODO Удаление html символов -> \n \r \t с помощью re.sub
clean_list_text = [re.sub(r'\s+', ' ', item).strip() for item in text_vs_category]
# print(clean_list_text)

# TODO Итогова обработка, Вывод текста + ссылка. Преобразование генератора с " ".join
result = [{" ".join(item.stripped_strings): item['href']}for item in name_and_reference]
print(result)

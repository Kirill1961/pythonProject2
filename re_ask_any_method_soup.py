import re
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import random
import pprint
import csv


# TODO получение  data из сайта deltaks

CSV = "cards.csv"

# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
# }

HEADERS = {
 "Accept": "?ysclid=m7k9au82m338007291",
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
 }


# HOST = "https://deltaks.ru/"  # вытащить можно только data из url передано в BS, HOST всегда оканчивается "/"


HOST = "https://stmgroup.ru/"


URL_ABOUT = "https://stmgroup.ru/Shop/About/"  # url для EX сведений о компании

URL_ARTIKLE = "https://stmgroup.ru/Shop/Article"  # url для extract(ЕХ) статей


# TODO ask
def ask_soup(
    url, params=" "
):  # url -  сайт / params=" " - именованный аргумент что бы далее присвоить значение
    html = requests.get(
        url, headers=HEADERS, params=params  # headers, params в моём случае не нужны
    )  # requests.get - запрос сайта по адресу из переменной url, text - запрос текста
    soup = BeautifulSoup(
        html.text, "lxml"
    )  # soup - ЭКЗ класса BS, 'lxml' - парсер которым будем пользоваться

    # TODO "Методы BeautifulSoup"

    # print("HTML: {0}, name:{1}, text: {2}".format(soup.div, soup.div.name, soup.div.text), "\n")  # вывод тега и его содержимого

    # content_1 = soup.recursiveChildGenerator()  # поиск тегов по имени
    # for i in content_1:
    #     if i.name == "hr":
    #         print(i, "\n")

    # for tag in soup.find_all(True):   # находит все теги в документе, но не текстовые строки
    #     print(tag.name)

    # root = soup.hr
    # rc = [e.name for e in root.children if e.name is not None]  # дочерние элементы тегов
    # print(rc, "\n")

    # root = soup.hr
    # rc = [e.name for e in root.descendants if e.name is not None]  # находим всех потомков div
    # print(rc, "\n")

    # root = soup.hr
    # rc = [soup.find(e.name) for e in root.descendants if e.name is not None if
    #       e.name == "hr"]  # находим заданных потомков div и их атрибуты
    # print(rc, "\n")

    # link = soup.a  # вывод родителей снизу вверх
    # for parent in link.parents:
    #     if parent is None:
    #         print(parent)
    #     else:
    #         print(parent.name)

    # def has_class_but_no_id(tag):   # поиск атрибутов
    #     return tag.has_attr('style') and not tag.has_attr('a')
    # print(soup.find_all(has_class_but_no_id))

    # for tag in soup.find_all(re.compile("sp")):  # поиск тегов содержащих "sp" или другие str
    #     print(tag.name)

    # content_1 = soup.find_all(href=re.compile("https://metrika"))  # поиск ссылок  по атрибуту href

    # content = soup.find\
    #     ("div", class_="container body-content").find\
    #     ("ul", class_="list-inline").find\
    #     ("li", class_="list-inline-item").get(
    # "a", "https://metrika.yandex.ru/stat/?id=4491112&from=informer")  # спускаемся по дереву к нужному тегу

    # content_1 = soup.find("div", class_="container").find("div", class_="container").find(find\
    #     #     ("div", class_="container body-content")) \
    #     .find("span", style="margin-left: 40px")
    # TODO cards
    cards = []
    # TODO "ВАЖНО! Правильно составить доступ к родителю, очерёдность методов find и find_all"
    contents = soup.find("div", id="index").find_all(
        "div", class_="card card-body flex-fill my-flex"
    )  # id - родитель для каталога

    # TODO  проверка на отклик сайта
    if html.status_code == 200:
        for content in contents:  # форлуп вы атрибутов в теге "а"
            total_cards = {
                "title_": content.find("a").find("img").get("title"),
                "href_": HOST + content.find("a").get("href"),
                "image_": HOST + content.find("a").find("img").get("src"),
            }
            cards.append(total_cards)
        return cards
    else:
        print("Error")


# TODO сохранение в csv
def save_cards(path):  # сохранение в csv
    content = ask_soup(HOST)
    with open(path, "w", newline="") as file:
        write = csv.writer(file, delimiter=" ")  # delimiter - разделитель
        write.writerow(["Name product", "link on product", "link on image"])
        for item in content:
            write.writerow([item["title_"], item["href_"], item["image_"]])
    with open(path, "r") as read:
        print(read.read())


save_cards(CSV)


# def parser(url):
#     PAGINATION = input("Ввод:")
#     PAGINATION = int(PAGINATION.strip())
#     html = ask_soup(HOST)
#     if html.status_code == 200:
#         print("OK")
#         # for page in range(1, PAGINATION):
#         #     print(f"parsingpage: {page}")
#         #     html = ask_soup(HOST)
#     else:
#         print("Error")


# pprint.pp(parser(HOST))
# TODO end

# pprint.pprint(ask_soup(HOST))

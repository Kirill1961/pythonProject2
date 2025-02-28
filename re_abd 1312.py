import re
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import random
import pprint



def fix_unicode(text):
    return text.replace(u"\u2019", "'")  # изменение кодировки


# url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"  # сохраняем сайт в переменную
# html = requests.get(url).text  # requests.get - запрос сайта по адресу из переменной url, .text - очистка от тегов и тд
# soup = BeautifulSoup(html, 'html5lib')  # 'html5lib' - формат возвращаемого текста из переменной html
#
# content = soup.find("div", "entry-content")  #
# regex = r"[\w']+|[\.]"  # re выбирает слова из тега "div" класса "entry-content"
#
# document = []
#
# for paragraph in content("p"):  # извлекаем текст с тегом <р> из ("div", "entry-content")
#     words = re.findall(regex, fix_unicode(paragraph.text))  # отбор с помощью re слов
#     document.extend(words)
#
# # print(document)
#
# """ Куча мала, в словаре transition все слова из document = [], поочерёдно key и value"""
# bigrams = zip(document, document[1:])  # zip составляет пары из 1-го и 2-го слов и сохраняем в bigrams
# transition = defaultdict(list)  # словарь по умолчанию, values - тип list позволяет использовать методы списков
# # print(transition, ">>>")
#
#
# for prev, current in bigrams:
#     print(prev, current, "^^^^^^^^^^^^^^^^^^")
#     transition[prev].append(current)  # вставляем в dict (transition) ключи prev и значения current
#
# print(transition, "\n")
# print(prev, "prev")
# print(transition[prev], ">>>", "\n")
#
#
# def generate_using_bigrams():
#     # print(transition, ">>>")
#     current = "."
#     result = []
#     n = 0
#     while n < 2:
#         n += 1
#         next_word_candidates = transition[current]
#         print(next_word_candidates, "|||||||||||||||", "\n")
#         current = random.choice(next_word_candidates)   # рандомно выбираем value д/result[] и key д/transition
#         result.append(current)
#         print(result, "result", "\n")
#         if current == ".": return " ".join(result)
#
#
# print(generate_using_bigrams())


# trigrams = zip(document, document[1:], document[2:])
# trigram_transitions = defaultdict(list)
# starts = []
# for prev, current, next in trigrams:
#     if prev == ".":
#         starts.append(current)
#
#
#     trigram_transitions[(prev, current)].append(next)
#
#
# def generate_using_trigrams():
#     current = random.choice(starts)
#     prev = "."
#     result = [current]
#     while True:
#         next_word_candidates = trigram_transitions[(prev, current)]
#         next_word = random.choice(next_word_candidates)
#         prev, current = current, next_word, result.append(current)
#         if current == ".":
#             return " ".join(result)


""" пример, подразумеваем что через requests.get(url) сайт получен"""


def exempl(x):
    with open(x, 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        s = soup.findAll("p")  # тк find извлекает 1-е совпадение, применяем findAll для извл. всех совпадений
        # print(soup.h2)
        # print(soup.head)
        # print(soup.li)
        # print(soup.p)
        return s


# print(exempl('H_T_M_L.html'))


# TODO """ получение  data из сайта deltaks"""

# HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"}

HEADERS = {"Accept": "product/smazka-pronikayushchaya-mnogotselevaya-universalnaya-rc-40-650-ml-4046-wd-590041638/?at=J8tgo4B6GF2Gk5y5cG4NYw3iM8159KIX5QPNNH8E9ZMz&from_sku=590041638&oos_search=false",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"}


# HOST = "https://deltaks.ru/"  # вытащить можно только data из url передано в BS, HOST всегда оканчивается "/"

HOST = "https://www.ozon.ru/"

URL_ABOUT = "https://deltaks.ru/Shop/About/"  # url для EX сведений о компании

URL_ARTIKLE = "https://deltaks.ru/Shop/Article"  # url для extract(ЕХ) статей


# TODO ask
def ask_soup(url, params=" "):  # передали сайт в аргумент
    html = requests.get(url, headers=HEADERS,
                        params=params)  # requests.get - запрос сайта по адресу из переменной url, text - запрос текста
# TODO очистка от тегов непосредственно при передачи аргумента html
    soup = BeautifulSoup(html.text, 'html.parser')  # soup - ЭКЗ класса BS, 'lxml' - парсер которым будем пользоваться

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

    cards = []

    contents = soup.find_all("div", id="index", class_="row justify-content-start")
    for content in contents:
        # cards.append(content.get_text(strip=True))

        cards.append(
            {

                "title": content.find("img").get("title"),
                "url": HOST + content.find("a").get("href"),
                "image": HOST + content.find("img").get("src"),
            }
        )

        # content_1 = soup.find("div")

    print (cards)
    # print("HTML: {0}, name:{1}, text: {2}".format(soup.h1, soup.h1.name, soup.h1.text))
    return html, soup
def parser(url):
    html, soup = ask_soup(HOST)
    if html.status_code == 200:
        print("OK")
    else:
        print("Error")

    return html.text
parser(HOST)
# TODO end

# pprint.pp(ask_soup(HOST))
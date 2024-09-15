import re
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import random
import pprint



# Два способа извлечения схемы доступа URL
web_url = "https://academy-data-science.eduson.tv/ru"

def extract_url_without_scheme(web_url):
    # паттерн для изъятия схемы доступа
    r = r"(^[a-zA-Z]+://)"
    scheme = re.findall(r, web_url)
    pat_for_trim_sub = re.compile(r)
    # паттерн для удаления схемы доступа
    pat_for_trim_pattern = r"([a-zA-Z:]+//)(.*)"
    # 1й способ удаление схемы доступа с помощью sub
    fetch_sheme = pat_for_trim_sub.sub("", web_url)
    # 2й способ удаление схемы доступа с помощью regex
    trim_scheme = re.match(pat_for_trim_pattern, web_url)

    return (f"схема доступа {scheme}, \n"
            f"удаление схемы доступа: \n"
            f"1й способ trim_scheme = {trim_scheme.group(2)} \n"
            f"2й способ  fetch_sheme = {fetch_sheme}")


print(extract_url_without_scheme(web_url))


def fix_unicode(text):
    return text.replace(u"\u2019", "'")  # изменение кодировки


# TODO pars
url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"  # сохраняем сайт в переменную
html = requests.get(url).text  # requests.get - запрос сайта по адресу из переменной url, .text - очистка от тегов и тд
soup = BeautifulSoup(html, 'html5lib')  # 'html5lib' - формат возвращаемого текста из переменной html

content = soup.find("div", "entry-content")  #
regex = r"[\w']+|[\.]"  # re выбирает слова из тега "div" класса "entry-content"

document = []


for paragraph in content("p"):  # извлекаем текст с тегом <р> из ("div", "entry-content")
    words = re.findall(regex, fix_unicode(paragraph.text))  # отбор с помощью re слов
    document.extend(words)
    print(document)

""" Куча мала, в словаре transition все слова из document = [], поочерёдно key и value"""
bigrams = zip(document, document[1:])  # zip составляет пары из 1-го и 2-го слов и сохраняем в bigrams
transition = defaultdict(list)  # словарь по умолчанию, values - тип list позволяет использовать методы списков


for prev, current in bigrams:
    transition[prev].append(current)  # вставляем в dict (transition) ключи prev и значения current


# TODO bigramm
def generate_using_bigrams():
    current = "We've"  # выбор слов для текста начинается с ОБ указанного в кавычках
    result = []
    while True:  # Если поставить while True: - то цикл работает до выполнения условия if
        next_word_candidates = transition[current]
        current = random.choice(next_word_candidates)  # рандомно выбираем value д/result[] и key д/transition
        result.append(current)
        if current == ".": return " ".join(result)  # условие для остановки while, if в тексте встретится ОБ "."


print(generate_using_bigrams(), " BIGRAMM", "\n"
                                            "")

trigrams = zip(document, document[1:], document[2:])  # разбиваем слова на тройки
trigram_transitions = defaultdict(list)  # словарь по умолчанию, values - тип list позволяет использовать методы списков
starts = []

for prev, current, next in trigrams:  # пользуем тройку слов "предыдущее-текущее-следующее"
    if prev == ".":  # выбор слов для текста начинается с ОБ указанного в кавычках
        starts.append(current)  # в starts = [] пишем "текущее"
    trigram_transitions[(prev, current)].append(next)  # Заполняем словарь key - (prev, current) и value - (next)


# TODO trigramm
def generate_using_trigrams():
    current = random.choice(starts)  # из starts произвольно выбранное слово
    prev = "."  # "." ставится перед случайно выбранным current
    result = [current]  # создаём словарь для записи сгенерированного текста

    while True:

        next_word_candidates = trigram_transitions[(prev, current)]  # вызываем словарь с ключом (prev, current)
        # и сохраняем в переменную next_word_candidates значение в виде списка

        next_word = random.choice(next_word_candidates)  # случайно слово из next_word_candidates

        prev, current = current, next_word  # перемещаем ОБ из переменной current в prev и из next_word в current
        result.append(current)  #
        if current == ".":
            return " ".join(result)


print(generate_using_trigrams(), " TRIGRAMM")

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



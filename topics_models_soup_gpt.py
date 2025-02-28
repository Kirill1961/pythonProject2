from gensim import corpora, models
import numpy as np
import re
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import random



def fix_unicode(text):
    return text.replace(u"\u2019", "'")  # изменение кодировки

# url = "http://radar.oreilly.com/2010/06/what-is-data-science.html" # сохраняем сайт в переменную
url = "http://radar.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page=1"  # сохраняем сайт в переменную
# url = "https://www.e-disclosure.ru/portal/company.aspx?id=4543"  # сохраняем сайт в переменную

# TODO .text - очистка от тегов и тд сразу при получении ответа на запрос
html = requests.get(url).text  # requests.get - запрос сайта по адресу из переменной url, .text - очистка от тегов и тд

soup = BeautifulSoup(html, 'html5lib')  # 'html5lib' - парсер, формат возвращаемого текста из переменной html


# TODO Выведем все классы у `div`, чтобы понять, какие есть
for div in soup.find_all("div"):

    print(div.get("class"))

# TODO Вывод ограниченного числа Символов html, в данном случае 20000
# print(html[:20000])


# TODO Вывод текста тега <p> в чистом виде
text = soup.a.text
print(text, '*****************************')
print(text.split())

# TODO Выбираем нужный класс class_="content"
content = soup.find("div", class_="content")  # Тег "div" по которому будем искать в html слова или символы из класса content
print(content)

# TODO шаблон для извлечения текста из paragraph.text
regex = r"[\w']+|[\.]"  # шаблон regex выбирает слова из тега "div" класса "content"

document_radar = []
print(document_radar)

# TODO извлекаем текст с тегом <a> из класса ("div", "entry-content"), fix_unicode - обращение за парсером
for paragraph in content('a'):  # извлекаем текст с тегом <a> из ("div", "entry-content")
    # print(paragraph, '>>')
    words = re.findall(regex, fix_unicode(paragraph.text))  # отбор с помощью re слов и парсера из fix_unicode
    document_radar.extend(words)
    print(document_radar)


documents = [document_radar]

# TODO Текстовые документы для Пробной прокрутки
#Предположим, у вас есть некоторые текстовые документы
#documents = [
#     "apple orange banana",
#     "banana apple",
#     "orange apple",
#     "banana banana orange",
#     "orange apple banana",
#     "banana orange",
#     "banana apple orange",
#     "apple banana",
#     "orange orange",
#     "banana"
# ]

# Разбиваем документы на токены
tokenized_documents = [document.split() for document in document_radar]

# TODO Пробный запуск с текстовыми документами documents
# tokenized_documents = [document.split() for document in documents]
# print(tokenized_documents, "tokenized_documents")


# Создаем словарь уникальных терминов
dictionary = corpora.Dictionary(tokenized_documents)
print(dictionary, "UNICUM terms dictionary")


# Преобразуем документы в мешок слов (Bag of Words) присваиваем всем уникальным словам № тематики
corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]
# print(corpus, "Bag of Words")


# Обучаем LDA модель
lda_model = models.LdaModel(corpus, id2word=dictionary, num_topics=5)
print(lda_model, "lda_model")


# Выводим темы и их распределение слов
for topic_id, topic_words in lda_model.print_topics():
    # pass
    print(f"Topic {topic_id}: {topic_words}", '<<<<<<<<<<<<<<<<<')


# Печатаем распределение тем для каждого документа
for doc_id, doc_topics in enumerate(lda_model[corpus]):
    pass
    # print(f"Document {doc_id}: {doc_topics}")



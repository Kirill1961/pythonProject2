from gensim import corpora, models
import numpy as np
import re
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import random



def fix_unicode(text):
    return text.replace(u"\u2019", "'")  # изменение кодировки

url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"  # сохраняем сайт в переменную
html = requests.get(url).text  # requests.get - запрос сайта по адресу из переменной url, .text - очистка от тегов и тд
soup = BeautifulSoup(html, 'html5lib')  # 'html5lib' - формат возвращаемого текста из переменной html

content = soup.find("div", "entry-content")  #
regex = r"[\w']+|[\.]"  # re выбирает слова из тега "div" класса "entry-content"

document_radar = []


for paragraph in content("p"):  # извлекаем текст с тегом <р> из ("div", "entry-content")
    words = re.findall(regex, fix_unicode(paragraph.text))  # отбор с помощью re слов
    document_radar.extend(words)
    # print(document_radar)


# documents = [document_radar]
# Предположим, у вас есть некоторые текстовые документы
# documents = [
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
    print(f"Topic {topic_id}: {topic_words}")


# Печатаем распределение тем для каждого документа
for doc_id, doc_topics in enumerate(lda_model[corpus]):
    pass
    # print(f"Document {doc_id}: {doc_topics}")



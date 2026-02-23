""" Генератор списков - формируется в квадратных скобках [ ]. выражение-генератор формируется в круглых скобках ( )
    генератор списков создает в памяти список результатов, который можно многократно получить или вывести и пока
     генератор списков не произведёт все действия код выполняться не будет.
     Выражение-генератор возвращает данные по мере их создания, извлекает по одному элементу из последовательности
     пока не закончится вся коллекция"""
from threading import Thread
from time import sleep
""" Своими словами - list generator сначала полностью переберёт и вычислит все значения переменной "х"
    в [] скобках, сохранит все значения переменной "х" в памяти а затем результат 
    подставит в итерируемую переменную"""
for p in [x * 3 for x in (1, 2, 3, 4, 5)]:
    print(p)
""" Своими словами - generator expression вытаскивает по одному вычисленному значению переменной "х" 
    из () скобок и подставляет в итерируемую переменную, те в памяти весь результат не хранится."""

for d in (x * 3 for x in (1, 2, 3, 4, 5)):
    print(d)

""" Библиотека requests является нестандартной и устанавливается следующей командой:
    pip install requests, В библиотеке requests функции для формирования HTTP-запросов называются так же,
    как и сами запросы. Например, для выполнения GET-запроса используем функцию get().
    content - атрибутДля получения данных из ответа сервера 
    Response.content -  возвращает содержание ответа сервера, представленное в байтах, размер страницы
    response.status_code - возвращает номер, указывающий на состояние (200 в порядке, 404 не найдено)"""

import requests
from requests import get

""" resp - это объект библиотеки requests, создаём объект resp для GET-запроса по нужному URL,
   в дальнейшем будем перебирать URL адреса , делать по ним запрос requests.get()  и размещать результат 
   в ОБ resp"""

resp = requests.get('http://headfirstlabs.com')
print(resp.status_code, '****')

""" ___________________________________Генератор
   Перебираем коллекцию urls в variable url и делаем GET-запрос перебираемых url
   с помощью метода get(url) из модуля requests"""

urls = ('http://headfirstlabs.com', 'http://twitter.com', 'https://www.oreilly.com/')
for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), resp.status_code, resp.url)

""" ______________________generator expression
    Перебираем коллекцию urls в variable url и делаем GET-запрос перебираемых url
    с помощью метода get(url) из модуля requests"""

urls = ('http://headfirstlabs.com', 'http://twitter.com', 'https://www.oreilly.com/')
for resp in (requests.get(url) for url in urls):
    print(len(resp.content), resp.status_code, resp.url)

""" В А Ж Н О! generator expression - можно встраивать в ф-цию.
    Создадим ф-цию которая инкапсулирует generator expression и используем его """


def gen_req_ex(urls):
    return (requests.get(url) for url in urls)


for resp in gen_req_ex(urls):
    print(len(resp.content), resp.status_code, resp.url)

""" Другой вариант - поместить значения перебираемые из ф-ции gen_req_ex (urls) 
    в ТРИ переменные: s , d , f, тк yield возвращает три значения а затем их вывести. 
    Используем yield. Результат будет без скобок"""


def gen_req_ex(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield (len(resp.content), resp.status_code, resp.url)


for s, d, f in (gen_req_ex(urls)):
    print(s, d, f, '|/|/')

''' Если результат выводить через одну переменную, то выйдет кортеж'''
for k in (gen_req_ex(urls)):
    print(k, '///')

t = Thread(target=gen_req_ex, args=[urls])
t.start()
""" Например аналог генератора в виде цикла for работать в ф-ции не будет """

# def gen_req_ex (ur_ls):
#     for url in ur_ls:
#         reg_url = requests.get(url)
#         return reg_url
# for resp in gen_req_ex (ur_ls):
#     print(resp)


""" Функция get() вернула ответ HTTP-сервера с кодом 200. Значит, запрос был обработан успешно."""

response = get("https://static-maps.yandex.ru/1.x/?"
               "ll=37.677751,55.757718&"
               "spn=0.016457,0.00619&"
               "l=map")
print(response)

"""_________________Вывод словаря_____________________________________"""


def gen_req_ex(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield resp.url, [len(resp.content), resp.status_code, ]


print({k: v for k, v in (gen_req_ex(urls))})

def gen_req_ex(urls):

    # print('Cirill', 111)
    sleep(3)
    for resp in [requests.get(url) for url in urls]:
        print(len(resp.content), resp.status_code, resp.url)
    print('Cirill', 222)

""" Помещаем ф-цию gen_req_ex(urls) в экземпляр " t " класса Thread, 
    тем самым размещаем в паралельном потоке с запросом  requests.get
     Задержка работы ф-ции gen_req_ex(urls) на 3 сек обеспечивает sleep(3)"""

t = Thread(target=gen_req_ex, args=[urls])
t.start()

resp = requests.get('http://headfirstlabs.com')
print(resp.status_code,'END CODE', '****')
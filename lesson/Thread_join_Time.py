""" класс Thread из модуля threading, выполнение частей кода
в разных потоках, ф-ция threa_d выводит два сообщ:
 первая часть кода - 111 и с задержкой n секунд - 222
 вторая часть кода - в глобальной области код для вывода 333
вывод 111(из 1 й части) и 333(из 2 й части) производится одновременно, тк Thread
взял управление ф-й threa_d, в 1-й части кода, на себя и создал для неё паралельный поток.
Вывод 333 выполняется первым тк в глобальной зоне.
222 с задержкой на n секунд хотя очередь исполнения раньше
чем 333 тк находится в теле ф-ции threa_d"""
import requests
from threading import Thread
from time import sleep

""" Форматирование: print('{} 222'.format(name)), в  {} вставляется 
отформатированный в str объект, точка "." соединяет строку 
куда закидывает ф-я format строчный объект
print(f'333,{12}') ещё вариант форматирования в str"""
def threa_d(n, name):
    print('{} 111.'.format(name), end=' ')
    sleep(n)
    print('{} 222'.format(name))

""" создаём объект класса Thread, именуем "t", два обязательных аргумента:
target - имя объекта функции без скобок и args - аргументы ф-ции threa_d
для запуска в паралели используем ф-ю start()"""
t = Thread(target=threa_d, args=(3, 'Cirill'))
t.start()
print('Cirill {} '.format(333))


urls = ('http://twitter.com', 'http://headfirstlabs.com', 'https://www.oreilly.com/')

def gen_req_ex(urls):

    print('Cirill - is a good programmer ?')
    sleep(2)
    for resp in (requests.get(url) for url in urls):
        print(len(resp.content), resp.status_code, resp.url)
    print('Cirill good programmer')

""" Помещаем ф-цию gen_req_ex(urls) в экземпляр " t " класса Thread, 
    тем самым размещаем в паралельном потоке с запросом  requests.get
     Задержка работы ф-ции gen_req_ex(urls) на 3 сек обеспечивает sleep(3)"""

# gen_req_ex(urls)
time = Thread(target=gen_req_ex, args=[urls])
time.start()

resp = requests.get('http://headfirstlabs.com')
print(resp.status_code,'END CODE', '****')
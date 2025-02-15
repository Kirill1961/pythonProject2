"""
Yield – ключевое слово, которое используется вместо return.
С его помощью функция возвращает значение без уничтожения локальных переменных,
кроме того, при каждом последующем вызове функция начинает своё выполнение с оператора yield.
Генератор — это обычная функция, которая при каждом своём
вызове возвращает объект. При этом в функции-генераторе вызывается next.
Отличие генераторов от обычной функции состоит в том, что функция
возвращает только одно значение и один раз с помощью ключевого слова return,
а генератор возвращает новый объект при каждом вызове с помощью yield.
По сути генератор ведет себя как итератор,
что позволяет использовать его в цикле for.
yield используется в функциях так же, как и return – для возвращения результата работы.
Разница заключается в том, что yield возвращает генератор.
главная особенность yield: при вызове функции код в теле функции не исполняется.
Функция просто возвращает объект-генератор. Код вызывается каждый раз,
когда for обращается к генератору. При первом запуске функции она будет исполняться,
пока не дойдет до yield, после чего вернет первое значение из цикла.
При каждом последующем вызове будет происходить следующая итерация и возвращение значения цикла.
Процесс будет повторяться, пока генератор не окажется пустым.
Генератор считается пустым, если функция не встречает yield –
это происходит либо в конце цикла, либо при невыполнении условий if и else
ещё
В первый запуск вашей функции, она будет исполняться от начала до того момента,
когда она наткнётся на yield — тогда она вернёт первое значение из цикла.
На каждый следующий вызов будет происходить ещё одна итерация написанного вами цикла,
возвращаться будет следующее значение — и так пока значения не кончатся."""
from itertools import islice

def count_up(n):
    while n != 10:
        yield n
        n += 1


# ex = count_up(-1)
# # print(next(ex))
# # print(next(ex))
# # print(next(ex))
#
for i in count_up(-1):
    print(i, ' 1111111')


# # /////////////////
# def count_for(k, s, g):
#     for fi in range(k, s, g):
#         yield fi
#
#
# g_f = count_for(5, 0, -1)
# print(next(g_f))
# print(next(g_f))
# print(next(g_f))
# print(next(g_f))
# print(next(g_f))

#
# for ig in range(10, 5, -1):
#     print(( ig ))

__doc__ = """ generator in generator / subgenerstor"""
#
# def sub_generator():
#     yield 'Kirill'
#     yield 'okokokokokokokok'
# def generator ():
#     yield 'good'
#     yield from sub_generator()
#     yield 'programmer'
# for i_gen in generator():
#     print (i_gen, end=' ')


__doc__ = """ klassik generator """
#
# def count_up(n):
#     res = []
#     while n != 10:
#         res.append(n)
#         n+=1
#     return (res)
# print( count_up(1))
#
# def count_for(k):
#     for fi in range(k):
#         yield fi + 1
# g = count_for(5)
# for ig in g:
#     print((ig))
#
# def prober():
#     print ('prober')
# prober()

def cr_gen():
    my_l = [1, 2, 3]
    for mg in my_l:
        # print(mg_i)
        yield mg * 2, mg ** 2  # # как только код дошёл до yield происходит обращение циклу "for cr_l in cr_gen():"
        # #  после этого из цикла происходит обращение к cr_gen()


for cr_l in cr_gen():
    print(cr_l)
print(type(cr_gen()))


#
# def cr_gen():
#     my_l = [1,2,3]
#     for mg in my_l:
#         # print(mg_i)
#         yield mg*2, mg**2
# m_gen = cr_gen()
# print(m_gen)
# for cr_l in m_gen:
#     print(cr_l)


__doc__ = """Цикл в Цикле"""
def f():
    n = 0
    while n < 2:
        n += 1
        m = 0
        while m < 10:
            m += 1
            yield m


for i in f():
    print(i, " Цикл в Цикле")


__doc__ = '''По условию отсекаем часть (0,5) генерируемых значений'''
def f():
    n = 0
    while n < 2:
        n += 1
        m = 0
        while m < 10:
            m += 1
            if m <= 5:
                yield m
for i in f():
    print(i, " По условию отсекаем часть (0,5) генерируемых значений")


def cr_gen(x, y):
    c = x + y
    yield (c)


# for i in cr_gen(5, 6):
#     print(i)
# print(cr_gen(2, 3))

import requests

urls = ('http://headfirstlabs.com', 'http://twitter.com', 'https://www.oreilly.com/')

__doc__ = """ Другой вариант - поместить значения перебираемые из ф-ции gen_req_ex (urls)
    в ТРИ переменные: s , d , f, тк yield возвращает три значения а затем их вывести.
    Используем yield. Результат будет без скобок"""


def gen_req_ex(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield (len(resp.content), resp.status_code, resp.url)


# for s, d, f in (gen_req_ex(urls)):
#     print(s, d, f, '|/|/')

__doc__ = """Если результат выводить через одну переменную, то выйдет кортеж"""
# for k in (gen_req_ex(urls)):
#     print(k, '///')

__doc__ = """_________________Вывод словаря_____________________________________"""


def gen_req_ex(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield {len(resp.content): [resp.status_code, resp.url]}


# for k in (gen_req_ex(urls)):
#     print(k, '///')


__doc__ = 'три подряд yield выполняются поочерёдно'
def foo(x):
    while True:
        x += 1
        # print(x)
        yield x         # первое действие
        yield x * 10    # второе действие
        yield x + 50    # третье действие
        # print(x, "x2")
f = foo(1)
res = [next(f) for _ in range(3)]
print(f"выполненые три действия: {res}")


__doc__ = ''' Бесконечный Счётчик '''
def foo(x):
    while True:
        x += 1
        yield x


f = foo(0)
print(f'Бесконечный Счётчик № {next(f)}')
print(f'Бесконечный Счётчик № {next(f)}')
print(f'Бесконечный Счётчик № {next(f)}')
print(f'И ещё № {[next(f) for _ in range(2)]}')


__doc__ = '''Разворачивание значений генератора'''


# 1-й Вариант на прямую
def foo(x):
    while True:
        x = 2
        yield x


f = foo(2)
# next(f)

one, two, three = next(f), next(f), next(f)
print(f'Вызов третьего значения: {three}')


# 2-й Вариант через list
def foo(x):
    while True:
        x = 2
        yield x

f = foo(2)

one, two, three = [next(f) for _ in range(3)]
print(f'Вызов второго значения: {two}')

# 3-й Вариант через list
f = foo(2)
one, two, three = islice(f, 3)
print(f'Для контроля количества значений: {one, two, three}')

__doc__ = '''Менеджер управлением вызова функций'''


def foo1():
    return 'функция foo1'


def foo2():
    return 'функция foo2'


def foo():
    while True:
        yield foo1()
        yield foo2()


f = foo()

a, b = next(f), next(f)
print(f'Вызов {a}')
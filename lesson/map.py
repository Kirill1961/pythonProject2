import random


""" если есть какой-то список list,tupl,dict и тд и какая-то функция fun то
 map() может применить эту функцию ко всем элементам списка,
  а то, что будет возвращать функция - записывать в новый список.
map применяет какую-либо функцию к каждому элементу списка своих аргументов,
 выдавая список результатов как возвращаемое значение. """
# item1 |       |     |      | func(item1) |
# item2 |       |     |      | func(item2) |
# ..... | ----> | map |      | ..........  |
# item n|       |     | ---->| func(item n)|
#               |     |      |             |
# func  | ----> |     |      |             |

my_list = ['one', 'two']


def up(string):
    return string.upper()


me_my_li = map(up, my_list)
for i_str in me_my_li:
    print(i_str, '  Перевод строчного ОБ в верхний регистр ')

l_ist = [11, 22, 33]


def dub_lis(x):
    return x * 2


my_map = map(dub_lis, l_ist)
for ite_r in my_map:
    print(ite_r, "умножение элементов списка x * 2")
# print(next(my_map), "умножение элементов списка x * 2")
# print(next(my_map), "умножение элементов списка x * 2")
# print(next(my_map), "умножение элементов списка x * 2")


""" эквивалент ф-ции map, с помощью цикла for
передаём значения из списка в ф-цию int или в любую другую ф-цию"""

lis_str = ['1', '5', '9']
a = (int(x) for x in lis_str)
print(list(a),'////')

m_ap = map(type, ['1', '5', '9'])
for ilis in m_ap:
    print(ilis, '||||')


my_set_one = {'one', 'two', 'three'}
my_set_two = {'for', 'five'}


def un_set(*args):
    return my_set_one.union(my_set_two)


sum_set = map(un_set, my_set_one, my_set_two)
# print(un_set(my_set_one,my_set_two))
print(next(sum_set), " слияние множеств")
for i_sum in sum_set:
    print(i_sum, " слияние множеств")

lis_str = ['2', '6', '1', '8']
a_lis = map(int, lis_str)
print(next(a_lis))
print(next(a_lis))

""" разбивка на списки со str значениями состоящих из букв"""
town = ['Moscow', 'Murmansk', 'Voroneg']
a_len = map(list, town)
for i_t in a_len:
    print(i_t, " разбивка на списки со str значениями")


""" кол-во символов значениях"""
town = ['Moscow', 'Murmansk', 'Voroneg']
a_len = map(len, town)
for i_t in a_len:
    print(i_t)

""" вывод в верхнем регистре"""
town = ['Moscow', 'Murmansk', 'Voroneg']
a_len = map(str.upper, town)
for i_t in a_len:
    print(i_t)

""" через созданную ф-цию выводим нижний регистр"""
town = ['Moscow', 'Murmansk', 'Voroneg']
def low(l):
    return list(l.lower())
wr_res = map(low,town)
# print(next(wr_res))
# print(next(wr_res))
# print(next(wr_res))
wr_lis = list(wr_res)
print(wr_lis, " через созданную ф-цию выводим нижний регистр")

""" через созданную ф-цию выводим нижний регистр
с помощью lambda"""
# def low(l):
#     return list(l.lower())
wr_res = map(lambda l: list(l.lower()) ,town)
wr_lis = list(wr_res)
print(wr_lis, " нижний регистр с помощью lambda ")

""" через созданную ф-цию выводим нижний регистр
с помощью lambda в обратном порядке"""
wr_res = map(lambda l: l[::-1] ,town)
wr_lis = list(wr_res)
print(wr_lis)
#
# """ ввод через input с помощью map"""
# key_a = map(int,input().split())
# key_wr = list(key_a)
# print(key_wr)
a = [9,8,7]
def app_end(a):
    sortlist = []
    sortlist.append(a)
    # print(sortlist, '  sortlist')
    return sortlist
app = map(app_end, a)
for i in app:
    print(i, '   app_endapp_endapp_end')
# app_end([9,8,7])

# Поэлементное сложение 2х списков

u=[20,30,50]
i = [1,2,100]
print([x for x in map(sum, zip(i, u)) ], " Поэлементное сложение 2х списков")


# Маркировка ОБ по условию
v =  [5, 10, 3, 8, 12, 7]
print(list(map(lambda x : 1 if x > 5 else 0, v)), "Маркировка ОБ по условию")


# Ещё Поэлементное сложение 2х списков

# Поэлементное сложение 2х списков
a, b, c = [1, 2], [3, 4], [5, 6]
result = list(map(sum, zip(a, b, c)))
print(result, " list(map(sum, zip(a, b, c)) Поэлементное сложение 2х списков")


# Поиндексное действие П Р О С Т О
c = [10, 20, 30, 40]
b = [2, 2, 2, 2]
print(list(map(lambda x_f, e_r_f:  e_r_f * x_f, c, b)), " Поиндексное действие П Р О С Т О")


#  Генерация LIST разной длинны из заданного LIST
a = [14, 8, 0, 16, 11, 16, 1, 0, 18, 1, 0, 2, 18, 5, 1, 19, 13, 10, 5, 20, 15, 2, 19, 1, 8]
print(list(map(lambda i: [a[r: (r + i)] for r in range(0, 25, i)],
               [random.randint(2, 5) for i in range(5)])), "Генерация LIST разной длинны из заданного LIST")


# Len вложенных списков
l = [
    ['numpy', 'decision trees', 'libsvm', 'probability'],
    ['statistic', 'R', 'go', 'scipy', 'numpy', 'machine learning'],
    ['Python', 'Hadoop', 'numpy']
     ]

print(list(map(len, l)), "Len вложенных списков")

if __name__ == "__mane__":
    print('UNPACK')


# map - применяет через lambda - max к value словаря но выводит ключи
dict = {1: {"a": 20, "b": 1, "c": 1000, "d": -5},
2: {"a": 555, "b": 10, "c": -33, "d": 77},
3: {"a": 0.01, "b": 17, "c": 0, "d": 840}}

res = map(lambda x: max(x, key=x.get), dict.values())
print(list(res), "map - применяет через lambda - max к value словаря но выводит ключи")
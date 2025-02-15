import random
import pandas as pd

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

m_ap = map(type, ['1', 5, '9'])
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


# Поэлементное умножение 2х списков
print(list(map(lambda x, y: x * y, u, i)), 'Поэлементное умножение/вычитание/ и тд 2х списков')

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

# Вывод ключа с мах значением value словаря с вложенными словарями
# map - применяет через lambda - max к value словаря но выводит ключи
dict = {1: {"a": 20, "b": 1, "c": 1000, "d": -5},
2: {"a": 555, "b": 10, "c": -33, "d": 77},
3: {"a": 0.01, "b": 17, "c": 0, "d": 840}}

# dict = {"a": 0.01, "b": 17, "c": 0, "d": 840}

res = map(lambda x: max(x, key=x.get), dict.values())
print(list(res), "map - применяет через"
                 " lambda - max к value словаря но выводит ключи")

# Вывод ключа  с мах значением value простого словаря
dict = {"a": 20, "b": 1, "c": 1000, "d": -5}
print(f"Ключ с мах значением value: {max(dict, key=dict.get)}")


# Добавляем столбец со значениями из словаря category_map, к имеющемуся столбцу  "Category"
__doc__ = '''Создали DF со столбцом "Category"'''
df = pd.DataFrame({"Category": ["A", "B", "C", "A", "D"]})

# Задаём соответствие категорий и чисел
__doc__ = '''Задаём values для значений из "Category"'''
category_map = {"A": 100, "B": 200, "C": 300}

# Применяем PANDAS MAP,
__doc__ = '''Создаём столбец "Mapped" в котором отображены values для соответствующих значений из "Category"'''
df["Mapped"] = df["Category"].map(category_map)
print(df)



# Подсчёт Пропусков через сравнивание столбцов из DF c их средними из группировки
import pandas as pd

df11 = pd.DataFrame({
    "A": [2, 2, 3, 2, 3],
    "B": [10, 20, pd.NA, 40, 50],
    "C": [pd.NA, 200, 300, 400, pd.NA]
})

# Среднее столбцов по сгруппированному 'A'
group_mean = df11.groupby(['A']).mean()
print(group_mean, '\n')

# Копирем и изменяем копию
df11_cp = df11.copy()


__doc__ = '''
* Через  df11[col] -> прокручиваем столбцы
* df11['A'].map(mean[col]) -> Заменяет значения в столбце 'A' на средние значения остальных столбцов из group_mean
* df11[col] != df11['A'].map(group_mean[col]) -> Сравниваем оригинальные столбцы  из DF и их Средние из group_mean
'''
for col in df11.columns[1:]:

    avrg = df11['A'].map(group_mean[col])  # Замена значений в столбце 'A' на средние значения остальных столбцов из group_mean
    column_df = df11[col]  # Столбец оригинальный из DF

    df11_cp['NEW'+'_' + col] = column_df != avrg  # Сравниваем оригинальные столбцы  из DF и их Средние из group_mean

    print(df11[col], avrg, '\n') # Для информации о процессе вывели оригинальные столбцы  из DF и их Средние из group_mean
print(df11_cp, '\n')

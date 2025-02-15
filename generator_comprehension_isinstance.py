""" Генератор списков или Списочное включение или list comprehension смысел в том что ставим всё выражение в [ ] вместо
    метода append тем самым уменьшаем ко-во строк кода, генератор вызывает append автоматически,
    то же самое можно делать со словарями"""
import random
from functools import reduce
import random as rn

ls1 = [1, 2000, "john", 3, "a", "bob"]
ls2 = [(y, x) for x in ls1 for y in [ls1.index(x)]]
ls3 = {k: v for k, v in ls2}
print(ls3, " ls3 ls3l s3l s3l s3")
print(ls3[2], " ls3[2] ls3[2] ls3[2]")
print(ls2, " ls2 ls2 ls2 ls2 ls2")
tp = ("id", "fo")
r = [l for l in tp]
print(r)

dict_for_iter = {
    "js": 14,
    "av": 1,
    "bh": 5,
    "fp": -3,
}

""" ___________________Генератор списков, Запись в list key и value из словаря"""

list_t = []
for i_l in dict_for_iter.keys():
    list_t.append(i_l)
print(list_t)

""" ___________________то же самое только с list comprehension"""

list_key = [i_l.title() for i_l in dict_for_iter.keys()]
print(list_key, "то же самое только с list comprehension")

""" _______________Генератор словарей, преобразовав старый /dict_for_iter/ получаем новый словарь
    key  из прежнего словаря преобразовали с title(), а value увеличили на 100 """

dict_dif = {kd.title(): vd + 100 for kd, vd in dict_for_iter.items()}
print(
    (dict_dif),
    "получаем новый словарь key  из "
    "прежнего словаря преобразовали с title(), а value увеличили на 100",
)

""" ___________Расширенные генераторы с фильтрами , условие if. 
     Данный генератор обрабатывает только value > 0  """

dict_dif = {kd.title(): vd + 100 for kd, vd in dict_for_iter.items() if vd > 0}
print((dict_dif, "Данный генератор обрабатывает только value > 0"))

from operator import itemgetter

ps = [(2, 4), (-1, 7), (4, 5), (3, -4), (-1, -5)]
got = itemgetter(0, 2, 3)(ps)

print(got, "itemgetter, вывод из списка по индексу")

# Объединение пар в общий список

list_pair = [i if r == 0 else k for i, k in ps for r in range(2)]
print(list_pair, " Объединение пар в общий список")

# Операции между LIST и LIST[LIST], умножить ОБ из b  на ОБ из LIST[LIST] поиндексно

x = [[10, 20, 30, 40], [50, 60, 70, 80]]  # вложенные LIST[LIST]
b = [2, 2, 2, 2]

j = map(
    lambda k: [[j * k for j in i] for i in x], b
)  # lambda вытаскивает  из вложенных LIST поиндексно все ОБ
print(next(j), " next(j) выводит одну итерацию")

# срезом [0:len(x)], берём 1-ю итерацию
print(
    [[j * v for j in i] for v in b for i in x][0 : len(x)],
    " срезом [0:len(x)], берём 1-ю итерацию ",
)

# Объединение двойных вложенных списков LIST[LIST]
a = [[1, 2, 3], [4, 5, 6]]
print(
    list(j for i in a for j in i),
    "Объединение двойных вложенных списков LIST[LIST] в [LIST]",
    "\n",
)

# Объединение тройных  вложенных списков LIST[LIST[LIST]]
r = [[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1]], [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]]
triple = [[x for k in j for x in k] for j in r]
print(
    triple,
    " Объединение тройных  вложенных списков LIST[LIST[LIST]] в LIST[LIST]",
    "\n",
)

# Перемножение, сложение, и тд с LC , lambda, reduce. Списки с разным len
print(
    [
        [reduce(lambda x, y: x * y, (m)) for m in list(i)]
        for i in list(map(lambda y: zip(y, b), x))
    ],
    " Перемножение, сложение, и тд с LC , lambda, " "reduce. Списки с разным len",
    "\n",
)

#  Почленное умножение списков
print(
    [i[0] * i[1] for i in list(zip([2, 5], [3, 10]))],
    " Почленное умножение списков [2,5], [3,10]",
    "\n",
)
print(" или", "\n")
print(
    [i * j for i, j in list(zip([100, 5], [3, 100]))],
    " Почленное умножение списков [100,5], [3,100]",
    "\n",
)

# Запись из первого списка во второй со стиранием первого списка
a = [1, 2]
b = [3, 4]
a.clear(), [a.append(i) for i in b]
print(
    " Запись из списка b=[3, 4] в список a=[1, 2] со стиранием   списка а;",
    "a=",
    a,
    "b=",
    b,
    "\n",
)

#  Фильтр списка по заданным параметрам, здесь по первому префексу строчного ОБ
a = ["Asdf", "Sddf", "Sdre", "Gerty"]
print(
    [i for i in a if i.startswith("G")],
    "Фильтр списка по заданным параметрам, " "здесь по первому префексу строчного ОБ",
    "\n",
)

# Генерация LIST[LIST] разной длинны
a = [[rn.random() for i in range(5)] for _ in range(2)]
b = [[rn.random() for i in range(5)] for _ in range(1)]
c = [a, b]
print(c, "Генерация LIST[LIST] разной длинны", "\n")

# zip с LIST  разной длинны
b = [[10], [20]]
a = [[1], [2], [3]]
print(
    [[i * j for i, j in zip(a[k], b[k])] for k, _ in enumerate(b)],
    " zip с LIST  разной длинны",
    "\n",
)

# K-Means - sort ОБ принадлежащих кластерам по индексам кластеров
a = [2, 1, 1, 0, 2, 1, 1, 0, 1, 1, 1]  # индексы кластеров
b = [2, 17, 19, 4, 1, 37, 18, 3, 15, 31, 29]  # iputs ОБ
k = 3  # заданное кол-во кластеров

print(
    [[p for p, t in zip(b, a) if t == i] for i in range(k)],
    "K-Means - sort ОБ принадлежащих " "кластерам по индексам кластеров",
    "\n",
)

# Разбить список на пары или др кол-во, comprehension срезов
d = [-49, 0, -49, 15, -46, 5, -41, 8, -34, -1]
print(
    [d[j : 2 + j] for j in range(0, 10, 2)],
    " Разбить список на пары или др кол-во",
    "\n",
)

# Простая маркировка  значений из списка: 1, если значение больше 5, иначе 0
values = [5, 10, 3, 8, 12, 7]
labels = [1 if value > 5 else 0 for value in values]
print(labels, "Простая маркировка  значений из списка", "\n")

# Генерация из заданного LIST в LIST разной длинны и в случайной последовательности
a = [
    14,
    8,
    0,
    16,
    11,
    16,
    1,
    0,
    18,
    1,
    0,
    2,
    18,
    5,
    1,
    19,
    13,
    10,
    5,
    20,
    15,
    2,
    19,
    1,
    8,
]


def generation_list_different_len(chunk_size):
    d = list(
        map(
            lambda i: [a[r : (r + i)] for r in range(0, len(a), i)],
            [rn.randint(2, 5) for i in range(chunk_size)],
        )
    )
    c = [i for j in d for i in j]
    rn.shuffle(c)
    return c


print(
    generation_list_different_len(5),
    "Генерация  из заданного LIST - "
    "LIST разной длинны и в случайной последовательности",
    "\n",
)

#  Генерация LIST [LIST] разной длинны вложенных списков
list_nested = [[random.randint(3, 20) for _ in range(random.randint(2, 6))] for _ in range(5)]
print(f"Генерация LIST [LIST] разной длинны вложенных списков: {list_nested}")

# Замена числа в list без изменения len
# Исходный список
my_list = [1, 2, 3, 4, 5]

# Замена числа 3 на 10
my_list[2] = 10

print(my_list, "Замена числа в list без изменения len", "\n")

# Создание всех вариантов пар из списка
print(
    [(i, j) for i in range(5) for j in range(5)],
    "Создание всех вариантов пар из списка",
    "\n",
)

# Список преобразуем в pairs in tuple (индекс,, значение), полезная штучка
x = ["a", "b", "c"]
print(
    [(j, i) for i in x for j in [x.index(i)]],
    " Список преобр. в pairs in tuple (индекс,, значение)",
    "\n",
)
print(
    [(j, i) for i in x for j in [rn.randint(1, 10)]],
    " Список преобр. в pairs in tuple (random_ind, value)",
    "\n",
)


# isinstance(x, str) - определение и фильтрация по типу данных
list_2 = [22, "qwer", True, "asdf", 77, False, True]
print(
    [x for x in list_2 if isinstance(x, bool)],
    " --> isinstance определение и фильтрация по типу данных",
    "\n",
)

# условие в левой части генератора только вместе с else, в правой одно if
numbers = [1, 2, 3, 4, 5, 6]
modified_numbers = [x**2 if x % 2 == 0 else x for x in numbers if x > 2]
print(modified_numbers, "условие в левой части генератора только вместе с else, в правой одно if",
    "\n")

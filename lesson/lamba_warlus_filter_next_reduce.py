import random
import numpy as np
from functools import reduce
from collections import defaultdict
import os


counts = defaultdict(lambda: [1, 1])  # lambda передаёт в созданный словарь величину [1, 1]
counts["asdf"].append(555)
print(counts, " величине [1, 1] в созданном словаре присвоили key - asdf и добавили величину 555")


def fuf(x, y):
    return x / y


print(fuf(4, 2))

""" ф-ция fuf запишется в виде лямбда ф-ции
 вот так, можно присвоить переменную w и вызывать w с аргументами,
  после двоеточия пишем тело ф-ции"""
w = lambda x, y: x / y
print(w(2, 4))

""" аргументы можно записывать в конце строки,
но в скобки отдельно ставим ф-цию с телом и аргументы ,
в этом случае переменную ф-ции вызываем без арг"""
a = (lambda x, y: x * y)(4, 5)
print(a)

""" аргументов можно любое кол-во"""

hellow = lambda name: ('Hi ' + name + ' !')
print(hellow('Kirill'))

# Умножение, сложение и тд значений в кортеже

print((lambda x, y: x * y)(2, 10), " Kirill")
print((lambda x, y, z: x * y * z)(2, 10, 2))
print((lambda x, y, z: x + y * z)(2, 10, 2))
print((lambda x, y, z: x - y * z)(2, 10, 2))

# Сортируем по 1-му индексу кортежей или по любому другому

list_1 = [('Антон', '22', '180'), ('Joe', '45', '174'), ('Dob', '13', '192')]
list_1.sort(key=lambda x: x[1])  # Сортируем по 1-му индексу кортежей или по любому другому
print(list_1, ' Сортируем по 1-му индексу кортежей или по любому другому')

# lambda Без аргументов
x = lambda: [0, 0]
z = x()  # приравниваем lambda к переменной и работаем с содержимым тела
z.append(555)
print(x(), ' lambda Без аргументов')  # если " х " вызываем со скобками ты выводится содержимое тела ф-ции
print(z, ' append(555)')

""" Сортировка с помощью lambda ф-ции, в переменную ite_m
 поочерёдно передаются пары из dict в виде кортежа
 например первая пара ('a', 2), цифра в [ ] это индекс,
 если 0 то sorted по key, если 1 то по value,
 в конце список кортежей трансформ в словарь,
 sorted в обратном порядке с пощ ф - ции reversed """

dict_lamb = {'a': 2, 'j': 0, 'g': 9, 'b': 5}
sort_lamb = dict(reversed(sorted(dict_lamb.items(), key=lambda ite_m: ite_m[1])))
print(sort_lamb, " в переменную ite_m поочерёдно передаются пары из dict в виде кортежа")

# Случайный выбор значения из списка с помощью random.choice([x1, x2 ... xn ])

x = lambda: [random.choice([1, 0]) for i in range(5)]
print(x(), " random.choice")

# выполнение действия lambda при вызове элемента из списка с индексом 2
a = [2, 4, lambda: print(" lambda как элемент списка а"), 10, 1]
print(a, "список с ф-цией lambda")

# выполнение lambda из списка а
a[2]()

# Использование  lambda в фильтре при отборе чётных значений

v = [2, 3, -14, 10, 1, -5, 48]


def get_filter(w, filter=None):  # filter это lambda x: x%2 == 0
    if filter is None:
        return a
    res = []
    for x in w:
        if filter(x):
            res.append(x)
    return res


r = get_filter(v, lambda x: x % 2 == 0)  # lambda передаём в filter
print(r, " lambda в фильтре при отборе чётных значений")

# lambda vs map
lm = [i for i in map(lambda x: x ** 2, v)]
print(lm, " lambda vs map")

# Фу-ция filter, возвращает значения прописаные по условиям фильтрации - чётные и < нуля
fi_lter = [i for i in filter(lambda x: x % 2 == 0, v)]
fil_ter = [i for i in filter(lambda x: x < 0, v)]
print(fi_lter, fil_ter, " определяем значения чётные и < нуля")

# Значения из списка " а " передаются в lambda x: x*-1
# и производим sort значений после умножения на -1.

a = [2, 51, 14, 142, 17, 89, -1, -7]
a.sort(key=lambda x: x * -1)
print(a, " производим sort значений по возрастанию после умножения на -1")

#  Сортируем список кортежей по индексу ОБ кортежа
f = [(2, 3, 21), (-14, 10, 2), (1, -5, 17), (-67, 0, 12), (15, 1, 33), (0.5, -9, 77)]
f.sort(key=lambda row: row[1])
print(f, " Сортируем список кортежей по индексу ОБ кортежа")

# СРЕЗЫ
f = [(2, 3, 21), (-14, 10, 2), (1, -5, 17), (-67, 0, 12), (15, 1, 33), (0.5, -9, 77)]
print([i for i in filter(lambda row: row, f)][-1:], " СРЕЗЫ последняя кроме всех")
print([i for i in filter(lambda row: row, f)][:-1], " СРЕЗЫ все кроме последней")
print([i for i in filter(lambda row: row, f)][-4:], " СРЕЗЫ последние 4 значения")
print([i for i in filter(lambda row: row, f)][:-2], " СРЕЗЫ все кроме 2x последних")

# фильтр с  not / in, фильтрация булевых типов данных  True / False, индексы:row[2] - кортежи / [:-1] - списка кортежей
f = [(2, 3, True), (-14, False, False), (1, False, 17), (9, 17, False), (-87, 5, False), (44, False, 3)]
# f = [(2, 3, True), (-14, True, 2), (1, True, 17), (9, 17, True), (-87, 5,  True), (44, False, 3)]
print([i for i in filter(lambda row: not row[1], f)][:], " фильтрация булевых типов данных  True / False")
print([i for i in filter(lambda row: row, f)][-4:], " та же конструкция но весь список f", "\n")
p = [k for k in filter(lambda row: not row[1], f)][:]
print(p, "\n")


# Фильтрация по типу данных
list_1 = [11, "qwer", True, "asdf", False, 555]
res_filrt = filter(lambda x: type(x) == bool, list_1)
print("\t" * 5, list(res_filrt), "Фильтрация по типу данных", "\n")



# Оператор Морж / Warlus

def func(x):
    return x * 100


result = [func(100), func(100) ** 2, func(100) ** 3]  # func() вызывается три раза

result_warlus = (w := func(100), w ** 2, w ** 3)  # func() вызывается один раз и записывается в переменную w

result_lambda = lambda y: y

print(result, " result", "\n")
print(result_warlus, "   :=  result_warlus,", "\n")

print(result_lambda([v := func(200), v ** 2, v ** 3]), " result_lambda со своим аргументом", "\n")
print(result_lambda(result), " result_lambda с аргументом для func(x): ", "\n")

# Списковое включение с Морж / Warlus
data = [11, 22, 33]

res_func = [func(x) for x in data]  # прокручиваем data через func(x), func() вызывается три раза

res_y_func = [y for x in data if (y := func(x))]  # func() вызывается один раз и записывается в переменную y

print(res_func, " res_func", "\n")
print(res_y_func, " res_y_func", "\n")

# walrus - Накапливание данных
c = 0
data = [5, 4, 3, 2]
print([c := c + x for x in data], " walrus - Накапливание данных", "\n")

# lambda определяет заданное число совпадений ОБ

a = 5
b = 5
bo_ol = [a == b for _ in range(5)]
print([i for i in filter(lambda r: not r is False, bo_ol)])
if [i for i in filter(lambda r: not r, bo_ol)] is True:
    print("ok")
else:
    print("no")
# Филтрация по bool
bo_ol = [True, False, True, True, True]
print([r for r in filter(lambda r: r is False, bo_ol)], " фильтруем из списка bo_ol False", "\n")
print([r for r in filter(lambda r: r is True, bo_ol)], " фильтруем из списка bo_ol True", "\n")

# Фильтрация по структуре данных, здесь отделяем list от всего остального
data_structure = [None, [5, 80], None]
print(list(filter(lambda x: type(x) == list, data_structure))[0], " Фильтрация по структуре данных, здесь"
                                                                  " отделяем list от всего остального", "\n")

if len([r for r in filter(lambda r: r is True, bo_ol)]) == 0:
    print(" len == 0")
else:
    print(" len != 0")

# Генератор случайных чисел в заданном диапазоне и в нужном кол-ве
r = lambda x, y: random.randint(x, y)
print([r(10, 30) for _ in range(5)], " Генератор случайных чисел в заданном диапазоне и в  нужном кол-ве", "\n")

#  Генератор случайных чисел в заданном диапазоне, с заданным шагом и в нужном кол-ве
print([(lambda x, y, z: random.randrange(x, y, z))(10, 100, 20) for _ in range(5)], " Генератор случайных чисел в "
                                                                                    "заданном диапазоне, с заданным"
                                                                                    " шагом и в  нужном кол-ве", "\n")

# Операции между LIST и LIST[LIST], умножить ОБ из b  на ОБ из LIST[LIST] поиндексно

x = [[10, 20, 30, 40], [50, 60, 70, 80]]  # вложенные LIST[LIST]
b = [2, 2, 2, 2]

j = map(lambda k: [[j * k for j in i] for i in x], b)  # lambda вытаскивает  из вложенных LIST поиндексно все ОБ
print(next(j), " next(j) выводит одну итерацию", "\n")

# Поиндексное действие П Р О С Т О
c = [10, 20, 30, 40]
b = [2, 2, 2, 2]
print(list(map(lambda x_f, e_r_f: e_r_f * x_f, c, b)), " Поиндексное действие П Р О С Т О", "\n")

# Операции между LIST и LIST[LIST], умножить ОБ из y_  на ОБ из LIST[LIST] поиндексно

x_ = [[1, 49, 4, 0], [1, 41, 6, 1], [1, 40, 2, 0]]
y_ = [0.5, 0.5, 0.5, 0.5]
print(list(map(lambda enum_and_y, data: [d * y_[enum_and_y[0]] for d in data], enumerate(y_), x_)),
      " Разный LEN() у LIST и LIST[LIST] и Операции между LIST и LIST[LIST] с разным LEN()", "\n")

#  reduce  используем с 3х мерной матрицей

ar = np.arange(1, 13, 1).reshape(2, 3, 2)
print(ar, " генерируем 3х мерную матрицу от 1 до 12 ", "\n")

ar_reduc_1 = reduce(lambda x, y: x + y, ar)
print(ar_reduc_1, " reduce уменьшает размерность матрицы суммируя ОБ в матрице, сумма ОБ не меняется = 78", "\n")

ar_reduc_2 = reduce(lambda x, y: x + y, ar_reduc_1)
print(ar_reduc_2, " ещё раз уменьшили ", "\n")

ar_reduc_3 = reduce(lambda x, y: x + y, ar_reduc_2)
print(ar_reduc_3, " и ещё раз ", "\n")

#  Использование цепочки методов в lambda функции

l = [1, 2]
lb = (lambda x: (l.pop(), l.append(x), l.insert(0, 100)))(10)
print(l, " Использование цепочки методов в lambda функции, здесь применены l.pop(),l.append(x), l.insert(0, 100)", "\n")

# reduce действия со списком

print(reduce(lambda x, y: x * y, (2, 5)), " reduce действия со списком", "\n")

# Перемножение, сложение, и тд с LC , lambda, reduce. Списки с разным len
print([[reduce(lambda x, y: x * y, (m)) for m in list(i)]
       for i in list(map(lambda y: zip(y, b), x))], " Перемножение, сложение, и тд с LC , lambda, "
                                                    "reduce. Списки с разным len", "\n")

# min значение в списке
a = [1, 2, 3, 0.5]
print(min(range(len(a)), key=lambda i: a[i]), "min значение в списке, проверка поиндексно", "\n")

#  Преобразование в матрицу 1 / 0 по совпадению в списках
b = [9, 5, 2, 10, 10, 10, 10, 1, 9, 3]
d = [[5, 9], [11, 10], [13, 4], [6, 10], [11, 12]]
n = list(map(lambda x: [1 if j in x else 0 for j in b], d))
print(n, " Преобразование в матрицу 1 / 0 по совпадению в списках", "\n")


# самое длинное слово самый короткий код
file_text = "That's an important role in everything from traditional computer science it comes close to providing one stop shopping for most statistical work "
list_word_split = file_text.split(" ")
max_len_word = max(list(map(lambda x: len(x), list_word_split)))
long_words = list(filter(lambda x: len(x) == max_len_word, list_word_split))
print(f"long lenght : {max_len_word}")
print(f"long words : {long_words}", "\n")


# фильтрация по расширению файла
#os.path.splitext, чтобы разделить имя файла и его расширение
files = ["13.txt", "23.txt", "25.pdf", " ", "14.txt", "xls_x.xlsx"]
for file in files:
    if os.path.splitext(file)[1] == ".txt":
        print(file)

# фильтрация по расширению файла
files = ["13.txt", "23.txt", "25.pdf", " ","14.txt", "xls_x.xlsx"]
for i in files:
    if i[-4:] == ".txt":
        print(i, "filter file extension")

# lambda без аргумента
PI = 3.14
num_pi = lambda : PI
print(num_pi())


# Сортировка по второму элементу
persons = [["Kir", 53], ["Leo", 10], ["Bim", 25]]
print(sorted(persons, key=lambda x: x[1]))

# map - применяет через lambda - max к value словаря но выводит ключи
dict = {1: {"a": 20, "b": 1, "c": 1000, "d": -5},
2: {"a": 555, "b": 10, "c": -33, "d": 77},
3: {"a": 0.01, "b": 17, "c": 0, "d": 840}}

res = map(lambda x: max(x, key=x.get), dict.values())
print(list(res), "map - применяет через lambda - max к value словаря но выводит ключи")

# фильтруем буквы , цыфры с  filter
n = "Kirill53"
filtr = "".join(filter(lambda x: x if x.isalpha() else None, n))
print(f"фильтруем буквы , цыфры с  filter:  {n} - > {filtr}")

# Фильтр вложенных списков содержащих тип str
a = [[4], ['qwer'], [5, 1], [555, 'abc'], [12, 10, 7, 5]]

f = list(filter(lambda x: any(isinstance(y, str) for y in x), a))
print(f"Фильтр вложенных списков содержащих тип str -> {f}")
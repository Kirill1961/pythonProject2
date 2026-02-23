

import numpy as np
from numpy.random import default_rng
from io import StringIO
import time as tm
import logging
import random
import pandas as pd
from sklearn.metrics import confusion_matrix


logging.basicConfig(level=logging.DEBUG, filename="x_o_r.log", filemode="w")
logger = logging.getLogger("X_O_R")
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

# Добавляем в матрицы zeros или ones нужные значения, ТОЛЬКО из type=ndarray!
a = np.ones((1, 5), int)  # для вставок создали array (1,5) из едениц
logger.debug(a)
res = np.zeros((5, 5), int)  # нулевой array (5,5)
logger.debug((res, " res"))
# tm.sleep(0.5)
tm.sleep(0.5)
# logger.debug(res)


# Итерация с заменой строк и столбов
res1 = [res[i] if sum(res[i]) != 0 else res[i] + a[0] for i in range(4)]
logger.debug((res1, " change string"))

# Анимация заполнения array
rs = np.zeros((5, 5), int)


def zer():
    def iner(n):
        for n in range(n):
            tm.sleep(0.01)
            rs[n] = a  # замена строки
            rs[:, n] = a  # замена столба
            print(rs, "Замена строк и столбов")
            # logger.debug(res)
        return rs

    return iner


z = zer()
z(5)

#  linspace то же самое что и arange но num - задаёт кол-во случайных значений и шаг расчитывает сам
print(np.linspace(0.1, 0.2, num=5), " linspace то же самое что и arange но num - задаёт кол-во случайных "
                                    "значений и шаг расчитывает сам", "\n")
logger.debug((np.linspace(0.1, 0.2, num=5), " linspace"))

#  default_rng - Создание матрицы с item type float от 1 до 0, '5' - начальное число ? XM
print(default_rng(5).random((2, 3)), " default_rng - Создание матрицы с item type float от"
                                     " 1 до 0, '5' - начальное число ? XM", "\n")
logger.debug((default_rng(5).random((2, 3)), " default_rng"))

# Создание random матрицы из целых случайных чисел. 10 интервал выбора чисел
print(np.random.randint(10, size=(5, 5)), " np.random.randint -  Создание random матрицы из целых случайных чисел."
                                          " 10 интервал выбора чисел", "\n")

# Создание random матрицы с 0 и 1, интервал от 0 - 1,size - кол-во значений, dim - любая
print(np.random.randint(2, size=(5)), " Создание random матрицы с 0 и 1, интервал от 0 - 1,size"
                                      " - кол-во значений, dim - любая", "\n")
logger.debug((np.random.randint(2, size=(2, 5)), " random.randint"))

print(np.random.randint(2, size=(2, 5)), " Создание random матрицы с 0 и 1, интервал от 0 - 1,size"
                                         " - кол-во значений, dim - любая", "\n")

print(np.random.randint(2, size=(2, 2, 5)), " Создание randomматрицы с 0 и 1, интервал от 0 - 1,size"
                                            " - кол-во значений, dim - любая", "\n")

# np.random.random - Создание матрицы с item type float от 1 до 0
print(np.random.random((3, 2, 2, 5)), " np.random.random - Создание матрицы с item type float от 1 до 0", "\n")

# flat - многомерный массив сворачивает до одномерного, return КОПИЮ
f = np.random.randint(10, size=(2, 3, 3))
print(f, " не свёрнутый массив")
print(f.flat[2], " flat свернул массив и вывел идекс 2")
print(f.flat[11], " flat свернул массив и вывел идекс 11", "\n")

# flat - Заполнение другими значениями свёрнутого массива
g = np.array([[[4, 0, 1],
               [8, 9, 4],
               [0, 5, 4]],

              [[2, 9, 6],
               [9, 3, 5],
               [6, 1, 0]]])
print(g, " исходный массив")
g.flat = 5
print(g, " заполненый массив другими значениями", "\n")
g.flat[[2, 5, 8]] = 100
print(g, " заполняем массив заданным значением на заданные места ", "\n")

# Умножение столбов
l = np.array([[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]])
print(l, "До Умножения столбов", "\n")
print((l[..., 1:] * 10), " Умножаем столбы с инд 1 и 2", "\n")

# Euclidean 3D
x = np.array((1, 2, 6))
y = np.array((-2, 3, 2))
print(np.linalg.norm(x - y), "Euclidean 3D", "\n")

# adjacency matrix - Матрица смежности GPT, list must be sorted
# Создание графа в виде списка рёбер
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Определение количества вершин в графе
num_vertices = max(max(edge) for edge in edges)
print()
# Создание пустой матрицы смежности
adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

# Заполнение матрицы смежности на основе списка рёбер
for edge in edges:
    start, end = edge
    adjacency_matrix[start - 1][end - 1] = 1  # Мы вычитаем 1, так как индексы в Python начинаются с 0

# Вывод матрицы смежности
for row in adjacency_matrix:
    print(row, "adjacency matrix")

print(" ")

# adjacency matrix MY  - Матрица смежности МОЁ, list must be sorted
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

vertex_num = max(j for i in edges for j in i)

# Создание нулевой  матрицы смежности k - строк, v - столбцов
n = [[0 for _ in range(vertex_num)] for _ in range(vertex_num)]

# Форлупим кортежи связей где k - строки, v - столбцы
for k, v in edges:
    # if k == 0 :
    #     n[k][v] = 1
    # else:
    n[k][v - 1] = 1  # в соответствущей k - строке, v - столбце меняем 0 на 1
    n = np.array(n)
print(n, " Матрица смежности МОЁ, list must be sorted")


# adjacency_matrix - вариант Грасса + моё дополнение
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
# Количество вершин
vertex_num = (max(j for i in friendships for j in i) + 1)
# генерируем все варианты пар для сравнения с friendships
d = [(i, j) for i in range (vertex_num) for j in range(vertex_num)]
adjacency_1 = np.array([1 if t in friendships or t in friendships else 0 for t in d]).reshape(10, 10)
print(adjacency_1, "adjacency_matrix - вариант Грасса + моё дополнение")


# friend user vs user - передружить всех юзеров, аналог crossjoin в SQL
a = np.eye(4, 4)  # единичная матрица
print(np.array([[(i, j)for i in a]for j in a]), "передружили i vs j")  # передружили i vs j

# Короткий arange
print(np.r_[1:11], "Короткий arange шаг 1")
print(np.r_[1:11:2], "Короткий arange шаг 2")


# ???????
n = 3
x = np.array((1, 2, 6))
y = np.array((-2, 3, 2))
a = np.zeros(shape=(n, n))
b = np.zeros(shape=(n, n))
for i in range(n):
    for j in range(i + 1, n):
        a[i, j] = abs(x[i] - x[j])
        b[i, j] = abs(y[i] - y[j])
print(a)
print(b)

# Автоматический подбор размера матрицы с помощью reshape(-1, 1)
import numpy as np

# Одномерный массив с 6 элементами
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Преобразование в двумерный массив с 9 строками и 1 столбцом
reshaped_arr = arr.reshape(-1, 1)
# Преобразование в двумерный массив с 3 строками и 3 столбцом
reshaped_arr_ = arr.reshape(-1, 3)

print(reshaped_arr)
print(reshaped_arr_)

# Матрица из букв alphabet
print(np.array([chr(i) for i in range(97, 109)]), 'Одномерный массив', '\n')
print(np.array([chr(i) for i in range(97, 109)]).reshape(3, 4), 'Двухмерный массив', '\n')
print(np.array([chr(i) for i in range(97,115)]).reshape(3, 2, 3), 'Трёхмерный массив', '\n')

# Уменьшение размерности массива, order='C', 'F', 'A', 'K'
print(np.arange(1, 13).reshape(2, 2, 3), 'Исходный массив', '\n')
print(f"C-order, строковой порядок, стоит по умолчанию: {np.arange(1, 13).reshape(2, 2, 3).ravel(order='C')} Выход (идёт по строкам внутри блоков)")
print(f"F-order, Fortran-order, столбцовый порядок: {np.arange(1, 13).reshape(2, 2, 3).ravel(order='F')}  Выход (идёт по столбцам)")
print(f"A-order, Any-order, сохраняет исходный: {np.arange(1, 13).reshape(2, 2, 3).ravel(order='A')} ")
print(f"K-order, Keep-order, сохраняет физический порядок: {np.arange(1, 13).reshape(2, 2, 3).ravel(order='A')} ")



arr_2d = np.array([[1.11111111e-01],
                   [3.33333333e-01],
                   [6.66666667e-01],
                   [6.66666667e-01],
                   [5.26315789e-02],
                   [1.04526316e-04]])

# 1. Метод
arr_1d = arr_2d.flatten()

print(f'1. Метод уменьшения размерности : {arr_1d}')

print(arr_1d.shape)  # (6,)

# 2. Метод
arr_1d_2 = arr_2d.ravel()
print(f'2. Метод уменьшения размерности : {arr_1d_2}')

# 3. Метод
arr_1d_3 = arr_2d.reshape(-1)
print(f'3. Метод уменьшения размерности : {arr_1d_3}')

# 4. Метод
arr_1d_4 = arr_2d.ravel()
print(f'4. Метод уменьшения размерности : {arr_1d_4}')

# 4. Метод
arr_1d_5 = arr_2d.flatten()
print(f'5. Метод уменьшения размерности : {arr_1d_5}')


# TODO вектор столбец n умножить на вектор строку m = матрица shape(n x m)
np.random.seed(0)
arr = np.round(np.random.normal(scale=2, loc=1.5, size=(5, 2)), 2)
a = np.random.randint(1, 10, size=5)
b = np.round(np.random.random(3), 1)

a_T = a.reshape(-1, 1)  # TODO транспонирование вектора а, 1 столбец и n строк

print('Вектор строка "a" : \n', f'{a}')
print('Массив 2 х 5 : \n', f'{arr}')
print('Скалярное умножение arr.T @ a : \n', f'{arr.T @ a_T}')
print('Вектор столбец : \n', f'{a_T}')
print('Вектор строка : \n', f'{b}')
print('Произведение векторов : \n', f'{a_T * b}')

# TODO Пирсон / ФИ для двух классов (0, 1) и двух бинарных признаков

# Две бинарные переменные
A = [1, 0, 1, 0, 1, 0, 1, 0]
B = [1, 0, 1, 1, 0, 0, 1, 0]

# Построим confusion matrix (таблицу сопряжённости)
cm = confusion_matrix(A, B)
a, b, c, d = cm[1, 1], cm[1, 0], cm[0, 1], cm[0, 0]

# Фи-коэффициент по формуле
phi = (a * d - b * c) / np.sqrt((a + b)*(c + d)*(a + c)*(b + d))

print('confusion matrix (таблица сопряжённости) : \n', f'{cm}')
print(f"phi = {phi:.3f}")

# TODO confusion_matrix для 3-х классов (0, 1, 2) и 2-х бинарных признаков
#  * Строка в итоговой матрице - это класс
y_true = [0, 1, 2, 2, 0, 1, 2]
y_pred = [0, 0, 2, 2, 0, 2, 1]

# y_true = [2, 2, 2, 2, 3]
# y_pred = [3, 2, 2, 1, 2]

cm = confusion_matrix(y_true, y_pred)
print('confusion_matrix для 3-х классов : \n', f'y_true : {y_true} \n', f'y_pred : {y_pred} \n', f'{cm}')
for i, j in enumerate(cm):
    print(f'Частота совпадений для класса {i} : {j}')

# TODO Индексы наибольших значений в массиве
#   * argpartition - не возвращает отсортированные индексы, а просто перемещает топ-3 в конец массива.
np.random.seed(0)
arr = np.array(np.random.randint(1, 20, size=10))
idx = np.argpartition(arr, -3)[-3:]
print(f'Индексы наибольших значений в массиве {arr} : \n', f'Индексы {idx}')
print('Наибольшие значения согласно индексам : \n', f'{arr[idx]}')


# TODO Таблица умножения с numpy

ar = np.empty([0])
for i in range(1, 10):
    for j in  range(1, 10):
        ar = np.append(ar, np.array([i * j]))
print('Таблица умножения с numpy : \n', ar.reshape(9, 9))

# TODO Уменьшение Размерности с reshape(n, -1)
np.random.seed(0)
arr = np.array(np.random.randint(1, 20, size=12)).reshape(3, 2, 2)


print('3-х мерный массив : \n', arr)
print('2-х мерный массив 3 строки : \n', arr.reshape(3, -1))
print('2-х мерный массив 3 столбца : \n', arr.reshape(-1, 3))


# TODO append array

a = np.random.randint(10, size=(4, 5))
b = np.random.randint(100, 1000, size=(1, 5))
res = np.append(b, a).reshape(-1, 5)
print(res)

# TODO hsplit

print('Разделение строк \n :', np.vsplit(a, 2))
print('Отрезаем столбцы первые 3 и то что останется \n :', np.hsplit(a, np.array([3, 5])), '\n')

# TODO Псевдо-генератор RandomState,
#  - Генерирует все виды массивов и распределений
rng = np.random.RandomState(1)
print('Псевдо-генератор RandomState c randint : \n', rng.randint(1, 10, 12), '\n')
print('Псевдо-генератор RandomState c normal : \n', rng.normal(0, 1, 12), '\n')

# TODO diag
ar = np.random.randint(1, 10, size=9).reshape(3, 3)
print('diag : \n', np.diag(np.diag(ar)), '\n')

ar = np.random.randint(1, 10, size=12).reshape(3, 4)
print('diag : \n', np.diag(np.diag(ar)), '\n')
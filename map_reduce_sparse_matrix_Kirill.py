"""MapReduce - вид модели пишется под конкретную задачу,
    mapper - проектор который привязывает Элемент к Индикатору пример: (word, 1) или (name_matrix, (i, j), value)
    reducer - коллектор, производит результирующую операцию с Индикаторами - сложение, умножение и тд.
    Если матрица 1млрд х 1млрд и она разрежена 0.0 значениями, то пользуем кортеж (name, (i, j), value),
    MapReduce - позволяет произвести умножение Разреженных матриц пользуя кортежи (name, (i, j), value).
    таким образом: перемножаем НЕ нулевые элементы матрицы в виде ((i, j), value), ответ получаем так же
    ввиде кортежей ((i, j), value)
    Перемножение разреженных матриц:     А[i, k] * B[k, j] = C[i_A, j_A]
    где k - значения из итерации общего размера m, в А ставим в столбы в В ставим в строки, тк они должны быть равны
    i_A и j_A  """

import random
from collections import defaultdict
import numpy as np
import pprint
# TODO begin

np.random.seed(0)
A_ = np.random.randint(10, size=(2, 3))  # размерность матрицы С = А * В, будет 2 х 3
B_ = np.random.randint(10, size=(3, 3))
print(A_, "\n", "\n", B_, "\n")

C = A_.dot(B_)  # размерность матрицы С = А * В, будет 2 х 3
print(C, "C C C C", "\n")

A = np.array([[3, 2, 0], [0, 0, 0]])
B = np.array([[4, -1, 0], [10, 0, 0], [0, 0, 0]])

# A = np.array([[30, 20, 10], [50, 80, 90]])
# A = np.array([[30, 20], [50, 80]])
# A = np.array([[30, 20], [50, 80], [70, 90]])
# A = np.array([[30, 20, 0], [70, 80, 90], [55, 88, 99], [17, 18, 19]])
# B = np.array([[4, 1, 5], [9, 7, 8], [6, 2, 3]])
# B = np.array([[40, -10, 0, 0], [50, 0, 33, 75], [0, 44, 0, 55]])
# B = np.array([[4, 1, 5], [9, 7, 8]])
# B = np.array([[40, -10], [50, 0], [0, 70]])

# print(np.shape(B)[0], ">>>>")
# Матрица D
D = [
    [3, 0, 0],
    [0, 0, 6],
    [0, 8, 0]
]

# Разреженная матрица - sparse matrix, при больших размерах заменяем матрицу на

matrix_name = "D"

# Результирующий список кортежей
sparse_representation = []

# Проход по всем элементам матрицы
for i in range(len(D)):  # индекс строки матрицы, те размер содержащего списка
    for j in range(len(D[i])):  # индекс столбца матрицы, те размер вложенных списков
        if D[i][j] != 0:  # условие исключения значения НОЛЬ
            sparse_representation.append((matrix_name, (i, j), D[i][j]))

# Вывод результата
for item in sparse_representation:
    print(item, "D D D D ", "\n")

# TODO A B
# Моё преобразование  sparse_matrix в tuple (name, (i, j), value)

# Генерируем sparse_matrix, для mutate sparse_matrix в кортеж (name, (i, j), value)
random.seed(0)
c = [[0 if random.random() < 0.8 else random.randint(1, 10) for i in range(3)] for _ in range(5)]
print(c)
name = "C"
sparse_matrix = []
for i in range(len(c)):
    for j in range(len(c[i])):
        if c[i][j] != 0:
            sparse_matrix.append((name, (i, j), c[i][j]))
# pprint.pprint(sparse_matrix)

# TODO param
print(np.size(A, axis=1) , " comon size")  # axis=1 - ось по строкам A
m_1 = np.shape(A)[1]  # axis=1 - size по столбам A
n_1 = np.shape(B)[1]  # axis=1 - size по столбам B
m_0 = np.shape(A)[0]  # axis=0 - size по строкам A
n_0 = np.shape(B)[0]  # axis=0 - size по строкам B
matrix_s = A, B
names = "AB"
d = m_0 - n_0  # разница между кол-вом строк А и строк В

print(d, "delta")

# Разбиваем матрицы на элементы (name, (i, j), c[i][j])
def elements_matrix(name, elems):
    matrix_elem = []
    for n, elem in enumerate(elems):  # n - индекс для names
        for i in range(len(elem)):  # индексы строк
            for j in range(len(elem[i])):  # индексы столбов
                # if elem[i][j] and elem[j][i] != 0:
                if name[n] == "A":
                    matrix_elem.append((name[n], i, j, elem[i][j]))  # пишем в список координаты и значения для А
                elif name[n] == "B":
                    matrix_elem.append((name[n], i, j, elem[i][j]))  # пишем в список координаты и значения для В
    yield matrix_elem


elements = elements_matrix(names, matrix_s)


# print(list(elements))

print(A, "\n", B, "\n")
# TODO elem

# Запись значений элементов в список словаря
def matrix_multiply_mapper(m, element):
    elements_total = defaultdict(list)
    for elem in [j for i in element for j in i]:
        name, i, j, value = elem[0], elem[1], elem[2], elem[3]
        for k in range(m):  # m - общий размер
            if name == "A":
                elements_total[j].append(A[i, k])  # первым заполняем список словаря значениями матрицы А
            else:
                elements_total[i].append(B[k, j])  # вторым заполняем список словаря значениями матрицы В
            for element in elements_total.values():
                num_pairs = len(element)  # num_pairs - число для задания количества пар
                r = [element[i: i + m] for i in range(0, num_pairs, m)]  # срезами вытаскиваем значения по 2 или более
                pr = np.array([sum(i * j for i, j in list(zip(i, j)))
                               for i in r[0: m + d] for j in r[m + d:]])  # срезы, соединение знач. для умножения и sum
                # pr = [(i, j) for i in r[0: m + d] for j in r[m + d:]]
                # print(r)
    yield pr

# TODO end
element_mtrx = matrix_multiply_mapper(m_1, elements)
print(list(element_mtrx), "element_mtrx", "\n")


print(A, "\n", B, "\n")

""" reducer не понадобился тк вся обработка в matrix_multiply_mapper"""
def matrix_multiply_reducer(m, key_indexed_value):
    pass

reduce = matrix_multiply_reducer(m_1, element_mtrx)
# print(list(reduce), "reduce", "\n")

print(A, "\n", B, "\n")
# перемножение для проверки
print(A.dot(B))

"""MapReduce - вид модели пишется под конкретную задачу,
    mapper - проектор который привязывает Элемент к Индикатору пример: (word, 1) или (name_matrix, (i, j), value)
    reducer - коллектор, производит результирующую операцию с Индикаторами - сложение, умножение и тд.
    Если матрица 1млрд х 1млрд и она разрежена 0.0 значениями, то пользуем кортеж (name, (i, j), value),
    MapReduce - позволяет произвести умножение Разреженных матриц пользуя кортежи (name, (i, j), value).
    таким образом: перемножаем НЕ нулевые элементы матрицы в виде ((i, j), value), ответ получаем так же
    ввиде кортежей ((i, j), value)
    Перемножение разреженных матриц:     А[i, k] * B[k, j] = C[i_A, j_A]
    где k - значения из итерации общего размера m, в А ставим k - в столбы в В ставим k - в строки, тк они должны быть
    равны i_A и j_A -  """

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

# A = np.array([[3, 2, 70], [0, 0, 0]])
# B = np.array([[4, -1, 0], [10, 30, 0], [0, 0, 5]])
A = np.array(
    [
        [30, 10, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 70],
        [0, 0, 50, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)

B = np.array(
    [
        [2, 0, 0, 0, 0],
        [5, 0, 0, 0, 0],
        [0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0],
    ]
)
# A = np.array([[30, 40], [0, 0]])
# A = np.array([[30, 20], [50, 80]])
# A = np.array([[30, 20], [50, 80], [70, 90]])
# A = np.array([[30, 20, 10], [70, 33, 90], [55, 88, 11], [17, 18, 19]])
# B = np.array([[4, 1, 5], [9, 7, 8], [6, 2, 3]])
# B = np.array([[40, -10, 0, 0], [50, 0, 33, 75], [0, 44, 0, 55]])
# B = np.array([[4, 1, 5], [9, 7, 8]])
# B = np.array([[4, 1], [9, 7]])
# B = np.array([[4, 1], [5, 0], [0, 7]])
# B = np.array([[0, 7], [0, 70]])

# print(np.shape(B)[0], ">>>>")
# Матрица D
D = [[3, 0, 0], [0, 0, 6], [0, 8, 0]]

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
c = [
    [0 if random.random() < 0.8 else random.randint(1, 10) for i in range(3)]
    for _ in range(5)
]
print(c)
name = "C"
sparse_matrix = []
for i in range(len(c)):
    for j in range(len(c[i])):
        if c[i][j] != 0:
            sparse_matrix.append((name, (i, j), c[i][j]))

# TODO param
print(np.size(A, axis=1), " comon size")  # axis=1 - ось по строкам A
comon_size = np.shape(A)[1]  # axis=1 - size по столбам A
b_1 = np.shape(B)[1]  # axis=1 - size по столбам B
a_0 = np.shape(A)[0]  # axis=0 - size по строкам A
b_0 = np.shape(B)[0]  # axis=0 - size по строкам B
matrix_s = A, B
names = "AB"
d = abs(comon_size - b_1)  # разница между кол-вом строк А и строк В

print(d, "delta", "\n")


def elements_matrix(name, elems):
    matrix_elem = []
    for n, elem in enumerate(elems):  # n - индекс для names
        # print(elem, ">>>", "\n")
        for i in range(len(elem)):  # индексы строк
            # print(i,"s t r i ng", "\n")
            for j in range(len(elem[i])):  # индексы столбов
                # print(j, "c o l u mn s", "\n")
                # if elem[i][j] != 0:
                if name[n] == "A":
                    matrix_elem.append(
                        (name[n], (i, j), elem[i][j])
                    )  # пишем в список координаты и значения для А

                elif name[n] == "B":
                    matrix_elem.append(
                        (name[n], (i, j), elem[i][j])
                    )  # пишем в список координаты и значения для В

    yield matrix_elem


entries = elements_matrix(names, matrix_s)
print("matrix for sparse and multiply")
print(A, "\n", "\n", B, "\n")


# TODO elem
def matrix_multiply_mapper(m, element):
    for elem in [j for i in element for j in i]:
        name, (i, j), value = (
            elem[0],
            elem[1],
            elem[2],
        )  # выделение компонентов из элементов - name, i, j, value
        for k in range(m + 1):  # m - общий размер
            if name == "A":
                yield (i, k), i, value
            else:
                yield (k, j), j, value


# TODO end
mapper = matrix_multiply_mapper(comon_size, entries)
# print(list(mapper), "element_mtrx", "\n")


# print(A, "\n", B, "\n")


def matrix_multiply_reducer(m, entries):
    result_by_index = defaultdict(list)
    global result_multiply_spars_matrix
    for key, index, value in entries:
        # привязка координат к величинам в матрицах и запись в словарь
        result_by_index[key].append((index, value))

        # if len(r) == a_1 * 2 - explanation: a_1 это общий размер и он удваивается тк список в словаре заполняется
        #   a_1 числом значений из строк А + a_1 число значений столбов из В
        coordinates_values_total = [
            (r[0:comon_size], r[comon_size:])
            for r in result_by_index.values()
            if len(r) == comon_size * 2
        ]

        #  Разделение координат и величин для действий над величинами;
        #  if all((k[1], v[1])) - удаляет нулевые величины, False
        coordinates = [
            set([(k[0], v[0]) for k, v in zip(i[0], i[1]) if all((k[1], v[1]))])
            for i in coordinates_values_total
        ]

        # умножение и сложение величин двух матриц;
        # if i[k] - удаляет пустые set(),  False
        values_not_zero = [
            sum([(k[1] * v[1]) for k, v in zip(pair[0], pair[1])])
            for pair in coordinates_values_total
        ]

        # соединение вычисленных значений с соответствующими им координатами; if pair[0] - удаляет пустые set(),  False
        result_multiply_spars_matrix = [
            pair for pair in zip(coordinates, values_not_zero) if pair[0]
        ]

    return result_multiply_spars_matrix


reducer = matrix_multiply_reducer(comon_size, mapper)  # m_1 общий размер
print(list(reducer), "result multiply spars matrix", "\n")
# print(reducer, "reduce", "\n")

print("check multiply by numpy", "\n")
# перемножение для проверки
print(A.dot(B))

# map_reduce = (entries, mapper, reducer)
# print(list(map_reduce))

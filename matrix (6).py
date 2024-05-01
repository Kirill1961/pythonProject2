import numpy as np
from numpy.random import default_rng
from io import StringIO

all_people = [{'id': 11, 'name': 'Joe'}, {'id': 22, 'name': 'Bob'}, {'id': 33, 'name': 'Tom'},
              {'id': 44, 'name': 'Nick'}, {'id': 55, 'name': 'Fred'}]

connect_friend = [(0, 1), (0, 2), (1, 2), (3, 2), (3, 0), (1, 4)]


def conn_fre(x, y):
    arry = []
    for w in range(x):
        arry.append([])
        for r in y:
            a = 1 if (w in r) == True else 0
            arry[w].append(a)
            print(w, r, connect_friend.index(r), w in r, r[0])
    print(arry[4], ' friendships by index ')
    frend_ship = [num for num, is_frend in enumerate(arry[1]) if is_frend]
    print(frend_ship, ' id friends for set user')
    print(' ', *[e for e in range(len(connect_friend))], sep='  ')  # распаковали список с помощью звезды " * "
    for l in range(x):  # вывод графа в табличном виде,
        print(l, arry[l])


matrix_1 = np.eye(5)
print(matrix_1)

conn_fre(len(all_people), connect_friend)

# Векторно-матричное умножение,  находим  скалярное произведение вектора и каждой строки матрицы

# input = [0.4, 0.3, 0.6]
# weights = [[0.1, 0.2, 0.4],
#            [0.2, 0.1, 0.0],
#            [0.4, 0.2, 0.1]]
# output = 0


# def scalar_product(input, weights):
#     output = 0
#     for i in range(len(input)):
#         output += input[i] * weights[i]
#
#     return output
#
#
# def matrix_vector_multiplay(vector, matrix):
#     output = [0, 0, 0]
#     for i in range(len(vector)):
#         output[i] = scalar_product(vector, matrix[i])
#     return output
#
#
# prediction = matrix_vector_multiplay(input, weights)
# print(prediction)
#
#
# # Мой вариант умножения, чуток неправильный
#
# def scalar_product_(input, weights):
#     output = 0
#     out_put = []
#     for i in range(len(input)):
#         wei_ghts = weights[i]
#         output += input[i] * wei_ghts[i]
#         out_put.append(output)
#         # print(output, '>>>>>>>>>>')
#     return out_put
#
#
# print(scalar_product_(input, weights))

# Генератор матрицы 1- 16
new_matrix = np.arange(1, 17).reshape(4, 4)
print(new_matrix, " Генератор матрицы 1- 16")

# Генератор матрицы 0 - 15
new_matrix = np.arange(16).reshape(4, 4)
print(new_matrix, " Генератор матрицы 0 - 15", " \n")

# Поэлементное сложение

x = np.array([11, 200])
y = np.array([35, 441])
print(np.add(x, y), " Поэлементное сложение с фу-ей add(x, y)", "\n")

# Преобразование списка в матрицу
g = [[10, 5, 44], [20, 8, 39], [40, 100, 501]]
print(g, " список до преобразования", "\n")
g_matrix = np.array(g)
print(g_matrix, " Преобразование списка в матрицу", "\n")
print(g_matrix.ndim, " - количество измерений", g_matrix.shape, " - размерность по каждому измерению", "\n")

# Преобразование матрицы в горизонтальную матрицу
print(np.hstack(g_matrix), " Преобразование матрицы в горизонтальную матрицу", "\n")

# Преобразование матрицы в обратно в вертикальную матрицу
print(np.vstack(g_matrix), " Преобразование матрицы в обратно в вертикальную матрицу", "\n")

# Суммирование по столбцам
print(g_matrix.sum(axis=0), " Суммирование по столбцам", "\n")
# Преобразование Обратно в список
print(g_matrix.tolist(), " Обратно в список", "\n")

# Просто список в 1D матрицу, а затем в 2D матрицу
j = [2, 4, 6, 8]
j_mat = np.array(j)

print(j_mat, " - Просто список [2, 4, 6, 8] в 1D матрицу", "\n")
print(j_mat.reshape(2, 2), " а затем в 2D матрицу ")

# Из списка в матрицу и Сумма построчно

c = [[1000, 1], [5, 80], [1, 200], [200, 1], [65, 21], [20, 73], [13, 72]]
print(c, " Список С", "\n")
m = np.array(c)
print(m, " Матрица m списка С", "\n")
mx = m.sum(axis=1)
print(mx, " Сумма построчно в матрице m или вложенных списков в L[L] - C  ", "\n")

# Индекс min или max значения во вложенном списке через матрицу
print(np.where(mx == 86), " индекс значения 86", "\n")

print(m[np.where(mx == 86)], " Определяем по ИНДЕКСУ значение в матрице m или вложенный список в L[L] - C")

# Генерация матрицы с одинаковыми значениями
a_full = np.full((1, 3, 3), 20)
print(a_full, " Генерация матрицы с одинаковыми значениями, np.full((1,3,3 - это shape),20 - значение в матрицу) ",
      "\n")

# Матрица нулевая 5 х 5 с целыми числами
print(np.zeros((5, 5)).astype(int), " Матрица нулевая 5 х 5 с целыми числами", "\n")

# Вытаскиваем из матрицы строки для действий
d = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
c = [[0, 1, 2],
     [3, 4, 5]]

print([[d[j][i] for i in range(3)] for j in range(3)], "Вытаскиваем из матрицы строки для действий", "\n")
print([[c[j][i] for i in range(3)] for j in range(2)], "Вытаскиваем из матрицы строки для действий", "\n")

# Перемещение осей при задании матрицы
e = np.ones((6, 3, 5))  # 6 матриц 3 строки и 5 столбов
print(e, " Перемещение осей при задании матрицы, 6 матриц 3 строки и 5 столбов ")
# d = np.ones((6, 3, 5))  # 6 матриц 3 строки и 5 столбов
b = np.rollaxis(e, 2, 0).shape  # Ось с индексом 2 это "5" перемещаем на место с индексом 0
print(np.ones((b)), " Перемещение осей при задании матрицы, 5 матриц 6 строки и 3 столбов ", "\n")

# Определим метки -1 если х<0 и +1 если х>0, для сгенерированных х в 1D матриц
x = np.linspace(-2.5, 2.5, 6)
print(x)
print(np.piecewise(x, [x < 0, x >= 0], [-1, 1]), "np.piecewise Определим метки -1 если х<0 и +1 если х>0", "\n")

# Матрица с regex
text = StringIO("1312 foo\n1534  bar\n444   qux")
regexp = r"(\d+)\s+(...)"  # match [digits, whitespace, anything]
out_put = np.fromregex(text, regexp, [('num', np.int64), ('key', 'S3')])
print(out_put, "StringIO Матрица с regex", "\n")

# np.expand_dims - Увеличение размерности
x = np.array([1, 2])
print(x)
y = np.expand_dims(x, axis=0)
print(y, "axis=0")
b = np.expand_dims(x, axis=1)
print(b, "axis=1")
v = np.expand_dims(x, axis=(0, 1))
print(v, "axis=(0, 1)")
w = np.expand_dims(x, axis=(2, 0))
print(w, "axis=(2, 0)", "\n")

# np.stack - Объединения 2-х мерных массивов с одинаковым shape
u = np.arange(10, 19).reshape(3, 3)
e = np.arange(0, 9).reshape(3, 3)
print(e, "arr1", "\n" * 2, u, " arr2", "\n")
print(np.stack([e, u], axis=0), "np.stack - Объеденения 2х мерных массивов с одинаковым shape ", "\n")

# list(zip(h, o) - Объединения  2х мерных массивов с разным shape :-)
f = np.random.random((2, 3))
g = np.random.random((1, 3))
c = [f, g]  # :-) тот же эффект
print(list(zip([f, g])), "Объеденения 2х мерных массивов с разным shape list(zip(h, o)  :-)", "\n")

# r_  Объединение 2-х мерных массивов с разным shape axis=0
h = np.random.random((2, 3))
o = np.random.random((1, 3))
print(np.r_[h, o], "r_  ->  Объединение 2-х мерных массивов с разным shape axis=0")

# с_  Объединение 2-х мерных массивов с одинаковым shape axis=1
h = np.random.random((2, 3))
o = np.random.random((2, 3))
print(np.c_[h, o], "c_  ->  Объединение 2-х мерных массивов, с_ только с одинаковым shape, axis=1", "\n")

# np.empty - Заполняется последним array/slice подходящим под указанный shape или dtype , если нет то НУЛИ
print(np.random.random((1, 3)), "np.random.random((1, 3))", "\n")
print(np.random.random((2, 3)), "np.random.random((2, 3))", "\n")
print(np.empty((3, 2, 2)), "np.empty Заполняется последним записанным array или slice", "\n")

# Нулевой array
print(np.empty(0), "Нулевой array", "\n")
r = f, g
print(r, "Запись в нулевой array  2х мерных массивов с разным shape", "\n")

# indices - генерация матриц с маской и с заменой axis
i = np.indices((1, 3, 5))
print(i, "indices - генерация матриц с маской и с заменой axis", "\n")
i[:] = 0
print(i, "Обнуление матрицы", "\n")

# Изменение размерности матрица с axis=0 и axis=1
a = np.array([11, 22, 33])
b = np.expand_dims(a, axis=0)
print(b, "Изменение размерности матрица с axis=0 ")
b = np.expand_dims(a, axis=1)
print(b, "Изменение размерности матрица с axis=1 ", "\n")

# Вытащить диагональ матрицы
a = (np.array([61, 16, 23, 72, 61,
               28, 93, 20, 40, 99,
               97, 64, 87, 21, 69,
               79, 63, 77, 69, 36,
               52, 13, 90, 83, 14])).reshape(5, 5)
print([a[i, i] for i in range(5)], "\n")
# Простая построчная итерация массива
print(np.array([a[i] for i in range(5)]), " Простая построчная итерация", "\n")
# Построчная итерация массива for+for
print([[j for j in a[i]] for i in range(5)], " Построчная итерация массива for+for", "\n")

# Разметка массива по признаку 1 - ОБ > 50 и 0 - ОБ < 50
print(np.array([[0 if j < 50 else 1 for j in a[i]] for i in range(5)]),
      "Разметка массива по признаку 1 - ОБ > 50 и 0 - ОБ < 50", "\n")

# flat - многомерный массив сворачивает до одномерного, return КОПИЮ
f = np.random.randint(10, size=(2, 3, 3))
print(f, " не свёрнутый массив")
print(f.flat[2], " flat свернул массив и вывел идекс 2")
print(f.flat[11], " flat свернул массив и вывел идекс 11", "\n")

# Столбцы и строки из матрицы
print(f, " Столбцы и строки из матрицы")
print(f[..., 1], " столбец с инд 1", "\n")
print(f[0][1, 1], "  значение в 2й строке 2го столба 1го блока с инд 1", "\n")
print(f[0][..., 1], " 2й столб 1го блока ", "\n")
print(f[1][2, ...], " 3я строка 2го блока ", "\n")




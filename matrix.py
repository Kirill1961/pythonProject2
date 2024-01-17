import numpy as np

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
    for l in range(x):         # вывод графа в табличном виде,
        print(l, arry[l])

matrix_1 = np.eye(5)
print(matrix_1)

conn_fre(len(all_people), connect_friend)


# Векторно-матричное умножение,  находим  скалярное произведение вектора и каждой строки матрицы

input = [0.4, 0.3, 0.6]
weights = [[0.1, 0.2, 0.4],
           [0.2, 0.1, 0.0],
           [0.4, 0.2, 0.1]]
output = 0
def scalar_product(input, weights):
    output = 0
    for i in range(len(input)):
        output += input[i] * weights[i]

    return output

def matrix_vector_multiplay(vector, matrix):
    output = [0, 0, 0]
    for i in range(len(vector)):
        output[i] = scalar_product(vector, matrix[i])
    return output
prediction = matrix_vector_multiplay(input, weights)
print(prediction)


# Мой вариант умножения, чуток неправильный

def scalar_product_(input, weights):
    output = 0
    out_put = []
    for i in range(len(input)):
        wei_ghts = weights[i]
        output += input[i] * wei_ghts[i]
        out_put.append(output)
        # print(output, '>>>>>>>>>>')
    return out_put
print (scalar_product_(input, weights))


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
g_matrix  = np.array(g)
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
print(j_mat. reshape(2,2), " а затем в 2D матрицу ")


# Из списка в матрицу и Сумма построчно

c = [[1000, 1], [5, 80], [1, 200], [200, 1], [65, 21], [20, 73], [13, 72]]
print(c, " Список С", "\n")
m = np.array(c)
print(m, " Матрица m списка С", "\n")
mx = m.sum(axis=1)
print(mx, " Сумма построчно в матрице m или вложенных списков в L[L] - C  ", "\n")

# Индекс min или max значения во вложенном списке через матрицу
print(np.where(mx == 86),  " индекс значения 86", "\n")

print(m[np.where(mx == 86)], " Определяем по ИНДЕКСУ значение в матрице m или вложенный список в L[L] - C")

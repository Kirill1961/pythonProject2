from collections import deque, Counter
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math as mt

users: list[dict] = [{'id': 0, 'name': 'Alice'},  # list[dict] - аннотация
                     {'id': 1, 'name': 'Benjamin'},
                     {'id': 2, 'name': 'Charlotte'},
                     {'id': 3, 'name': 'David'},
                     {'id': 4, 'name': 'Emily'},
                     {'id': 5, 'name': 'Frederick'},
                     {'id': 6, 'name': 'Grace'},
                     {'id': 7, 'name': 'Henry'},
                     {'id': 8, 'name': 'Isabella'},
                     {'id': 9, 'name': 'James'}]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Количество вершин
vertex_num = (max(j for i in friendships for j in i) + 1)

# adjacency_matrix - вариант Грасса + моё дополнение
# генерируем все варианты пар для сравнения с friendships
d = [(i, j) for i in range(vertex_num) for j in range(vertex_num)]

adjacency_1 = np.array([1 if t in friendships or t in friendships else 0 for t in d]).reshape(10, 10)
print(adjacency_1, "adjacency_matrix - вариант Грасса + моё дополнение")

# Количество вершин
vertex_num = (max(j for i in friendships for j in i) + 1)

print(vertex_num)

# Создание матрицы смежности k - строк, v - столбцов
adjacancy = [[0 for _ in range(vertex_num)] for _ in range(vertex_num)]

# Форлупим кортежи связей где k - строки, v - столбцы
for k, v in friendships:
    # if k == 0 :
    #     adjacancy[k][v - 1] = 1
    # else:
    adjacancy[k][v - 1] = 1  # в соответствущей k - строке, v - столбце меняем 0 на 1
    adjacancy = np.array(adjacancy)
evl, evc = np.linalg.eig(adjacancy)  # evl, evc собственное число, собственный вектор
eigen_vector = [sum(i) for i in evc]
print(adjacancy)
print(evl, "numpy собственные  значения пользователей", "\n")
print(evc, "numpyСобственные вектора пользователей")


# TODO begin
G = nx.Graph()
G.add_edges_from(friendships)

# Визуализация графа
nx.draw(G, with_labels=True)

# Сохранение изображения в файл
plt.savefig("graph_between_central.png")

# eigenvector centrality from gpt
# Создание графа
G = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
              (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)])

# Вычисление центральности собственного вектора из gpt
centrality = nx.eigenvector_centrality_numpy(G)

# Вывод результатов
for node, centr in centrality.items():
    print("Узел:", node, "Центральность собственного вектора:", centr)


# TODO to next
e = np.eye(10)
div_adjacancy_e = adjacancy / e
print(div_adjacancy_e, ">>>>>")
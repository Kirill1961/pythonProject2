import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Создаем граф
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

graph = {0: [1, 2],
         1: [0, 2, 3],
         2: [0, 1, 3],
         3: [1, 2, 4],
         4: [3, 5],
         5: [4, 6, 7],
         6: [5, 8],
         7: [5, 8],
         8: [6, 7, 9],
         9: [8], }

# Создаем направленный граф
G = nx.Graph()

# Добавляем вершины и ребра в граф
for vertex, neighbors in graph.items():
    G.add_node(vertex)
    for neighbor in neighbors:
        G.add_edge(vertex, neighbor)

# Расположение вершин на графе
pos = nx.spring_layout(G)

# Рисуем граф
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
plt.title('Граф')
plt.show()


"""Движение очереди FIFO"""


def bfs(graph, start):
    visited = set()  # Множество для отслеживания посещенных вершин
    queue = deque([start])  # Очередь для обхода вершин
    visited.add(start)  # Помечаем начальную вершину как посещенную
    print(visited, "vis start")
    while queue:  # Пока очередь не пуста
        print(queue, "que поставлены в очередь")
        vertex = queue.popleft()  # Извлекаем вершину из очереди
        print(vertex, "vrx")  # Выводим текущую вершину

        for neighbor in graph[vertex]:  # Перебираем соседей текущей вершины
            if neighbor not in visited:  # проверяем наличие  соседа в set(), определяем посещен/не посещён сосед
                print(neighbor, "nbr")
                visited.add(neighbor)  # если не посещён сохраняем соседа в set() и отмечаем его как посещенный
                queue.append(neighbor)  # Добавляем соседа в очередь
                print(visited, "vis")


# Пример графа в виде словаря смежности
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E', 'J'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E'],
#     'J': ['B']
# }


graph = {0: [1, 2],
         1: [0, 2, 3],
         2: [0, 1, 3],
         3: [1, 2, 4],
         4: [3, 5],
         5: [4, 6, 7],
         6: [5, 8],
         7: [5, 8],
         8: [6, 7, 9],
         9: [8], }

# Вызов функции поиска в ширину, начиная с вершины 'A'
# bfs(graph, 'A')
bfs(graph, 0)

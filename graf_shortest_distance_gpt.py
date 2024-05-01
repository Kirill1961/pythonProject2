from collections import deque

"""A -- B -- C
   |         |
   D -- E -- F"""

# Граф представлен в виде словаря списков смежности
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'F'],
    'D': ['A', 'E'],
    'E': ['D', 'F'],
    'F': ['C', 'E']
}


def shortest_distance(graph, start, end):  # start, end - вершины
    print(end, "end")
    # Инициализация
    queue = deque([(start, 0)])  # start - вершина от которой стартуем, 0 - расстояние от самой себя = нулю
    print(queue, "queue")
    visited = set([start])

    # Обход в ширину
    while queue:

        print(queue)
        node, distance = queue.popleft()
        print(node,"node", distance, "distance")
        if node == end:
            return distance
        for neighbor in graph.get(node, []):
            print(neighbor, "neighbor")
            if neighbor not in visited:
                visited.add(neighbor)
                print(neighbor, distance, "neighbor, distance")
                queue.append((neighbor, distance + 1))  # в список queue подаём соседа и прибавляем одну связь
    return None


# Находим расстояние от узла A до узла F
distance = shortest_distance(graph, 'A', 'F')  # Задаём вершины между которыми ищем расстояние
print("Расстояние от узла A до узла F:", distance)

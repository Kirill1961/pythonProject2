import networkx as nx

# Создание графа
G = nx.Graph()

# Добавление рёбер
G.add_edges_from([(0, 1), (0, 2), (0, 3), (3, 7), (3, 8), (1, 4), (8, 5), (5, 6), (7, 9)])


# G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
#                 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)])


# Вычисление центральности по посредничеству
betweenness_centrality = nx.betweenness_centrality(G)

# Вывод результатов
for node, centrality in betweenness_centrality.items():  # разбираем кортежи узел + степень посредничества
    print(f"Узел {node}: центральность по посредничеству {centrality}")

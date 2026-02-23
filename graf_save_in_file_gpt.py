import networkx as nx
import matplotlib.pyplot as plt

# Создание графа
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# Визуализация графа
nx.draw(G, with_labels=True)

# Сохранение изображения в файл
plt.savefig("graph.png")
# plt.show()
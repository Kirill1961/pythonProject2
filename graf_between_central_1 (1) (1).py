from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

"""Центральность по степени узлов degrees central, значимость узлов между группами"""

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

'6                   '
'  \                 '
'    5              3'
'      \          /  '
'        4      2    '
'          \   /     '
'            8       '
'            |       '
'            0       '

"Просмотр каждого user, начиная с первого 'id': 0, на проход через него кратчайших путей между всеми узлами," \
" интуитивно betwinness это 8, но shortests path узлов 2,3,4,5,6 вычисляются раньше и учитываются при проходе 8 узла"


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# friendships = [(0, 1), (1, 2), (1, 3), (3, 4)]


# friendships = [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (5, 6)]

# TODO begin
G = nx.Graph()
G.add_edges_from(friendships)

# Визуализация графа
nx.draw(G, with_labels=True)

# Сохранение изображения в файл
plt.savefig("graph_between_central.png")

for user in users:  # Добавляем в словари из списка users key - "friends" : [] список с id ближайшиx соседей
    user["friends"] = []


for i, j in friendships:  # заполнение друзьями list - user["friends"]
    users[i]["friends"].append(j)  # к key "friends" с индексом [i] добавляем друга (j)
    users[j]["friends"].append(i)

for id_friend in users:
    print(id_friend["id"], ":", id_friend["friends"], ",")


# print([i for i in users])
# shortest_paths_to = {{'id': 2, 'name': 'Charlotte'}["id"]: [[]]}
# print(shortest_paths_to)


"Один путь - это list узлов, количество list - это количество путей:[0, 2, 4] считаем один путь через узлы 0,2,4"

def short_paths_from(from_user):  # from_user - словари из users
    shortest_paths_to = {from_user["id"]: []}  # Создаём dict для short paths from_user, "id" берём из dict вершин

    frontier = deque((from_user, friend)  # Очередь - К текущему узлу добавляем следующий форлупим соседей
                     for friend in from_user["friends"])  # from_user["friends"] - создали в 50й строке user["friends"]
    while frontier:  # цикл работает пока список frontier, frontier - атрибуты узлов, двигаем очередь FIFO
        prev_user, user = frontier.popleft()

        user_id = user  # id Ближайшие соседи текущего узла

        # TODO middle
        path_to_prev_user = shortest_paths_to[prev_user["id"]]  # Словарь shortest_paths_to, prev_user["id"] - ind юзера

        path_to_prev_user.append(from_user["friends"])  # добавляем все пути соседей

        new_path_to_user = [path + [user_id] for path in path_to_prev_user]

        old_paths_to_user = shortest_paths_to.get(prev_user["id"], [])

        if old_paths_to_user:

            min_path_lenght = len(old_paths_to_user[0])  # из списка старых путей берём len первого пути

        else:
            min_path_lenght = float("inf")
        new_path_to_user = [path for path in new_path_to_user  # LIST[LIST] -> LIST
                            if len([path]) <= min_path_lenght  # len([path])-количество вершин пути
                            and path not in old_paths_to_user]

        shortest_paths_to[user_id] = new_path_to_user + old_paths_to_user  # shortest_paths_to - список путей
        # состоит из списков узлов
        frontier.extend((prev_user, friend) for friend in prev_user["friends"]
                        if friend not in shortest_paths_to)

    return shortest_paths_to


for user in users:  # крутим словари, добавляем ключ "shortest_path" + значение из short_paths_from(user)

    user["shortest_path"] = short_paths_from(user)

# TODO end
for user in users:

    user["betweenness_centrality"] = 0.0  # Инициализация нового ключа + value

for suorce in users:  # suorce - property вершин, user  с добавленными shortest_paths_to и betweenness
    source_id = suorce["id"]
    for target_id, paths in suorce["shortest_path"].items():
        if source_id < target_id:
            num_paths = len(paths)  # Суммируя  num_paths получим betweenness_centrality
            contrib = 1 / num_paths
            for path in paths:

                for id in path:

                    if id not in [source_id, target_id]:

                        suorce['betweenness_centrality'] += contrib
    print(id, "  ",suorce['betweenness_centrality'], "b e t w e e n n e s s")


def farness(user):
    return sum(len(paths)
               for paths in user["shortest_path"].values())


print(list(farness(user) / 3 for user in users))

for user in users:
    user["closeness_centrality"] = 1 / farness(user)
    print(user["closeness_centrality"])

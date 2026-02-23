import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


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

endorsements = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1), (1, 3), (2, 3), (3, 4),
                (5, 4), (5, 6), (7, 5), (6, 8), (8, 7), (8, 9)]

# endorsements = [(0, 1), (1, 0)]


for user in users:
    user["endorses"] = []
    user["endorsed_by"] = []
    # print(user)
for source_id, target_id in endorsements:  # id твоих одобрений и чужих
    # print(source_id, target_id)
    users[source_id]["endorses"].append(users[target_id])  # Твоё одобрение
    users[target_id]["endorsed_by"].append(users[source_id])  # Тебя одобряют


endorsements_by_id = [(user["id"], len(user["endorsed_by"])) for user in users]  # Число одобряющих юзера № id
print(endorsements_by_id)
user_id = user["id"]
num_endorsements = len(user["endorsed_by"])

print(sorted(endorsements_by_id, key=lambda user_id:  user_id))


def page_rank(users, damping = 0.85, num_iters=10):
    num_users = len(users)
    # Равномерно распределяем rank между всеми user и записываем в переменную pr
    pr = {user["id"] : 1 / num_users for user in users}

    # Назначаем базовый rank (нижняя граница rank)
    base_pr = (1 - damping) / num_users

    # цикл по количеству user
    for _ in range(num_iters):
        # Присваиваем для каждого id юзера - базовый rank
        next_pr = {user["id"]: base_pr for user in users}

        for user in users:
            # меняем начальный равномерно распределённый rank величиной len(user["endorses"] - кол-во поддержки для "id"
            link_pr = pr[user["id"]] * damping

            for endorsee in user["endorses"]:
                next_pr[endorsee["id"]] += link_pr / len(user["endorses"])
        # перезаписываем новое значение в pr
        pr = next_pr
    return pr

print(page_rank(users))
# page_rank(users)


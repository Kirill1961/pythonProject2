import math
from math import dist
from collections import  Counter
import random
import numpy as np
"""  Модель нейросети K-Nearest Neighbors (K N N )  """


# грубый подсчёт большинства голосов
def raw_major__vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    print(winner, ' winner ,', votes, ' словарь; key - МЕТКА : value - ЧИСЛО повторов')
    return winner

print(raw_major__vote(['a', 'b', 'b', 'a', 'a','b','b', 'a', 'a','b','b']), ' raw_major__vote')

# Отбор по большинству голосов

def majority_vote (labels): # Подаём из knn_classify() - метки labels отсортированные по возрастанию
    print(labels, ' Метки ближайшие к новой точке')
    vote_counts = Counter(labels) # vote_counts - Словарь, key  - метка : value - кол-во повторов
    winner, winner_count = vote_counts.most_common(1)[0] # список кортежей из vote_counts, берём кортеж с ind [0]
    # print(winner, winner_count, ' Победитель из всех претиндентов') # вытаскиваем из кортежа с ind [0]-1е и 2е значение

    # прокрутка кол-ва голосов, count это значение из словаря vote_counts
    # winner_count - это наибольшее число повторов (голосов),  .
    num_winners = len([count for count in vote_counts.values() if count == winner_count])
    # print(num_winners,  ' количество притендентов')
    print(winner, winner_count, ' Победитель из', num_winners, ' претиндентов')  # вытаскиваем из кортежа с ind [0]-1е и 2е значение
    print('')
    if num_winners == 1:  # если один победитель то возвращаем  его
        return winner
    else:
        return majority_vote((labels[:-1])) # если есть одинаковое число голосов,то повторяем но без самого дальнего

# print(majority_vote ([1,1,3,55,61,55,98,4,1,55,41,1,55,55,55]))
print(majority_vote (['a', 'b', 'b', 'a', 'a','b','b', 'a', 'a','b','b']), ' победитель')




""" Классификатор, точки(данные) это вектора (точка, метка) """



def create_labled_points(number_points):
    random_points = np.random.random(number_points) # случайные точки
    lables_for_points = random_points ** 2 # метки для точек
    # for result in zip(random_points,lables_for_points): # создаём пары ТОЧКА - МЕТКА, кортежи
    #     print(result, ' result')
    #     print(math.dist (result, (0.2, 0.5)), ' euclidian ')# Евклидово расстояние между point и newpoint
    #     print(' ')
    result = [i for i in zip(random_points,lables_for_points)] # создаём пары ТОЧКА - МЕТКА, список кортежей
    # print(result, ' result >>>>>>>>>>>>>>>>>>>>>')
    print('')

    # Сортировка по дистанции point - new_points
    # by_distanse = sorted(result, key=lambda labled_point: math.dist(labled_point, (0.2, 0.5)))
    # print(by_distanse, ' by_distanse')
    return result

create_labled_points(4), ' create_labled_points'# Задаём точки и метки в заданом количестве 10, метки у = х**2



def input_new_points(x):
    random_points = np.random.random(x)  # новая случайная точка new_points
    lables_for_new_points = random_points ** 2  # метка для новой точки new_points
    for result_new_point in [i for i in zip(random_points, lables_for_new_points)]: # метка и точка, список кортежей
        # print(result_new_point, ' result_new_point')
        return result_new_point
input_new_points(1)

# def create_labled_points(number_points):
#     random_points = np.random.random(number_points) # случайные точки
#     lables_for_points = random_points ** 2 # метки для точек
#     for result in zip(random_points,lables_for_points): # создаём пары ТОЧКА - МЕТКА
#         print(result, ' result')
#         print(math.hypot (result[0], 0.5), ' euclidian point vs newpoint')
#         # result_point = [math.hypot (result[0], 0.5)]
#         # print(result_point)
#         print(' ')
#
#         result_i = [i for i in zip(random_points,lables_for_points)] # создаём пары ТОЧКА - МЕТКА
#         print(result_i, ' result_i')
#         print('')
#         #     print(math.hypot (result[0][0], 0.5))
#         by_distanse = sorted(result_i, key=lambda labled_point: math.hypot(labled_point[0], 0.5))
#         print(by_distanse, ' by_distanse')
#
#         # return result, result_i
#
# create_labled_points(4), ' create_labled_points'# Задаём точки и метки в заданом количестве 10, метки у = х**2




# def input_new_points(data_new_points):  # создаём новую точку для определения её принадлежности к 'a' или 'b'
#     return list(np.random.random(data_new_points))

print(' ')
def knn_classify(k, labled_points, new_points):

    # Сортировка по дистанции point - new_points
    print(new_points, 'new_points точка которую классифицируем')
    by_distanse = sorted(labled_points, key=lambda labled_point_for_dist: math.dist(labled_point_for_dist, new_points))

    print(by_distanse, 'Отсортировали по удалённости от всех labled_points до новой new_points')
    k_nearset_labels  = [label for _,label in by_distanse[:k]]
    print(' ')
    print(k_nearset_labels,' k_nearset_labels, вывели три ближайших labled_points до новой new_points')
    return majority_vote((k_nearset_labels))

knn_classify(3, create_labled_points (10), input_new_points(1))


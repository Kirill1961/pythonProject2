import random
from turtle import distance
import math
from statistics import mean

direction
# Случайные точки
def random_point(dim):
    # print([random.random() for _ in range(dim)])
    return [random.random() for _ in range(dim)]

# Случайные дистанции
def random_distance(dim, num_pairs):
    print(dim, num_pairs, ' <<<<<<<<<<<<')
    return [distance((random_point(dim)[0]), (random_point(dim)[0])) for _ in range(num_pairs)]


# print( random_distance((5, 5)), ' random_distance')

# для заданного числа размерностей считаем расстояние vs точками min и average
def min_avg_ratio_func( num_pairs_y): # num_pairs_y -  кол-во пар точек
    dimensions = range(1, 10) # задаём кол-во размерностей
    avg_distances = []
    min_distances = []
    random.seed(0)
    for dim_x in dimensions:
        print(dim_x, ' кол-во размерностей',  num_pairs_y, ' число пар точек')
        distances = random_distance(dim_x, num_pairs_y)
        avg_distances.append(mean(distances))
        min_distances.append(min(distances))
        print(min_distances, 'min_distances' , avg_distances, 'avg_distances')
        # min_dist / avg_dist - соотношение минимального и среднего расстояния меж точками
        return [min_dist / avg_dist for min_dist , avg_dist in zip(min_distances, avg_distances)]
print(min_avg_ratio_func(20), ' min_dist / avg_dist')

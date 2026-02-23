import random
import math as mt

import matplotlib.pyplot as plt
import numpy as np
import logging
from math import exp
import matplotlib as mp

logging.basicConfig(level=logging.DEBUG, filename="x_o_r.log", filemode="w"
                    , format=" \n %(asctime)s \n %(levelname)s \n  %(message)s \n ")
logger = logging.getLogger("X_O_R")
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

inputs = [1.9, 200, 2.1, 2.5, 300, 2.8, 3.1, 3.5, 3.7, 400]
# inputs = [20, 2, 20, 2, 20, 20, 2, 2, 20, 20, 2, 20, 2, 20]

# TODO  inputs1 for coordinates
# inputs = [[19, 28], [21, 27], [20, 23], [11, 15], [13, 13], [26, 13], [-18, -3],
#           [-14, -5], [-11, -6], [-12, -8], [-26, -9], [-19, -11], [-22, -16], [-13, -19],
#           [-49, 0], [-49, 15], [-46, 5], [-41, 8], [-34, -1]]


# TODO  inputs1 for points
# inputs = [2, 100, 20, 4, 1, 30, 3, 150, 40, 200]


class Kmeans:

    def __init__(self, inputs, k):
        self.k = k
        self.means = None  # Центры на старте не заданы тк выбираем их из inputs
        self.inputs = inputs

    # TODO squared_distance
    def squared_distance(self, input, means):  # means -  случайные центры

        """Евклидово расстояние для ОБ в виде одного числа и в виде координат"""
        return np.linalg.norm(input - means)  # Евклидово между центром и ОБ для всех точек
        # return np.linalg.norm(np.array(input) - np.array(means))  # Евклидово между центром и ОБ для координат [x, y]

    def classify(self, input):
        # print("\t", min(range(self.k), key=lambda i: self.squared_distance(input, self.means[i])), "инд ближ центра")

        """lambda передаёт в squared_distance центры(self.means[i] и ОБ из inputs для euclidean.
        Возвращает индекс центра с меньшим расстоянием """
        return min(range(self.k), key=lambda i: self.squared_distance(input, self.means[i]))  # Индексы центров
        # от которых наименее удалены итерируемые ОБ

    def vector_mean(self, i_points, i):  # Проверка кластера на наличие ОБ, i_points - список ОБ в кластере
        if len(i_points) > 0:
            return self.means[i]

    # TODO traine
    def traine(self, inputs):
        print(inputs, " inputs traine")
        self.means = random.sample(inputs, self.k)  # k-случайных центров из inputs
        logger.debug((self.means, " k-random center from inputs"))
        assignments = None  # Индексы центров назначенных для всех ОБ на страте не заданы
        n = 0
        while True:
            n += 1
            new_assignment = list(map(self.classify, inputs))  # Новые индексы центров назначенных для всех ОБ
            logger.debug((n, new_assignment, "new_assignment"))
            if assignments == new_assignment:
                logger.debug((n, assignments, "assignments"))
                logger.debug(([[p for p, a in zip(inputs, assignments) if a == i] for i in range(self.k)]))
                return
            assignments = new_assignment

            for i in range(self.k):
                i_points = [p for p, a in zip(inputs, assignments) if a == i]  # Кластеризация ОБ назначенным центрам

                logger.debug((i_points, i, ">>>>>>>>>"))
                if i_points:
                    print(i, self.means[i], i_points)
                    self.means[i] = self.vector_mean(i_points, i)
                    # print(self.vector_mean(i_points, i), ">>>>>>>>>")

    """Для определения кол-ва кластеров(КЛ) строим диаграмму, Х - кол-во КЛ, У - сумма квадратов отклонения 
    от среднего, где число КЛ = len(inputs). SST max когда один КЛ в котором все inputs, SST min когда 
    число КЛ = числу ОБ те в каждом КЛ по 1му ОБ"""
    # TODO square
    def square_clustering_errors(self, inputs, k):
        print(inputs, k, ">>>>>>>>>>>>>>")
        clusterer = Kmeans(inputs, k)  # создаём ЭКЗЕМПЛЯР класса Kmeans
        clusterer.traine(inputs)  # traine генерирует случайные центры и запускает кластеризацию с выбранными центрами
        means = clusterer.means  # случайные центры, вытаскиваем их из класса через self
        assigments = list(map(clusterer.classify, inputs))  # назначение № кластеров для ОБ из inputs
        print(means, "square")
        return sum([self.squared_distance(input, means[cluster]) for input, cluster in zip(inputs, assigments)])


instance = Kmeans(inputs, k=1)  # экземпляр для вызова square_clustering_errors

ks = range(1, len(inputs) + 1)  # заданное число центров, начало с 1 тк k  не может = 0
errors = [instance.square_clustering_errors(inputs, k) for k in ks]  # SST
print(errors)

# a = Kmeans(inputs, k=1)
# print(a.classify(input), "classify")

plt.plot(ks, errors)
plt.xticks(ks)
plt.xlabel("k")
plt.ylabel("SST")
plt.title("Sum Error / num clusters")
plt.show()

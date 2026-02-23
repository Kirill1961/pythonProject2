import random
from collections import defaultdict

""" Кубики, X - d1 1й кубик, d2 - 2й кубик, Y - сумма 1го и 2го кубика"""


def roll_a_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def direct_sample():  # Прямая выборка Х и У - это вы-ка по данному закону распределения, х=d1, y=d1 + d2
    d1 = roll_a_die()
    d2 = roll_a_die()
    return d1, d1 + d2  # PROBABILITY значений 1-го и суммы 1-го и 2-го кубиков


print(direct_sample(), "direct_sample, PROB значений 1-го и суммы 1-го и 2-го кубиков", "\n")


def random_y_given_x(x):  # PROB Y при известном X - это условное распределение Р(y) = Р(y | x) ????

    return x, x + roll_a_die()


print([random_y_given_x(x) for x in range(1, 7)], "совместное условное распределение"
                                                  " условно зависимых Y и X при X = от 1 до 6", "\n")


def random_x_given_y(y):  # PROB X при известном Y - это условное распределение Р(х) = Р(х | y) ????
    if y <= 7:
        return random.randrange(1, y), y
    if y > 7:
        return random.randrange(y - 6, 7), y


print([random_x_given_y(y) for y in range(2, 13)], "совместное условное распределение "
                                                   "условно зависимых X и Y при Y = от 2 до 12", "\n")

""" Сэмплирование по Гиббсу, производим пары (х, у) не по заданным  Х и У а отдельно выбирая случайным образом из 
совместного распределения, таким образом получаем безусловно зависимые Х и У"""


def gibbs_sample(num_iter):  # безусловное распределение Х и У безусловно зависимых Х и У
    x, y = 6, 10

    for _ in range(1, num_iter):

        x, _ = random_x_given_y(y)  # _ это для распаковки Х
        _, y = random_y_given_x(x)  # _ это для распаковки У
        # print(x, y)
    return x, y


print(gibbs_sample(1), " gibbs_sample, безусловно зависимые Х и У", "\n")

""" Сравниваем условно зависимые х, у из direct_sample и безусловнозависимые х, у из gibbs_sample"""


def compare_distribution(num_samples):  # Его вар-т заполнения dict для сравнения распр-ия Гиббса и прямого распр-ия
    counts = defaultdict(lambda: [1, 1])  # lambda возвращает в словарь counts - value [0, 0] но лучше [1, 1]

    for _ in range(num_samples):
        counts[gibbs_sample(1)][0] += 1
        counts[direct_sample()][1] += 1
        print(counts, ">>>>>>>>>>>>>>>>>>")
    return counts


print(compare_distribution(10), " here", "\n")

""" Мой вариант отличается тем что value - кортеж в списке (3, 9): [(5, 7)]; у него просто список (1, 2): [3, 1]"""
def compare_distribution_my(num_samples):  # Мой вар-т заполнения dict для сравнения распр-ия Гиббса и прямого распр-ия
    counts_ = {}  # без defaultdict и lambda задаём пустой словарь
    for _ in range(num_samples):
        counts_[gibbs_sample(100)] = [direct_sample()]  # ключ это распр-ие Гиббса, величина это прямое распределение
    #     counts[gibbs_sample(10)][0] += 1  #
    #     counts[direct_sample()][1] += 1
    return counts_


print(compare_distribution_my(1000), " my")



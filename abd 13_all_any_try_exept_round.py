import math
import random
from typing import Union, Optional, Any, Final
from operator import itemgetter
import numpy as np

# x_data = [ 32,47, 57, 67]
# y_data = [ 32, 1600, 30000, 500000]
# x_data = [ 31, 36, 32, 19]
# y_data = [ 32, 37, 34, 20]
x_data = [ 100, 49, 41, 40, 25]
y_data = [ 31, 32, 37, 34, 20]
# x = [ 49, 41]
# y = [ 32, 37]
# x_data = [49]
# y_data = [32]
print(x_data, y_data, " значения для SGD ")

# index_random_for_x_y = random.choice([index_x for index_x, index_y in enumerate(y_data)])
# print(index_random_for_x_y, " random index")
# data_x_y = [x_data[index_random_for_x_y], y_data[index_random_for_x_y]]
# print(data_x_y, " random index  data_x_y  ")
#
# theta_0 = [random.random(), random.random()]
# print(theta_0, "theta_0 begin ")

# theta_0 = [0, 1]

# def data_x_y_for_sgd():
#     index_random_for_x_y = random.choice(range(len(x_data)))


def e_r(x, y, theta_n):
    a, b = theta_n
    # print(y - (b * x + a), " e_r residual")
    return y - a - b * x


def s_e(x, y, theta_n):
    # a, b = theta_n
    print(e_r(x, y, theta_n) ** 2, " square_e_r")
    return e_r(x, y, theta_n) ** 2


# Сумма квадратов отклонений
# def sum_s_e(x, y, theta_n):
#     data= zip(x, y)
#     # print([s_e(x, y, theta_n) for x, y in data])
#     return sum(s_e(x, y, theta_n) for x, y in data)
# print(sum_s_e(x, y, theta_0))


# def e_r(x, y, theta_n):
#     a, b = theta_n
#     print(y - (b * x + a), " e_r residual")
#     return (y - (b * x + a))


def s_e_g(data_x_y, theta_n):
    x, y = data_x_y
    print(e_r(x, y, theta_n), " e_r // residual")
    print(theta_n, " theta_n_for_s_e_g")
    print([-2 * e_r(x, y, theta_n) , -2 * e_r(x, y, theta_n) * x],  " grad_ᶐ_β")
    return [-2 * e_r(x, y, theta_n) , -2 * e_r(x, y, theta_n) * x]  # Градиент ᶐ и β


" Шаг сходимости / Step_Size"


# step_size = 1 / min(n, nm), где n - номер итерации, nm - ограничение min размера шага при больших значениях n
# step_size = 1 / min(n + 1, nm)

def minimz(x_data, y_data, l_r):
    index_random_for_x_y = random.choice([index_x for index_x, index_y in enumerate(y_data)])
    print("\t" * 4 ,index_random_for_x_y, " random index")
    data_x_y = [x_data[index_random_for_x_y], y_data[index_random_for_x_y]]
    print(data_x_y, " random index  data_x_y  ")

    # theta_0 = [random.random(), random.random()]
    theta_0 = [0, 1]
    print(theta_0, "theta_0 begin ")



    quantity_iteration_for_g_d = 0
    while quantity_iteration_for_g_d < 1000:
        quantity_iteration_for_g_d += 1

        print("\t" * 3, quantity_iteration_for_g_d, "\n")
        print(data_x_y, " data_x_y")

        step_size_for_a_b = [grad_for_a_b * l_r * 1 / quantity_iteration_for_g_d for grad_for_a_b in s_e_g(data_x_y, theta_0)]

        print(step_size_for_a_b, " step_size_ᶐ_β")
        theta_n = theta_0
        print(theta_n, " theta_0 before переопределения")

        theta_0 = [theta_0[k] -  step_size_for_a_b[k] for k in range(2)]  # индекс k - выбор для ᶐ или β
        print(theta_0, "theta_0 after переопределения")

        quotient_no_improvement = [round(theta_0[0], 4) == round(theta_n[0], 4)
                                   for _ in range(2)]  # 5-ти кратная проверка равенства theta_0 и theta_n
        print(quotient_no_improvement, " quotient_no_improvement")

        if all(quotient_no_improvement):     # фильтр определяет наличие False

            """ Ха-Ха, if all использовал вместо  if not bool"""
        # if not bool([_ for _ in filter(lambda row:
        #                                row is False, quotient_no_improvement)]):  # фильтр определяет наличие False

            print(theta_0, " theta_0 = theta_n")
            return theta_0

# print(minimz(data_x_y, theta_0, 0.01), " minimz")



def sgd_for_a_b(x_data, y_data,  l):
    numer_iteration = 0
    res = []
    while numer_iteration < 1:
        numer_iteration += 1
        print(minimz(x_data, y_data, l), ">>>>>>>>>>>>>>>")

        res.append(minimz(x_data, y_data, l))
    print(res, " res")
    a_b_result = np.array(res)
    try:
        sum_sgd_a_b = a_b_result.sum(axis=0).tolist()
        alfa_sgd, beta_sgd = sum_sgd_a_b[0] / len(y_data), sum_sgd_a_b[1] / len(x_data)
        print(sum_sgd_a_b, "sum_sgd_a_b")
        print(alfa_sgd, " - alfa_sgd", beta_sgd, " - beta_sgd")
    except AttributeError as e:
        print(str(e))

sgd_for_a_b(x_data, y_data, 0.001)


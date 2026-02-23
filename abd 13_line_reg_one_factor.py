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


def e_r(x, y, theta_n):
    a, b = theta_n
    # print(y - (b * x + a), " e_r residual")
    return y - a - b * x


def s_e(x, y, theta_n):
    # a, b = theta_n
    print(e_r(x, y, theta_n) ** 2, " square_e_r")
    return e_r(x, y, theta_n) ** 2


def s_e_g(data_x_y, theta_n):
    x, y = data_x_y
    print(e_r(x, y, theta_n), " e_r // residual")
    print(theta_n, " theta_n_for_s_e_g")
    print([-2 * e_r(x, y, theta_n) , -2 * e_r(x, y, theta_n) * x],  " grad_ᶐ_β")
    return [-2 * e_r(x, y, theta_n) , -2 * e_r(x, y, theta_n) * x]  # Градиент ᶐ и β


def comput_alpha(x_data, y_data, beta_sgd):
    mean_x = sum(x_data) / len(x_data)
    mean_y = sum(y_data) / len(y_data)
    return abs((mean_y - mean_x) * beta_sgd)  # значение alpha берём по модулю



" Шаг сходимости / Step_Size"

def minimz(x_data, y_data, l_r):
    index_random_for_x_y = random.choice([index_x for index_x, index_y in enumerate(y_data)])
    print("\t" * 4 ,index_random_for_x_y, " random index")
    data_x_y = [x_data[index_random_for_x_y], y_data[index_random_for_x_y]]
    print(data_x_y, " random index  data_x_y  ")

    theta_0 = [random.random(), random.random()]
    # theta_0 = [0, 1]
    print(theta_0, "theta_0 begin ")



    quantity_iteration_for_g_d = 0
    while quantity_iteration_for_g_d < 5000:
        quantity_iteration_for_g_d += 1

        min_step = 1000 # min_step ограничение шага по минимуму

        print("\t" * 3, quantity_iteration_for_g_d, "\n")
        print(data_x_y, " data_x_y")


        # step_size_for_a_b = [ 1 / (grad_for_a_b * l_r) / quantity_iteration_for_g_d  for grad_for_a_b in s_e_g(data_x_y, theta_0)]


        s_e_g_a_b  = s_e_g(data_x_y, theta_0)
        print(s_e_g_a_b, " s_e_g_a_b")

        step_size_for_a = min((s_e_g_a_b[0] * l_r), min_step)

        step_size_for_b = min((s_e_g_a_b[1] * l_r), min_step)


        step_size_for_a_b = [step_size_for_a, step_size_for_b]


        print(step_size_for_a_b, " step_size_ᶐ_β")
        theta_n = theta_0
        print(round(theta_0[0], 3), " theta_0_ᶐ before переопределения")
        print(round(theta_0[1], 3), " theta_0_β before переопределения") # round - ограничение знаков после запятой


        theta_0 = [theta_0[k] -  step_size_for_a_b[k] for k in range(2)]  # индекс k - выбор для ᶐ или β
        print(round(theta_0[0], 5), " theta_0_ᶐ after переопределения")
        print(round(theta_0[1], 5), "theta_0_β after переопределения")

        quotient_no_improvement = [round(theta_0[1], 3) == round(theta_n[1], 3)
                                   for _ in range(3)]  # 3-x кратная проверка равенства theta_0 и theta_n
        print(quotient_no_improvement, " quotient_no_improvement")
        beta = theta_0[1]

        if s_e_g_a_b[0] < 0.000001 or s_e_g_a_b[1] < 0.000001: # условие gпо минимальным градиентам
                                                              # градиенты dLoss/dᶐ и dLoss/dβ

        # if not bool([_ for _ in filter(lambda row:
        #                                row is False, quotient_no_improvement)]):  # фильтр определяет наличие False

            print(theta_0, " theta_0 = theta_n")

            return theta_0

# print(minimz(data_x_y, theta_0, 0.01), " minimz")



def sgd_for_a_b(x_data, y_data,  l):
    numer_iteration = 0
    res = [] # сохранение значений спуска
    while numer_iteration < len(x_data): #  число итераций
        numer_iteration += 1
        # print(minimz(x_data, y_data, l), ">>>>>>>>>>>>>>>")

        res.append(minimz(x_data, y_data, l)) # вызов итерации
    print(res, " res")
    a_b_result = np.array(res) #  преобразование  списка в матрицу для сложения поэлементно
    sum_sgd_a_b = a_b_result.sum(axis=0).tolist() # сложение матрицы по столбцам
    alfa_sgd, beta_sgd = sum_sgd_a_b[0] / len(y_data), sum_sgd_a_b[1] / len(x_data) # среднее коэфф ᶐ и β

    print(sum_sgd_a_b, "sum_sgd_a_b")
    print(alfa_sgd, " - alfa_sgd градиент свободного аргумента д/быть близок к нулю ", beta_sgd, " - beta_sgd")
    print(beta_sgd, " - beta_sgd")
    print(comput_alpha(x_data, y_data, beta_sgd), " -  alpha free argument")
sgd_for_a_b(x_data, y_data, 0.0001)



import math
import random
from typing import Union, Optional, Any, Final
from operator import itemgetter
import numpy as np

# x_data = [ 32,47, 57, 67]
# y_data = [ 32, 1600, 30000, 500000]
# x_data = [ 31, 36, 32, 19]
# y_data = [ 32, 37, 34, 20]
# x_data = [ 100, 49, 41, 40, 25]
# y_data = [ 31, 32, 37, 34, 20]
# x = [ 49, 41]
# y = [ 32, 37]

# x_data = [[49], [41], [40]]

# x_data = [[1, 49, 4, 0]]
# y_data = [32]

x_data = [[1, 49, 4, 0], [1, 41, 6, 1], [1, 40, 2, 0]]
y_data = [32, 37, 34]
print(x_data, y_data, " значения для SGD ")


def e_r(x_data, y_data, theta_n): # residual, theta_n - это вектор β

    print(y_data, " y_data")
    print([y_data - v * w for w in theta_n for v in x_data][0:len(x_data)], " e_r")
    # return [y_data - v * w for w in theta_n for v in x_data][0:len(x_data)]  # 1-й вариант вычисления
    print(list(map(lambda w : [y_data - v * w  for v in x_data], theta_n ))[0][1:], " e_r без intersept" )
    return list(map(lambda w : [y_data - v * w  for v in x_data], theta_n ))[0] # 2-й вариант вычисления


def mean_for_intersept(x_data, y_data):
    mean_y = sum([mean_y for mean_y in y_data]) / len(y_data)
    mean_x = sum([sum(x) / len(x_data[0]) for x in x_data ]) / len(x_data)
    x_intersept = mean_y - mean_x # тк всегда βₒ = 1 мы при вычислении x_intersept его не учитываем
    return x_intersept


# def summ_observer_error_square(y_data):


def r_square(x_data, y_data, t):
    return x_data, y_data, t



def s_e_g_multi_value(x_data, y_data, theta_n):
    print(e_r(x_data, y_data, theta_n), " |||||||||||||||||||||||||||||||||")
    return list(map (lambda x_for_grad, e_r_for_grad:
                     - 2 * e_r_for_grad * x_for_grad, x_data, e_r(x_data, y_data, theta_n)))

def quotient_determination(x_data, y_data, theta_n, data_x_y_full):
    pass


def minimz_multi_value( l_r):


    min_step_size_for_betas, min_beta_for_theta_n = 0,  None
    min_value_betas = []
    numer_iteration = 0
    while numer_iteration < 1: # quantity_ index
        numer_iteration += 1
        print("\t" * 3, numer_iteration, " numer_iteration", "\n")


        index_random_for_x_y = random.choice([index_x for index_x, _ in enumerate(y_data)])
        print("\t" * 4, index_random_for_x_y, " random index")
        data_x_y = [x_data[index_random_for_x_y], y_data[index_random_for_x_y]]
        print(data_x_y, " random index  data_x_y  ")

        beta_initial_for_theta_n = [1, 1, 1, 1]
        # beta_initial_for_theta_n = [random.random() for _ in x_data[0]]
        print(beta_initial_for_theta_n, "beta_initial_for_theta_n")

        beta_for_theta_n = beta_initial_for_theta_n # переопределение вектора β после инициализации


        if beta_for_theta_n == min_beta_for_theta_n :
            return beta_for_theta_n
        else:
            quantity_iteration_for_g_d = 0
            while quantity_iteration_for_g_d < 10:
                quantity_iteration_for_g_d += 1
                min_step = 1000 # min_step ограничение шага по минимуму

                print("\t" * 3, quantity_iteration_for_g_d, " quantity_iteration_for_g_d", "\n")

                step_size_for_betas = [s * l_r for s in s_e_g_multi_value(*data_x_y, beta_for_theta_n)][1:]  # без βₒ
                print(step_size_for_betas, " step_size_for_betas")

                print(beta_for_theta_n, " before" )
                beta_sgd = [beta_for_theta_n[ind] - (step_size_for_betas[ind] * 1 / quantity_iteration_for_g_d)
                            for ind, _ in enumerate(step_size_for_betas)]
                print(beta_for_theta_n, " after")

                if round(beta_for_theta_n[0], 17) == round(beta_sgd[0], 17):  # β noimprov до 16-го зн.coxp. result beta
                    min_value_betas.append(beta_for_theta_n)
                elif quantity_iteration_for_g_d == 10:  # Если закончился цикл сохраняем result beta
                    min_value_betas.append(beta_for_theta_n)
                else:
                    beta_for_theta_n = beta_sgd  # если фильтр не сработал, то переопределение вектора β после шага
    sum_of_betas = [sum(_) for _ in min_value_betas] # список из сумм вложенных списков
    # print(min_value_betas, sum_of_betas)

    min_betas = min_value_betas[sum_of_betas.index(min(sum_of_betas))]  # min значения beta по индексу
    print(min_betas.insert(0,  mean_for_intersept(x_data, y_data)))
    return min_betas # min значения beta + intercept


print(minimz_multi_value(0.001), " minimz")



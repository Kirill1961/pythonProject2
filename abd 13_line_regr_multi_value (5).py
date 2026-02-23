import math
import random
from typing import Union, Optional, Any, Final
from operator import itemgetter
import numpy as np



x_data = [[1, 49, 4, 0], [1, 41, 6, 1], [1, 40, 2, 0]]
y_data = [32, 37, 34]

data_x_y = [x_data, y_data]


def e_r(x_data, y_data, theta_n): # residual

    # print(y_data, " y_data")
    # print([y_data - v * w for w in theta_n for v in x_data][0:len(x_data)], " e_r")

    y_predict = list(map(lambda index_theta_n, data: [d * theta_n[index_theta_n[0]]
                                                 for d in data],  enumerate(theta_n), data_x_y[0]))

    error_y_and_ypredict = [list(map(lambda w : [y_data - v * w for v in x_data], theta_n))[0], y_predict]

    return error_y_and_ypredict  # Это список из 2-х значений - ошибка У observer и y_predict


def mean_for_intersept(x_data, y_data):
    mean_y = sum([mean_y for mean_y in y_data]) / len(y_data)
    mean_x = sum([sum(x) / len(x_data[0]) for x in x_data ]) / len(x_data)
    x_intersept = mean_y - mean_x # тк всегда βₒ = 1 мы при вычислении x_intersept его не учитываем
    mean_y_intercept = [x_intersept, mean_y]
    # print(mean_y_intercept, " mean_y_intercept")
    return mean_y_intercept




def s_e_g_multi_value(x_y_data, theta_n):
    x_data, y_data = x_y_data
    return list(map (lambda x_for_grad, e_r_for_grad:
                     - 2 * e_r_for_grad * x_for_grad, x_data, e_r(x_data, y_data, theta_n)[0]))


def quotient_determination(x_data, y_data, theta_n, data_x_y_full): # data_x_y_full - список всех Х и У

    averag_y = mean_for_intersept(*data_x_y_full)[1] # Среднее для У для расчёта знаменателя RR
    total_sum_square_deviation_from_avereg_y = sum([(i - averag_y) ** 2 for i in data_x_y_full[1]])  # знаменатель RR

    y_predict = [sum(i) for i in e_r(x_data, y_data, theta_n)[1]]
    averag_y_predict = (sum(y_predict)) / len(y_predict)
    sum_square_deviation_from_averag_y_predict = sum([(s_y - averag_y_predict) ** 2 for s_y in y_predict])# числитель RR

    return 1 - (total_sum_square_deviation_from_avereg_y / sum_square_deviation_from_averag_y_predict)


def minimz_multi_value( l_r):


    min_step_size_for_betas, min_beta_for_theta_n = 0,  None
    min_value_betas = []
    numer_iteration = 0
    while numer_iteration < 3: # quantity_ index
        numer_iteration += 1
        # print("\t" * 3, numer_iteration, " numer_iteration", "\n")

        data_x_y_full = [x_data ,y_data]

        index_random_for_x_y = random.choice([index_x for index_x, _ in enumerate(y_data)])  # случайный индекс
        # print("\t" * 4, index_random_for_x_y, " random index")
        data_x_y_by_random_index = [x_data[index_random_for_x_y], y_data[index_random_for_x_y]]
        # print(data_x_y_by_random_index, " random index  data_x_y  ")

        # beta_initial_for_theta_n = [1, 1, 1, 1]
        beta_initial_for_theta_n = [random.random() for _ in x_data[0]]
        # print(beta_initial_for_theta_n, "beta_initial_for_theta_n")

        beta_for_theta_n = beta_initial_for_theta_n


        if beta_for_theta_n == min_beta_for_theta_n :
            return beta_for_theta_n
        else:
            quantity_iteration_for_g_d = 0
            while quantity_iteration_for_g_d < 10:
                quantity_iteration_for_g_d += 1

                # print("\t" * 3, quantity_iteration_for_g_d, " quantity_iteration_for_g_d", "\n")

                step_size_for_betas = [s * l_r for s in s_e_g_multi_value(data_x_y_by_random_index, beta_for_theta_n)][1:]  # без βₒ
                # print(step_size_for_betas, " step_size_for_betas")

                # print(beta_for_theta_n, " before" )
                beta_sgd = [beta_for_theta_n[ind] - (step_size_for_betas[ind] * 1 / quantity_iteration_for_g_d)
                            for ind, _ in enumerate(step_size_for_betas)]
                # print(beta_for_theta_n, " after")
                r_square = quotient_determination(*data_x_y_by_random_index, beta_for_theta_n, data_x_y_full)
                # print( r_square, " quotient_determination")
                if round(beta_for_theta_n[0], 17) == round(beta_sgd[0], 17):  # β noimprov до 16-го зн.coxp. result beta
                    min_value_betas.append(beta_for_theta_n)
                elif quantity_iteration_for_g_d == 10:  # Если закончился цикл сохраняем result beta
                    min_value_betas.append(beta_for_theta_n)
                else:
                    print(r_square, " quotient_determination")
                    beta_for_theta_n = beta_sgd  # Переопределение вектора β если фильтр не сработал


    sum_of_betas = [sum(_) for _ in min_value_betas] # список из сумм вложенных списков
    # print(min_value_betas, sum_of_betas)


    min_betas = min_value_betas[sum_of_betas.index(min(sum_of_betas))]  # min значения beta по индексу
    min_betas.insert(0,  mean_for_intersept(x_data, y_data)[0])  # запись в список на 1-е место значение intersept
    return [1 / 1 + math.exp(-m) for m in min_betas]


print(minimz_multi_value(0.001), " minimz + кэффициент детерминации")


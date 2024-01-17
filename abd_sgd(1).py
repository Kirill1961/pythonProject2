import math
import random
from typing import Union, Optional, Any, Final
from operator import  itemgetter

# num_friends_three = [ 49, 41, 40, 25]
# daily_minutes = [ 32, 37, 34, 20]
num_friends_three = [ 49, 41]
daily_minutes = [ 32, 37]

# print(minimize_stohastic(square, derivative, x_for_sgd,  y_for_sgd , v_theta_for_sgd , alfa_0 = 0.01), ' minimize_stohastic')


def predict( alpha, beta, x_i):
    print(alpha, beta, " predict")
    return x_i * beta + alpha  # прогнозируемый  Ypredict


def error(alpha, beta, x_i, y_i):
    y_predict_of_residual = y_i - predict(alpha, beta, x_i)  # отклонение Ypredict
    # print(y_predict_of_residual, " отклонение Ypredict" "\n")
    return y_predict_of_residual


# Квадратичная ошибка Loss function
def squared_error(x_i, y_i, theta):
    alpha,  beta = theta
    return error(alpha, beta, x_i, y_i) ** 2


# Градиент квадратичной ошибки
def squared_error_gradient(x_i, y_i, theta, learning_rate):
    alpha, beta = theta
    print(alpha, beta, " squared_error_gradient")
    return [-2 * error(alpha, beta, x_i, y_i) * learning_rate, -2 * error(alpha, beta, x_i, y_i)* x_i * learning_rate]


# def step_size_alpha_beta(theta, data, learning_rate):
#     return [squared_error_gradient(x_i, y_i, theta, learning_rate) for x_i, y_i in data]
    # print(step_size_for_alpha_beta, " step_size_for_alpha_beta")

    #
    # step_size_for_alpha_beta = [squared_error_gradient(x_i, y_i, theta)[index_for_alpha_beta] * learning_rate
    #                             for x_i, y_i in data for index_for_alpha_beta in range(2)]
    #
    # step_size_for_alpha_beta = [squared_error_gradient(x_i, y_i, theta, learning_rate) for x_i, y_i in data]
    # print(*step_size_for_alpha_beta)
    # return step_size_for_alpha_beta


# print ([squared_error_gradient(i, j, theta = [random.random(),
#                                               random.random()]) for i, j in zip(num_friends_three, daily_minutes)])

# random.seed(0)


# В ГЕНЕРАТОРЕ оценочных коэфф, alpha, beta ставим под индексы в соответствии их местам в функциях

# theta = [random.random(), random.random()]   # theta[0] - alpha, theta[1] - beta
theta = [0, 1]   # theta[0] - alpha, theta[1] - beta

# def minimize_stohastic(target_fn, gradient_fn, x, y,  theta_0, alfa_0 = 0.01):
#
#     data = list(zip(x, y))
#     print(data, ' data = list(zip(x, y))')
#     theta = theta_0  # theta - параметр от которого зависит выборка
#     alfa = alfa_0
#     min_theta, min_value = None, float('inf')
#     iterration_whis_no_improvement = 0
#     iterration_whis_no_improvement_condition_for_value = 0
#     while iterration_whis_no_improvement < 100 and iterration_whis_no_improvement_condition_for_value < 500:
#         value = sum (target_fn(x_i, y_i, theta) for x_i, y_i in data)# Сумма квадратов residual
#         if value < min_value  :
#             min_theta, min_value = theta, value
#             print(' ')
#             iterration_whis_no_improvement = 0
#             iterration_whis_no_improvement_condition_for_value += 1
#             print('\t' * 6, '*',iterration_whis_no_improvement_condition_for_value, '*' )
#             print(' ')
#             alfa = alfa_0
#         else:
#             iterration_whis_no_improvement += 1
#             print('\t' * 6, '<<',iterration_whis_no_improvement, '>>')
#             alfa *= 0.9
#             for x_i, y_i in in_random_order(data):
#                 print('\t'*10, alfa, ' alfa ')
#                 print('\t' * 2, value, ' value  <-->', min_value, ' min_value ')
#                 gradient_i = gradient_fn(x_i, y_i, theta) # градиент для theta i-ое
#                 print(gradient_i, ' gradient_i')
#                 print('\t' * 16, theta, ' theta_previous ')
#                 theta = vector_subtract(theta, scalar_multiplay(alfa, gradient_i))# вычисление следующ. theta
#                 print('\t'*16,  theta, ' theta ;', min_theta, ' min_theta >>')
#                 print(' ')
#     return min_theta # минимальное значение точки на графике -0.26141959552258875

# def minimize_stohastic(target_fn, gradient_fn, x, y,  theta_0, step = 0.01):
def minimize_stohastic(target_fn, gradient_fn, x, y, theta_0, step=0.01):
    print(theta_0, " >>>>>>>>>>>>theta_0", "\n")
    data = zip(x, y)
    theta = theta_0
    step_size_for_a_b = [squared_error_gradient(x_i, y_i, theta, 0.01) for x_i, y_i in data]
    print(*step_size_for_a_b, " step_size_for_a_b")
    # step_size_for_alpha_beta = step_size_alpha_beta(theta, data, 0.01)
    # print(*step_size_for_alpha_beta, " step_size_for_alpha_beta")


print(minimize_stohastic(squared_error, squared_error_gradient, num_friends_three, daily_minutes, theta))

# alpha, beta = minimize_stohastic(squared_error, squared_error_gradient, num_friends_three,
#                                  daily_minutes, theta, 0.0001)


# print(minimize_stohastic(square, derivative, x_for_sgd,  y_for_sgd , v_theta_for_sgd , alfa_0 = 0.01),
#                                ' minimize_stohastic')



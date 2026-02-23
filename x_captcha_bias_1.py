import math as mt
import numpy as np
import random
import logging
from math import exp

logging.basicConfig(
    level=logging.DEBUG,
    filename="x_o_r.log",
    filemode="w",
    format=" \n %(asctime)s \n %(levelname)s \n  %(message)s \n ",
)
logger = logging.getLogger("X_O_R")
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

# TODO start
input_size = 25
hidden_size = 5
output_size = 10

# TODO mid
"input_vector - пока список, чт/бы проще увеличивать на 1 для bia, плюсованием "
input_vector = [
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
]

target_vector = [[1 if i == j else 0 for i in range(10)] for j in range(10)]
# logger.debug((np.array (target_vector), "targets"))
# logger.debug((input_vector, "input_vector"))
random.seed(0)

hidden_layer = np.random.random((hidden_size, input_size))  # w входа
# hidden_layer = np.full((hidden_size, input_size), 0.5) # w входа
# hidden_layer = np.append(hidden_layer_, b)
logger.debug(("hidden_layer", hidden_layer))
output_layer = np.random.random((output_size, hidden_size))  # w выхода
# output_layer = np.full((output_size, hidden_size), 0.5)  # w выхода
# output_layer = np.append(output_layer_, b)
logger.debug(("output_layer", output_layer))

network = [hidden_layer, output_layer]


# i = [(x, y) for x, y in zip(target_vector, input_vector)]
# logger.debug(i)

b = 0.8  # bias


# TODO f_activ


def f_activ(x):
    return (mt.exp(x) - mt.exp(-x)) / (mt.exp(x) + mt.exp(-x))
    # return 1 / (1 + mt.exp(-x))


def f_deriv(y):
    return 1 - y**2
    # return y * (1 - y)


rng = np.random.default_rng()


def forward(w_hide, w_out, inp):
    #     indices = rng.integers(10, size=10)[0]  # Индекс для синхронизации input с target
    indices = 0
    #
    #     input_hide = np.array([np.dot(hidden_layer[r], inp[indices]) for r in range(hidden_size)]) # вход hide
    #     # input_hide_1 = np.array\
    #     #     ([np.dot(hidden_layer[r] + [b], inp[indices]) for r in range(hidden_size)])  # вход hide, bias * на каждый вес нейрона
    #     input_hide_2 = np.array\
    #         ([np.dot(np.append(hidden_layer[r], b), np.append(inp[indices], b)) for r in range(hidden_size)])  # one bias к строке
    #
    #     output_hide = np.array([f_activ(j) for j in input_hide])  # выход hide
    #     # output_hide_1 = np.array([f_activ(j)  for j in input_hide_1])  # выход hide
    #     output_hide_2 = np.array([f_activ(j) for j in input_hide_2])  # выход hide
    #
    #     input_output = np.array([np.dot(output_hide, output_layer[r]) for r in range(output_size)])  # вход out, r - receive
    #     # input_output_1 = np.array([np.dot(output_hide_1 + b, output_layer[r] + b) for r in range(output_size)])  # вход out, bias * на каждый вес нейрона
    #     input_output_2 = np.array([np.dot(np.append(output_hide_2, b), np.append(output_layer[r], b)) for r in range(output_size)])  # вход out, one bias к строке
    #
    #     exit_output = np.array([f_activ(j) for j in input_output])
    #     # exit_output_1 = np.array([f_activ(j) for j in input_output_1])
    #     exit_output_2 = np.array([f_activ(j) for j in input_output_2])
    #
    #
    #     error = (exit_output - np.array(target_vector[indices]) )  # Ошибку считаем простым вычитанием массивов
    #     # error_1 = (exit_output_1 - np.array(target_vector[indices]) )  # Ошибку считаем простым вычитанием массивов
    #     error_2 = (exit_output_2 - np.array(target_vector[indices]) )  # Ошибку считаем простым вычитанием массивов

    #     print(exit_output)
    #     print(indices, inp[indices])

    # logger.debug((input_hide, " input_hide"))
    logger.debug((hidden_layer[0:26], " input_hide_1"))
    # logger.debug((input_hide_2, " input_hide_2"))
    #
    # logger.debug((output_hide, " output_hide"))
    # logger.debug((output_hide_1, " output_hide_1"))
    # logger.debug((output_hide_2, " output_hide_2"))
    #
    # logger.debug((input_output, " input_output"))
    # logger.debug((input_output_1, " input_output_1"))
    # logger.debug((input_output_2, " input_output_2"))
    #
    # logger.debug((exit_output, " exit_output"))
    # logger.debug((exit_output_1, " exit_output_1"))
    # logger.debug((exit_output_2, " exit_output_2"))
    #
    # logger.debug((error, " error"))
    # logger.debug((error_1, " error_1"))
    # logger.debug((error_2, " error_2"))


#     # logger.debug((indices, " inp[indices]"))
#     # logger.debug((exit_output, " exit_output"))
#     # logger.debug((target_vector[indices], " inp[indices]"))

# return inp[indices], output_hide_2, exit_output_2, error_2, target_vector[indices], indices, exit_output

forward(hidden_layer, output_layer, input_vector)

# TODO back_prop
# N = 100
# for _ in range(N):
#     N -= 1
#     def back_prop(h_layer, o_layer, i_vector):
#         global hidden_layer, output_layer
#         inp_indices, output_hide, exit_output_2, error, targets, indices, exit_output = forward(h_layer, o_layer, i_vector)  # Переменные для back_prop
#         deltas_output = [f_deriv(i) for i in exit_output_2] * error  # LG выхода
#         output_layer = np.array([output_layer[:, r] - deltas_output * (output_hide[r]) for r in range(hidden_size)])
#         "# new_output_layer - новая матрица транспонировалась, где строки это принимающий слой hidden"
#         deltas_hide = np.array([np.dot(deltas_output, output_layer[r]) * f_deriv(output_hide[r])
#                                 for r in range(hidden_size)])
#         hidden_layer = np.array([hidden_layer[:, r] - deltas_hide * (inp_indices[r]) for r in range(input_size)])
#         output_layer, hidden_layer = output_layer.transpose(), hidden_layer.transpose()
#
#         # logger.debug((inp_indices, " inp_indices"))
#         # logger.debug((output_hide, " output_hide"))
#         # logger.debug((exit_output, " exit_output"))
#         # logger.debug((error, " error"))
#         # logger.debug((deltas_output, " deltas_output"))
#         # logger.debug((output_layer,  " new_output_layer", output_layer.shape))
#         # logger.debug((deltas_hide,  " deltas_hide"))
#         # logger.debug((hidden_layer,  " hide_layer", hidden_layer.shape))
#         if N == 0:
#             logger.debug((indices, " inp[indices]"))
#             logger.debug((N, exit_output, " exit_output "))
#             logger.debug((N, exit_output_2, " exit_output_2"))
#             logger.debug((N, targets, " targets"))
#             logger.debug((N, error, " error"))
#
#
#     back_prop(hidden_layer, output_layer, input_vector)

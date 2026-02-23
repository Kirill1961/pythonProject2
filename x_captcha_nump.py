import math as mt
import numpy as np
import random
import logging
from math import exp

logging.basicConfig(level=logging.DEBUG, filename="x_o_r.log", filemode="w"
                    , format=" \n %(asctime)s \n %(levelname)s \n  %(message)s \n ")
logger = logging.getLogger("X_O_R")
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

# TODO start
input_size = 25
hidden_size = 5
output_size = 10

# TODO mid
input_vector = [[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

target_vector = [[1 if i == j else 0 for i in range(10)] for j in range(10)]
# logger.debug((np.array (target_vector), "targets"))
# logger.debug((target_vector, "targets"))
random.seed(0)

hidden_layer = np.random.random((hidden_size, input_size))  # w входа
# logger.debug(("hidden_layer", hidden_layer[0:1]))
output_layer = np.random.random((output_size, hidden_size))  # w выхода
# logger.debug(("output_layer", output_layer))

network = [hidden_layer, output_layer]

# i = [(x, y) for x, y in zip(target_vector, input_vector)]


# logger.debug(i)

# TODO f_activ

def f_activ(x):
    # return (mt.exp(x) - mt.exp(-x)) / (mt.exp(x) + mt.exp(-x))
    return 1 / (1 + mt.exp(-x))


def f_deriv(y):
    # return 1 - y ** 2
    return y * (1 - y)



rng = np.random.default_rng()


def forward(w_hide, w_out, inp):
    indices = rng.integers(10, size=10)[0]  # Индекс для синхронизации input с target
    input_hide = [np.dot(hidden_layer[r], inp[indices]) for r in range(hidden_size)]  # вход hide, r - коэфф receive
    output_hide = np.array([f_activ(j) for j in input_hide])  # выход hide
    input_output = np.array([np.dot(output_hide, output_layer[r]) for r in range(output_size)])  # вход out, r - receive
    exit_output = np.array([f_activ(j) for j in input_output])
    error = (exit_output - np.array(target_vector[indices]) )  # Ошибку считаем простым вычитанием массивов
    # print(exit_output)
    # print(indices, inp[indices])

    # logger.debug((input_hide, " input_hide"))
    # logger.debug((output_hide, " output_hide"))
    # logger.debug((input_output, " input_output"))
    # logger.debug((exit_output, " exit_output"))
    # logger.debug((error, " error"))
    # logger.debug((indices, " inp[indices]"))
    # logger.debug((exit_output, " exit_output"))
    # logger.debug((target_vector[indices], " inp[indices]"))

    return inp[indices], output_hide, exit_output, error, target_vector[indices], indices


# forward(hidden_layer, output_layer, input_vector)


# # TODO back_prop
N = 1000
for _ in range(N):
    N -= 1
    def back_prop(h_layer, o_layer, i_vector):
        global hidden_layer, output_layer
        inp_indices, output_hide, exit_output, error, targets, indices = forward(h_layer, o_layer, i_vector)  # Переменные для back_prop
        deltas_output = [f_deriv(i) for i in exit_output] * error  # LG выхода
        output_layer = np.array([output_layer[:, r] - deltas_output * (output_hide[r]) for r in range(hidden_size)])
        "# new_output_layer - новая матрица транспонировалась, где строки это принимающий слой hidden"
        deltas_hide = np.array([np.dot(deltas_output, output_layer[r]) * f_deriv(output_hide[r])
                                for r in range(hidden_size)])
        hidden_layer = np.array([hidden_layer[:, r] - deltas_hide * (inp_indices[r]) for r in range(input_size)])
        output_layer, hidden_layer = output_layer.transpose(), hidden_layer.transpose()

        # logger.debug((inp_indices, " inp_indices"))
        # logger.debug((output_hide, " output_hide"))
        # logger.debug((exit_output, " exit_output"))
        # logger.debug((error, " error"))
        # logger.debug((deltas_output, " deltas_output"))
        # logger.debug((output_layer,  " new_output_layer", output_layer.shape))
        # logger.debug((deltas_hide,  " deltas_hide"))
        # logger.debug((hidden_layer,  " hide_layer", hidden_layer.shape))
        if N == 0:
            logger.debug((indices, " inp[indices]"))
            logger.debug((N, exit_output, " exit_output"))
            logger.debug((N, targets, " targets"))
            logger.debug((N, error, " error"))

    back_prop(hidden_layer, output_layer, input_vector)

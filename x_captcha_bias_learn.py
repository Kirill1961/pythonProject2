import math as mt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
from math import exp
import matplotlib as mp
import logging

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

np.random.seed(0)

hidden_layer = np.random.random((hidden_size, input_size))  # w входа
h = np.array(
    [
        [
            1.04457206,
            0.7005175,
            1.3269237,
            0.43039782,
            0.57558906,
            0.22771132,
            0.08416064,
            1.33981777,
            0.79301687,
            0.73060997,
            1.0135107,
            0.34450566,
            0.81047214,
            0.89240866,
            0.84983538,
            0.58288563,
            0.36252739,
            1.05209254,
            0.02718084,
            1.16794009,
            0.71969403,
            0.59171946,
            0.99168439,
            0.94241793,
            0.81981541,
        ],
        [
            -0.01455376,
            -2.4582373,
            -3.01952986,
            -2.48876941,
            -0.92192922,
            9.26620549,
            0.09364479,
            -0.38231971,
            0.1500222,
            -4.09830105,
            1.56218242,
            3.642489,
            2.41967441,
            3.43750488,
            -0.63888833,
            2.16217498,
            0.07666712,
            0.14029262,
            0.6715981,
            -1.77836167,
            -0.17918039,
            0.13561183,
            -1.08772649,
            0.09223883,
            -0.34202126,
        ],
        [
            -2.55624594,
            -0.29329306,
            -2.32239688,
            -0.42129324,
            -1.86060656,
            2.36439606,
            0.95409111,
            -1.59985396,
            0.42543813,
            9.17454587,
            0.39579092,
            0.19882693,
            -2.25557392,
            0.32968298,
            -1.69921898,
            4.12359693,
            0.50791636,
            -1.26520321,
            0.99296011,
            -3.40873052,
            2.55051823,
            2.33053669,
            0.57999598,
            2.01623189,
            -2.25759094,
        ],
        [
            -1.02454795,
            0.92964898,
            1.38155848,
            0.81896337,
            -0.73615393,
            4.45524202,
            0.03635522,
            1.22410636,
            0.49533135,
            -3.92496701,
            -1.76106893,
            -1.89597905,
            -1.19852305,
            -2.13357402,
            -0.95592431,
            8.77971864,
            0.12882256,
            1.37330489,
            0.74367587,
            1.77257077,
            -0.32406046,
            -0.03291826,
            0.58092544,
            -0.18790074,
            -0.80288389,
        ],
        [
            0.45193728,
            0.51011423,
            1.4856004,
            0.65537274,
            0.74779625,
            0.85048693,
            0.21903828,
            0.95112039,
            0.81858688,
            1.14640717,
            0.27429063,
            0.11630527,
            1.53690066,
            0.42889072,
            0.95866857,
            0.81674689,
            0.98512558,
            1.44072513,
            0.9928642,
            0.77799108,
            0.94307626,
            0.69785271,
            0.6822101,
            0.35950258,
            0.92273041,
        ],
    ]
)
# hidden_layer = np.append(hidden_layer_, b)
logger.debug(("hidden_layer", hidden_layer))
# print(hidden_layer)
output_layer = np.random.random((output_size, hidden_size))  # w выхода
o = np.array(
    [
        [-4.40656266, -7.3548543, 5.28542231, 7.04010272, -4.74056654],
        [-2.27569009, -5.98858785, -11.06668669, 7.11394076, -1.19012386],
        [-4.56065222, -2.50016168, 10.83385147, -3.35721551, -4.5825812],
        [-0.35175304, -11.06200826, 3.08238117, -11.30579502, -0.66683475],
        [-2.49638379, 8.02059201, -4.4246393, -14.61243489, -3.11925209],
        [-1.95163299, 5.34358798, -13.90685129, -1.27638607, -1.99197095],
        [-7.55285813, 6.47043023, -4.7874364, 11.30107408, -7.85474729],
        [1.24977519, -18.37273152, -7.71919658, -3.23768736, 1.0440221],
        [-7.92548555, 5.99268003, 7.60897747, 5.15165667, -8.05695198],
        [-6.47549645, 7.75734858, 7.87556613, -7.30833156, -5.77574742],
    ]
)
# output_layer = np.append(output_layer_, b)
logger.debug(("output_layer", output_layer))

network = [hidden_layer, output_layer]


# i = [(x, y) for x, y in zip(target_vector, input_vector)]
# logger.debug(i)


def f_activ(x):
    # return (mt.exp(x) - mt.exp(-x)) / (mt.exp(x) + mt.exp(-x))
    return 1 / (1 + mt.exp(-x))


def f_deriv(y):
    # return 1 - y ** 2
    return y * (1 - y)


rng = np.random.default_rng()

b = 1  # bias


# TODO forward
def forward(w_hide, w_out, inp, indices):
    indices = (
        rng.integers(10, size=10)[0] if indices is None else indices
    )  # Индекс для синхронизации input с target
    # indices = 0
    # print(indices)
    global b
    for _ in range(hidden_size):
        # print(b)
        input_hide = np.array(
            [np.dot(hidden_layer[r], inp[indices]) for r in range(hidden_size)]
        )  # вход hide
        "bias прибавляем к просуммированным весам"
        input_hide_1 = np.array(
            [np.dot(hidden_layer[r], inp[indices]) + b for r in range(hidden_size)]
        )  # вход hide, bias * на каждый вес нейрона
        # input_hide_2 = np.array\
        #     ([np.dot(np.append(hidden_layer[r], b), np.append(inp[indices], b)) for r in range(hidden_size)])  # one bias к строке
        # print(input_vector[indices])

        output_hide = np.array([f_activ(j) for j in input_hide])  # выход hide
        output_hide_1 = np.array([f_activ(j) for j in input_hide_1])  # выход hide
        # output_hide_2 = np.array([f_activ(j) for j in input_hide_2])  # выход hide

        input_output = np.array(
            [np.dot(output_hide, output_layer[r]) for r in range(output_size)]
        )  # вход out, r - receive
        "bias прибавляем к просуммированным весам"
        input_output_1 = np.array(
            [(np.dot(output_hide_1, output_layer[r])) + b for r in range(output_size)]
        )
        # input_output_2 = np.array([np.dot(np.append(output_hide_2, b), np.append(output_layer[r], b))

        exit_output = np.array([f_activ(j) for j in input_output])
        exit_output_1 = np.array([f_activ(j) for j in input_output_1])
        # exit_output_2 = np.array([f_activ(j) for j in input_output_2])

        error = exit_output - np.array(
            target_vector[indices]
        )  # Ошибку считаем простым вычитанием массивов
        error_1 = exit_output_1 - np.array(
            target_vector[indices]
        )  # Ошибку считаем простым вычитанием массивов
        # error_2 = (exit_output_2 - np.array(target_vector[indices]) )  # Ошибку считаем простым вычитанием массивов

        "GD для bias"
        b_i = 1 / (1 + mt.exp(-b))  # пропустили bias через активацию
        b -= b_i * (1 - b_i) * 0.1  # делаем GD для dias
        # print(b)

        return (
            inp[indices],
            output_hide_1,
            exit_output_1,
            error_1,
            target_vector[indices],
            indices,
            exit_output,
            b,
        )


# forward(hidden_layer, output_layer, input_vector, indices=0)

# TODO back_prop
N = 1
for _ in range(N):
    N -= 1

    def back_prop(h_layer, o_layer, i_vector):
        global hidden_layer, output_layer
        (
            inp_indices,
            output_hide,
            exit_output_1,
            error,
            targets,
            indices,
            exit_output,
            b_,
        ) = forward(
            h_layer, o_layer, i_vector, indices=None
        )  # Переменные для back_prop
        deltas_output = np.array(
            [f_deriv(i) for i in exit_output_1] * error
        )  # LG выхода
        output_layer = np.array(
            [
                output_layer[:, r] - deltas_output * (output_hide[r])
                for r in range(hidden_size)
            ]
        )
        "# new_output_layer - новая матрица транспонировалась, где строки это принимающий слой hidden"
        deltas_hide = np.array(
            [
                np.dot(deltas_output, output_layer[r]) * f_deriv(output_hide[r])
                for r in range(hidden_size)
            ]
        )
        hidden_layer = np.array(
            [
                hidden_layer[:, r] - deltas_hide * (inp_indices[r])
                for r in range(input_size)
            ]
        )
        output_layer, hidden_layer = output_layer.transpose(), hidden_layer.transpose()

        if N == 0:
            logger.debug((indices, " indices"))
            logger.debug((b_, " b_"))
            logger.debug(
                (
                    N,
                    [1 if x > 0.5 else 0 for x in exit_output],
                    " exit_output without bias",
                )
            )
            logger.debug(
                (
                    N,
                    [1 if x > 0.5 else 0 for x in exit_output_1],
                    " exit_output_1 with  bias",
                )
            )
            logger.debug((N, targets, " targets"))
            logger.debug((N, error, " error"))
            logger.debug((hidden_layer, " hide_layer"))
            logger.debug((output_layer, " new_output_layer"))

    back_prop(hidden_layer, output_layer, input_vector)
#
# def predict(indices):
#     print(indices, " predict")
#     inp_indices, output_hide, exit_output_1, error, targets, indices, exit_output = forward(hidden_layer, output_layer, input_vector, indices)
#     logger.debug(indices)
#     logger.debug(np.array(inp_indices).reshape(5, 5))
#     logger.debug(( targets, " targets"))
#     logger.debug((np.array([1 if x > 0.5 else 0 for x in exit_output]), " exit_output "))
#     logger.debug(([1 if x > 0.5 else 0 for x in exit_output_1], " exit_output_1"))
# predict(6)


# TODO math

weights = hidden_layer[0]
abs_weights = list(map(abs, weights))

grid = np.array(abs_weights).reshape(5, 5)
logger.debug(grid)
ax = plt.gca()
ax.imshow(grid, cmap=mp.cm.binary, interpolation="none")


def patch(x, y, hatch, color):
    return matplotlib.patches.Rectangle(
        (x - 0.5, y - 0.5), 1, 1, hatch=hatch, fill=False, color=color
    )


for i in range(5):
    for j in range(5):
        print(i, j)
        # ax.add_patch(matplotlib.patches.Rectangle((j- 0.5, i - 0.5 ), 0.7, 0.5, hatch='o', fill=False, color='red'))
        if weights[5 * i + j] < 0:
            ax.add_patch(patch(j, i, '/', "red"))
            ax.add_patch(patch(j, i, '\\', "black"))


for i in range(5):
    for j in range(5):
        print(weights)
        # ax.add_patch(matplotlib.patches.Rectangle((j- 0.5, i - 0.5 ), 0.7, 0.5, hatch='o', fill=False, color='red'))
        if weights[5 * i + j] < 0:
            ax.add_patch(patch(j, i, '/', "red"))
            ax.add_patch(patch(j, i, '\\', "black"))
n = [weights[i] for i in range(25)]
n = [(ax.add_patch(patch(j, i, '*', "red")), ax.add_patch(patch(j, i, '\\', "black"))) for j in range(5)  for i in range(5)]
print(n)


plt.show()

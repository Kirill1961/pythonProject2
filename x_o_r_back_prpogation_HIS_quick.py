import math as mt
import numpy as np
from numpy import dot
import logging
import random
# import itertools
from itertools import accumulate

logging.basicConfig(level=logging.DEBUG, filename="x_o_r.log", filemode="w")
# format="%(asctime)s %(levelname)s %(message)s")


#  регистраторы никогда не должны создаваться напрямую, а всегда через функцию уровня модуля logging.getLogger(name).
logger = logging.getLogger("X_O_R")

# logging.disable() # отключение логгера, если проставить в арг цифру уровня то будет отключ только этот уровень

# Добавлен обработчик для вывода в косоль
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)  # если поставим уровень INFO, то добавленный обработчик sh невыводит в консоль
# logger.addHandler(sh)

print(logger, " рутовое имя")

print(logger.handlers, "наличие обработчиков", "\n")  # наличие обработчиков

h = np.random.random((1, 2, 3))
o = np.random.random((1, 1, 3))
xor_network = np.block([[h], [o]])

# TODO: correct data
# xor_network = [[[10, 10, -30],
#                 [20, 20, -10],
#                 [-60, 60, -30]]]
# TODO: incorrect data
# xor_network = [[[0.5, 0.5, -3],
#                 [2, 2, -1],
#                 [-0.5, 0.5, -3]]]
# xor_network = [[[5, 5, -3],
#                 [3, 7, -1],
#                 [-6, 6, -3]]]

# xor_network = [[[0.5, 0.1, -0.15],
#                 [0.15, 0.5, -0.2],
#                 [-0.45, 0.15, -0.1]]]

logger.debug(xor_network)
print(xor_network)


# logger.debug(xor_network)


def sigmoid(t):
    return 1 / (1 + mt.exp(-t))


# print(sigmoid(10))


def neuron_output(weights, inputs):
    # logger.debug(((weights, inputs), " weights, inputs"))
    # logger.debug((dot(weights, inputs), " input_for_last_neuro"))
    return sigmoid(dot(weights, inputs))


def feed_forward():
    # logger.debug((xor_network , i, ">>>>>>>>>>>>>>>>>>>>>>"))
    target_for_bp = []

    # TODO: feed_forward
    def inner_feed_forward(neural_network, input_vector):
        # logger.debug((neural_network, "neural_network"))
        global output_layer_hide
        outputs = []
        # logger.debug(targ)
        for layer in neural_network:
            input_with_bias = input_vector + [1]  # добавив 1 к [x, y] сравняем LEN вх с LEN скрытого слоя
            output_hide_without_bias = [neuron_output(neuron, input_with_bias) for neuron in layer[0:2]]  # выходы
            # из hide  для last_neuron без bias:
            outputs.append(output_hide_without_bias[0:2])

            output_layer_hide = outputs[0] + [1]  # выходной вектор из скрытого добавляем + [1] для bias -30
            output_last_neuro = [neuron_output(layer[-1], output_layer_hide)]  # выход выхода

            targets_bound_inputs = [0 if input_with_bias[0] == input_with_bias[1] else 1]  # привязка inputs к targets
            target_for_bp.append(targets_bound_inputs)
            if input_vector == [0, 0] and range_N > N - 15:
                logger.debug((range_N, input_vector, target_for_bp[-1], output_last_neuro))
            elif input_vector == [0, 1] and range_N > N - 15:
                logger.debug((range_N, input_vector, target_for_bp[-1], output_last_neuro))
            elif input_vector == [1, 0] and range_N > N - 15:
                logger.debug((range_N, input_vector, target_for_bp[-1], output_last_neuro))
            elif input_vector == [1, 1] and range_N > N - 15:
                logger.debug((range_N, input_vector, target_for_bp[-1], output_last_neuro))
            # logger.debug((input_vector, target_for_bp[-1], output_last_neuro,  " >>>>"))
            return output_hide_without_bias, output_last_neuro, target_for_bp

    return inner_feed_forward


wrap_feed = feed_forward()
n = 0
# TODO: while learn
# while n < 1000:
#     n += 1
N = 1000
for range_N in range(N):
    # logger.debug(range_N)
    # logger.debug("\n" * 2)
    inputs_total = [[x, y] for x in [0, 1] for y in [0, 1]]
    # for input_separate in inputs_total:
    input_separate_with_bias = inputs_total[random.randint(0, len(inputs_total) - 1)]
    # print(input_separate_with_bias)


    # logger.debug((input_separate))

    # logger.debug("\n")

    def backprpogate(network, input_vektor, wrap_feed_forward):

        global hidden_deltas
        args_from_feed_forward = wrap_feed_forward(network, input_vektor)
        hidden_outputs = args_from_feed_forward[0] + [1]  # выход скрытого слоя
        outputs = args_from_feed_forward[-2]  # выход последнего слоя
        t = args_from_feed_forward[-1]  # целевое значение
        targets = list(j for i in t for j in i)  # целевое значение

        # logger.debug([(output * (1 - output), output, target) for output, target in zip(outputs, [targets[-1]])])

        outputs_deltas = [output * (1 - output) * (output - target) for  # LG выходного слоя
                          output, target in zip(outputs, [targets[-1]])]  # кортежи output/target для error

        # TODO: MY
        """ MY код для одного выходного нейрона"""
        """ HIS код для нескольких выходных нейронов """
        for i, output_neuron in enumerate([xor_network[0][-1]]):  # i нумерация нейронов выходного слоя
            # logger.debug((xor_network[0][-1], "i,  output_weight"))
            for j, hidden_output in enumerate(hidden_outputs):  # j нумерация нейронов скрытого слоя
                logger.debug((output_neuron[j], outputs_deltas[i], hidden_output, " outputs_deltas * hidden_output"))
                output_neuron[j] -= (outputs_deltas[i] * hidden_output)  # новый вес выхода
                output_layer = output_neuron  # новый вес выхода
                output_deltas = outputs_deltas[i]  # LG выхода

                hidden_deltas = [hidden_output * (1 - hidden_output)  # LG скрытого слоя
                                 * dot(output_deltas, [n[i] for n in [output_layer]])  # dot LG выхода/новые веса выхода
                                 for i, hidden_output in enumerate(hidden_outputs)]  # выходы скрытого СЛ без bias

            for i, hidden_neuron in enumerate(xor_network[0][0:2]):  # веса скрытого, i - номер скрытого
                for j, input in enumerate(input_vektor + [1]):  # j - номер входного
                    hidden_neuron[j] -= (hidden_deltas[i][0] * input)  # новый вес скрытого


    backprpogate(xor_network, input_separate_with_bias, wrap_feed)

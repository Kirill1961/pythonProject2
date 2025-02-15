import math as mt
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
# TODO: correct data
# xor_network = [[[20, 20, -30],
#                 [20, 20, -10],
#                 [-60, 60, -30]]]
# TODO: incorrect data
xor_network = [[[1, 1, -3],
                [1, 1, -1],
                [-6, 6, -3]]]



# xor_network = [[[1, 0.5, -3],
#             [1.3, 4.2, 0.5],
#             [-3.1, 2, 0.7]]]

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
            # [0, 0, 1], [[20, 20, -30]
            # logger.debug((layer[0:2], input_with_bias, "neuron, input_with_bias"))

            # выходы   из hide  для last_neuron без bias:
            output_hide_without_bias = [neuron_output(neuron, input_with_bias) for neuron in layer[0:2]]


            #     logger.debug((neuron, input_with_bias, "neuron_input_with_bias")ы
            outputs.append(output_hide_without_bias[0:2])

            # input_vector = output_hide_and_last_layer

            output_layer_hide = outputs[0] + [1]  # выходной вектор из скрытого добавляем + [1] для bias -30
            # logger.debug((output_layer_hide, "output_hide_with_bias"))
            output_last_neuro = [neuron_output(layer[-1], output_layer_hide)]  # выход выхода
            # logger.debug((output_layer_hide, "output_layer_hide"))

            targets_bound_inputs = [0 if input_with_bias[0] == input_with_bias[1] else 1]  # привязка inputs к targets
            target_for_bp.append(targets_bound_inputs)
            # logger.debug((output_last_neuro, "output_last_neuro"))
            # logger.debug(
            #     ("dot", layer[0:2], input_with_bias, " = ", output_hide_without_bias, "output_hide_without_bias"))
            return output_hide_without_bias, output_last_neuro, target_for_bp

    return inner_feed_forward


# wraps_feed = feed_forward()
# inputs_total = [[x, y] for x in [0, 1] for y in [0, 1]]
# for input_separate in inputs_total:
#     print(input_separate)
# print("вход - ", input_separate, " , выход - ", wraps_feed(xor_network, input_separate))


wrap_feed = feed_forward()
n = 0
# TODO: while learn
N = 1000
while n < N:
    n += 1
    # logger.debug(n)
    # logger.debug("\n" * 2)
    inputs_total = [[x, y] for x in [0, 1] for y in [0, 1]]
    # for input_separate in inputs_total:
    input_separate_with_bias = inputs_total[random.randint(0, len(inputs_total) - 1)]
    # print(input_separate_with_bias)
    # logger.debug((input_separate))

    # logger.debug("\n")


    # print("вход - ", input_separate, " , выход - ", wraps_feed(xor_network, input_separate))
    def backprpogate(network, input_vektor, wrap_feed_forward):
        #  wrap_feed_forward - вызов прямого распространения
        #  network - Веса слоёв: [1, 1, -3] и [1, 1, -1] Среднего и [-6, 6, -3] выходного слоя
        #  input_vektor - Входной вектор в перцептрон, сгенерированный

        global hidden_deltas, n
        args_from_feed_forward = wrap_feed_forward(network, input_vektor)  # Запуск Прямого распространения
        hidden_outputs = args_from_feed_forward[0] + [1]  # выход скрытого слоя
        outputs = args_from_feed_forward[-2]  # выход последнего слоя
        t = args_from_feed_forward[-1]  # целевое значение
        targets = list(j for i in t for j in i)  # целевое значение
        if input_separate_with_bias == [0, 0] and n > N - 10:
            logger.debug((n, input_separate_with_bias, outputs))
        elif input_separate_with_bias == [0, 1] and n > N - 10 :
            logger.debug((n, input_separate_with_bias, outputs))
        elif input_separate_with_bias == [1, 0] and n > N - 10:
            logger.debug((n, input_separate_with_bias, outputs))
        elif input_separate_with_bias == [1, 1] and n > N - 10:
            logger.debug((n, input_separate_with_bias, outputs))



        # logger.debug((n, input_separate_with_bias, outputs))


        outputs_deltas = [output * (1 - output) * (output - target) for  # LG выходного слоя
                          output, target in zip(outputs, [targets[-1]])]  # кортежи output/target для error
        # logger.debug((outputs_deltas, "outputs_deltas"))

        # TODO: MY
        """ MY код для одного выходного нейрона"""

        for k, outputs in enumerate(args_from_feed_forward[-2]):  # k - номера выходных нейронов
            # logger.debug((k, outputs, "outputs"))

            for i, hidden_output in enumerate(hidden_outputs):  # вых. hide слоя + [1]bias, i-№ нейронов скрытого слоя
                xor_network[0][-1][i] -= outputs_deltas[0] * hidden_output  # новые веса выходного слоя
                hidden_deltas = hidden_output * (1 - hidden_output) * \
                                dot(outputs_deltas[0], xor_network[0][-1][i])  # LG скрытого слоя [-60,60,30]
                # logger.debug((xor_network[0][-1][i], "new_weight"))
                # logger.debug(( hidden_deltas, "<<<<"))

                for j, input_x in enumerate(input_vektor + [1]):  # j - № нейрона входного слоя, + [1] для bias
                    mul_grad_by_input = hidden_deltas * input_x
                    new_weight = [k for k in xor_network[0]][i][j] - mul_grad_by_input  # прежний вес минус GL * вход
                    # logger.debug (([j], hidden_deltas, " * ",  input_x,  " = ", mul_grad_by_input, " >>>>"))
                    # logger.debug(({i},  input_x, " * ",hidden_deltas, " = ", mul_grad_by_input,  # !!!!!!!!
                    #               [k for k in xor_network[0]][i][j]))

        # logger.debug(( hidden_outputs))
        """ HIS код для нескольких выходных нейронов """
        # for i, output_neuron in enumerate([xor_network[0][-1]]):   # i нумерация нейронов выходного слоя
        #     # logger.debug((xor_network[0][-1], "i,  output_weight"))
        #     for j, hidden_output in enumerate(hidden_outputs):  # j нумерация нейронов скрытого слоя
        #         output_neuron[j] -= (outputs_deltas[i] * hidden_output  )  # новый вес выхода
        #         output_layer = output_neuron  # новый вес выхода
        #         output_deltas = outputs_deltas[i]  # LG выхода
        #
        #         hidden_deltas = [hidden_output * (1 - hidden_output)  # LG скрытого слоя
        #                          * dot(output_deltas , [n[i] for n in [output_layer]])  # dot LG выхода/новые веса выхода
        #                          for i, hidden_output in enumerate(hidden_outputs)]  # выходы скрытого СЛ без bias
        #
        #     for i, hidden_neuron in enumerate(xor_network[0][0:2]):   # веса скрытого, i - номер скрытого
        #         for j, input in enumerate(input_vektor + [1]):   # j - номер входного
        #             hidden_neuron[j] -= (hidden_deltas[i][0] * input )  # новый вес скрытого



    backprpogate(xor_network, input_separate_with_bias, wrap_feed)

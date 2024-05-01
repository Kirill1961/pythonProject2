import math as mt
from numpy import dot
import logging
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

# xor_network = [[[20, 20, -30],
#                 [20, 20, -10],
#                 [-60, 60, -30]]]

xor_network = [[[1, 1, -3],
                [1, 1, -1],
                [-6, 6, -3]]]
# TODO: xor_network
input_x_y = [[0, 0], [0, 1], [1, 0], [1, 1]]  # Генерируется в коде
target_output = [0, 1, 1, 0]  # targ выходы для соотв входов

# xor_network = [[[15, 3, -30],
#                 [1, 16, -10],
#                 [-1, -87, -30]]]

logger.debug(xor_network)
print(xor_network)

def sigmoid(t):
    return 1 / (1 + mt.exp(-t))





def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))

#  TODO feed_forward
def feed_forward():

    target_for_bp = []

    def inner_feed_forward(neural_network, input_vector):
        # logger.debug((neural_network, input_vector))
        global output_layer_hide
        outputs = []
        # logger.debug(targ)
        for layer in neural_network:

            input_with_bias = input_vector + [
                1]  # добавив 1 к [x, y] сравняем LEN вх с LEN слоя  [0, 0, 1], [[20, 20, -30]
            output_hide_and_last_layer = [neuron_output(neuron, input_with_bias) for neuron in layer]
            outputs.append(output_hide_and_last_layer[0:2])
            output_layer_hide = outputs[0] + [1]  # во входной вектор добавляем + [1] для bias -30
            output_by_last_neuro = [neuron_output(layer[-1], output_layer_hide)]  # передам в сигму вход для last_neuro
            targets_bound_inputs = [0 if input_with_bias[0] == input_with_bias[1] else 1]  # привязка inputs к targets
            target_for_bp.append(targets_bound_inputs)

            return output_hide_and_last_layer[0:2], output_by_last_neuro, target_for_bp

    return inner_feed_forward

wrap_feed = feed_forward()
N=5000
for range_N in range(N):
    inputs_total = [[x, y] for x in [0, 1] for y in [0, 1]]
    for input_separate_with_bias in inputs_total:
        # print(input_separate_with_bias)


#  TODO: MY
        # print("вход - ", input_separate, " , выход - ", wraps_feed(xor_network, input_separate))
        def backprpogate(network, input_vektor, wrap_feed_forward):
            args_from_feed_forward = wrap_feed_forward(network, input_vektor)
            hidden_outputs = args_from_feed_forward[0]  # выход скрытого слоя
            outputs = args_from_feed_forward[-2]  # выход последнего слоя
            t = args_from_feed_forward[-1]  # целевое значение
            targets = list(j for i in t for j in i)  # целевое значение
            outputs_deltas = [output * (1 - output) * (output - target) for  # loc_grad выходного слоя
                              output, target in zip(outputs, [targets[-1]])]
            if range_N == N - 1:
                logger.debug((range_N, input_vektor,  t[-1], outputs))
            """ MY код для одного выходного нейрона"""
            for i, hidden_output in enumerate(hidden_outputs):  # выходы скрытого слоя, i - № нейронов скрытого слоя
                xor_network[0][-1][i] -= outputs_deltas[0] * hidden_output  # новые веса выходного слоя [-60,60,30]

                hidden_deltas = hidden_output * (1 - hidden_output) * dot(outputs_deltas[0],
                                                                          xor_network[0][-1][
                                                                              i])  # LG скрытого слоя [-60,60,30]
                for j, input_x in enumerate(input_vektor):  # j - № нейрона входного слоя
                    mul_grad_by_input = hidden_deltas * input_x
                    # logger.debug( xor_network[0][i])
                    xor_network[0][0:2][i][0:2] -= mul_grad_by_input



            """ HIS код для нескольких выходных нейронов """
            # for i, output_neuron in enumerate([xor_network[0][-1]]):   # i нумерация нейронов выходного слоя
            #     # logger.debug((xor_network[0][-1], "i,  output_weight"))
            #     for j, hidden_output in enumerate(hidden_outputs):  # j нумерация нейронов скрытого слоя
            #         output_neuron[j] -= outputs_deltas[i] * hidden_output  # новый вес выхода
            #         output_layer = output_neuron  # новый вес выхода
            #         output_deltas = outputs_deltas[i]  # LG выхода
            #
            #         hidden_deltas = [hidden_output * (1 - hidden_output)  # LG скрытого слоя
            #                          * dot(output_deltas, [n[i] for n in [output_layer]])  # dot LG выхода/новые веса выхода
            #                          for i, hidden_output in enumerate(hidden_outputs)]  # выходы скрытого СЛ без bias
            #
            #     for i, hidden_neuron in enumerate(xor_network[0][0:2]):  # i нумерация нейронов скрытого слоя
            #         for j, input in enumerate(input_separate):    # j входных нейронов
            #             mul_gl_by_input = [k * v for k in hidden_deltas[i] for v in input_separate]  # mul GL * input
            #             new_weight = [i - j for i, j in zip(xor_network[0][0:2][i][0:2], mul_gl_by_input)]
            #         # logger.debug(([i], hidden_deltas, input_separate, mul_gl_by_input, "mul_gl_by_input"))
            #         logger.debug(([i], new_weight, outputs, "new_weight_outputs"))  # новые веса скрытого и выход


        backprpogate(xor_network, input_separate_with_bias, wrap_feed)

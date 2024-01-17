import math as mt
from numpy import dot


def sigmoid(t):
    return 1 / (1 + mt.exp(-t))


# print(sigmoid(10))


def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))


def feed_forward(neural_network, input_vector):
    outputs = []
    for layer in neural_network:
        input_with_bias = input_vector + [1]
        output = [neuron_output(neuron, input_with_bias) for neuron in layer]
        outputs.append(output)
        input_vector = output
    return outputs

import torch
import torch.nn as nn
import numpy as np
import math

# Входные данные
x = torch.tensor([0.8, 0.3])  # x1 = 0.8, x2 = 0.3
w = torch.tensor([0.6, 0.9])  # w1 = 0.6, w2 = 0.9

# Вычисление взвешенной суммы
S = torch.sum(x * w)  # 0.8 * 0.6 + 0.3 * 0.9 = 0.48 + 0.27 = 0.75

# Применяем Threshold
activation = nn.Threshold(threshold=0.5, value=-1.0)
output = activation(S)
# print("Выходное значение:", output.item())  # Ожидаем 0.75 (т.к. > 0.5)

'''
torch.tensor  - Перцептроны логических элементов И и ИЛИ,
используем tensor
'''

# TODO Логические элементы с использованием torch.tensor
# Исходные данные, пары входных Х -> 0 или 1
x = np.array([[0, 1],
              [0, 0],
              [1, 1],
              [1, 0],
              [1, 1]])

# Данные - пары входных Х > или = 1 для двух входных перцептронов
# x = np.array([[0.70328048, 0.5742928],
#        [0.6736352 , 1.41190483],
#        [1.29315472, 0.91953589],
#        [1.28418402, 1.78066096],
#        [1.22075356, 1.27996567]])

# TODO веса
w = np.array([0.5, 0.5])  # веса

# TODO Элемент И, Перцептрон с порогом 0,5
for i in range(len(x)):
    x_weight = np.dot(w, x[i])  # Взвешенный X
    x_tens = torch.tensor(x_weight)  # Преобразование в Тензор

    # TODO Используем Threshold как активацию с порогом 0,5
    #   value=0.0 - это значение которое подставляется если вход ниже порога
    #   Threshold — это как простая ступенчатая функция активации:
    #   если "сигнал слишком слабый", заменяем его на "тишину" (value).


    threshold = torch.nn.Threshold(threshold=0.5, value=0.0)
    activated_output = threshold(x_tens)
    print(f"Activated output ws threshold 0.5: {activated_output}")


# TODO использую torch.tensor - Элемент ИЛИ, Мой перцептрон с порогом 0,2
''' tensor - строг к типам данных надо явно приводить данные к одному типу!'''
x = torch.tensor(
                [[0, 1],
                 [0, 0],
                 [1, 1],
                 [1, 0],
                 [1, 1]],
                dtype=torch.float32  # Приводим к float
                )

w = torch.tensor([0.5, 0.5])

for i in range(len(x)):
    x_weight_tensor = torch.dot(w, x[i])  # Взвешенный Х

    threshold = torch.nn.Threshold(threshold=0.2, value=0.0)  # Создаём ОБ библиотеки Threshold

    output = threshold(x_weight_tensor)
    print(f'Активизация с порогом 0,2 : {output}')

'''
np.array - Перцептроны логических элементов И и ИЛИ,
используем  array
'''

# TODO элемент И
# Исходные данные, пары входных Х -> 0 или 1
x = np.array([[0, 1],
              [0, 0],
              [1, 1],
              [1, 0],
              [1, 1]]
             )

# веса
w = np.array([0.5, 0.5])

# TODO bais - вычислил вручную
b = -0.7


def sigma(x):
    return 1 / (1 + np.exp(-x))  # Без добавления bias внутри!


for i in range(len(x)):
    # TODO bais - прибавляется к суммарному входу перцептрона
    x_weight = np.dot(w, x[i]) + b  # Взвешенный вход + bias

    neuron_output = sigma(x_weight)
    # Округляем, чтобы получить чёткий 0 или 1
    print(
        f"Вход: {x[i]}, Взвешенный вход: {x_weight:.3f}, Выход: {neuron_output:.3f}, Округленный: {round(neuron_output)}")



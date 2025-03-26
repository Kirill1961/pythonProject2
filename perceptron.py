import torch
import torch.nn as nn
import numpy as np
# Входные данные
x = torch.tensor([0.8, 0.3])  # x1 = 0.8, x2 = 0.3
w = torch.tensor([0.6, 0.9])  # w1 = 0.6, w2 = 0.9

# Вычисление взвешенной суммы
S = torch.sum(x * w)  # 0.8 * 0.6 + 0.3 * 0.9 = 0.48 + 0.27 = 0.75

# Применяем Threshold
activation = nn.Threshold(threshold=0.5, value=-1.0)
output = activation(S)

# print("Выходное значение:", output.item())  # Ожидаем 0.75 (т.к. > 0.5)

# TODO Данные - пары входных Х меньше 1 для двух входных перцептронов
# Исходные данные
# x = np.array([[0.03942177, 0.67227638],
#               [0.47916114, 0.37383578],
#               [0.68489155, 0.74104129],
#               [0.06193587, 0.09273794],
#               [0.08033752, 0.822498]])

# TODO Данные - пары входных Х > или = 1 для двух входных перцептронов
x = np.array([[0.70328048, 0.5742928],
       [0.6736352 , 1.41190483],
       [1.29315472, 0.91953589],
       [1.28418402, 1.78066096],
       [1.22075356, 1.27996567]])

# TODO веса
w = np.array([0.2, 0.2])  # веса


# TODO Перцептрон с порогом 0,5
# Применение взвешенного значения
for i in range(len(x)):
    x_weight = np.dot(w, x[i])  # Взвешенный X

# TODO  Преобразование в тензор
    x_tens = torch.tensor(x_weight)  # Преобразование в Тензор

# TODO Используем Threshold как активацию
    threshold = torch.nn.Threshold(threshold=0.5, value=0.0)
    activated_output = threshold(x_tens)  # Применяем порог
    print(f"Activated output ws threshold 0.5: {activated_output}")


# TODO Мой перцептрон с порогом 0,3
for i in range(len(x)):
    x_weight = np.dot(w, x[i])  # Взвешенный Х

    x_tens = torch.tensor(x_weight)  # Преобразование в Тензор

    threshold = torch.nn.Threshold(threshold=0.3, value=0.0)  # Создаём ОБ библиотеки  Threshold

    output = threshold(x_tens)
    print(f'Активизация с порогом 0,3 : {output}')
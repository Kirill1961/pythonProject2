import numpy as np
import torch
import numpy as np

# TODO torch.nn — это модуль нейронных сетей (Neural Networks) в PyTorch
import torch.nn as nn

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Пример использования
x = np.array([-2, -1, 0, 1, 2])
print(sigmoid(x))



def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# Пример использования
x = np.array([-2, -1, 0, 1, 2])
print(sigmoid(x))




# TODO torch.tensor -> Создаёт многомерный массив (тензор) для чисел, аналогично numpy.array().
x = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0])
print(torch.sigmoid(x))

# TODO АКтивация, Применение torch.clamp (ограничение значений)
x = torch.tensor([-1.0, 0.5, 2.0, 3.5])
clamped_x = torch.clamp(x, min=0.0, max=1.0)
print(clamped_x)  # tensor([0. , 0.5, 1. , 1. ])



# TODO АКтивация, Использование torch.where (пороговое значение)
x = torch.tensor([0.2, 0.6, 0.8, 0.1])
threshold = 0.5

# Если x >= threshold, заменяем на 1, иначе на 0
binary_x = torch.where(x >= threshold, torch.tensor(1.0), torch.tensor(0.0))
print(binary_x)  # tensor([0., 1., 1., 0.])


#  TODO АКтивация, Использование активационной функции torch.nn.Threshold
threshold = torch.nn.Threshold(threshold=0.5, value=0.0)
x = torch.tensor([0.2, 0.6, 0.8, 0.1])
print(threshold(x), '>>>>')  # tensor([0.0000, 0.6000, 0.8000, 0.0000])


#  TODO АКтивация, Использование активационной функции nn.Threshold
threshold_layer = nn.Threshold(threshold=0.5, value=-1.0)

x = torch.tensor([-1.0, 0.3, 0.5, 0.7, 1.0])
output = threshold_layer(x)

print(output)




# TODO Доступность CUDA
print("PyTorch версия:", torch.__version__)
print("CUDA доступна:", torch.cuda.is_available())
print("Количество GPU:", torch.cuda.device_count())
if torch.cuda.is_available():
    print("Имя первого GPU:", torch.cuda.get_device_name(0))

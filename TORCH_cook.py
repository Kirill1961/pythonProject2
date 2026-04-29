import random
import pandas as pd
import numpy as np
import re
from datetime import date, datetime, timedelta
import math
import datetime
from collections import defaultdict
import itertools
import matplotlib.pyplot as plt
import torch
import tensorflow as tf
import torch
from torch import nn
from torch.utils.data import DataLoader
# from torchvision import datasets
# from torchvision.transforms import ToTensor


#%%
print(torch.__version__)
print(torch.cuda.is_available())

#%%
# TODO Просто задать data с нормальным распределением
torch.normal(mean=0, std=1, size=(10,))  # 👉 Запятая обязательна

#%%
# TODO Просто задать data 2D с нормальным распределением
torch.normal(mean=0, std=1, size=(2, 4))

#%%
# TODO Задать вектор распределений, mean - 10 средних и std - 10 сигм
torch.normal(mean=torch.arange(1., 11.), std=torch.arange(1, 0, -0.1))

#%%
torch.normal(mean=0.5, std=torch.arange(1., 6.))

#%%
torch.normal(mean=torch.arange(1., 6.))

#%%
# TODO Несколько батчей с разными распределениями и разными mean, std
mean = torch.arange(1., 4.)        # (3,)
std = torch.arange(1., 0.4, -0.2)     # (3,)

eps = torch.randn(4, 3)         # (4, 3)

samples = eps * std + mean  # X = Z * std + mu

print(samples)

#%%
# TODO через expand 5 разных распределений с разными mean и std
#  .expand() задаёт форму для генерации батча в torch.normal, но не создаёт новые значения
mean = torch.arange(1., 6.)      # (5,) - вектор средних
std = torch.arange(1, 0.5, -0.1)   # (5,) - вектор sdt

samples11 = torch.normal(
    mean.expand(10, 5),
    std.expand(10, 5)
)

print(samples11)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
import logging


data_2 = pd.read_csv \
    ("https://raw.githubusercontent.com/koroteevmv/ML_course/2023/ML2.2%20real%20classification/data/diabetes.csv")
# print(data.head())


california = fetch_california_housing()  # fetch_california_housing() - функция из sklearn, в виде словаря
data = pd.DataFrame(california.data, columns=california.feature_names)  # DataFrame - массив
data["Price"] = california.target  # выборка столбца целевой переменной


# Настройка отображения
pd.set_option('display.max_columns', None)  # Показывать все столбцы
pd.set_option('display.width', 1000)        # Установить ширину вывода
pd.set_option('display.max_colwidth', None) # Установить максимальную ширину столбца


# print(type(california))
# print(california)  # total dataset
print(california.keys())  # ключи словаря dataframe
# print(california.DESCR)  # descript описание
print(california.data.shape)  # форма
# print(data.head())
# print(data.tail())
print(data.info())
print(data.head())
# Ваш DataFrame
# Полное описание данных
print(data.describe().round(2))
# print(california.get('frame'), ">>>>>>>>>>>>>>>>>>>>>>")


# возврат настроек вывода
current_max_columns = pd.get_option('display.max_columns')
current_width = pd.get_option('display.width')


y = data.Price
X = data.drop("Price", axis=1)  # вырезаем из dataframe целевую переменную target value

print(data["Price"].values)


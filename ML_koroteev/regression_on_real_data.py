import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_classification
import logging
import pprint

data_2 = pd.read_csv \
    ("https://raw.githubusercontent.com/koroteevmv/ML_course/2023/ML2.2%20real%20classification/data/diabetes.csv")
# print(data.head())


california = fetch_california_housing()  # fetch_california_housing() - функция из sklearn, в виде словаря
data = pd.DataFrame(california.data, columns=california.feature_names)  # DataFrame - массив
data["Price"] = california.target  # выборка столбца целевой переменной


# Настройка отображения
pd.set_option('display.max_rows', 10)  # установка количества рядов
pd.set_option('display.max_columns', None)  # Показывать все столбцы
pd.set_option('display.width', 1000)        # Установить ширину вывода
pd.set_option('display.max_colwidth', None) # Установить максимальную ширину столбца


# print(type(california))
# print(california)  # total dataset
print(california.keys())  # ключи словаря dataframe
# print(california.DESCR)  # descript описание
print(california.data.shape)  # форма
print(data.head())
# print(data.tail())
print(data.info())
print(data.head())
# Ваш DataFrame
# Полное описание данных
print(data.describe().round(2))  # статистические параметры
# print(california.get('frame'))


y = data["Price"]
# вырезаем из dataframe целевую переменную(ЦП) target value что бы отделить ЦП от остального df
X = data.drop("Price", axis=1)

print(data.Price.values, "Price", "\n")
print(X.shape, y.shape, "\n")

model = LinearRegression()
model.fit(X, y)
score = model.score(X, y)
print(score, "score", "\n")

coef = model.coef_   # Коэфф кореляции
print(model.coef_, "model.coef_", "\n")

print(X.columns, "\n")

model_quality = [(i, j) for i, j in zip(X.columns, coef)]  # Качество модели
model_quality_ = [(i, j) for i, j in zip(california.feature_names, coef)]  # Качество модели
print(model_quality_, "model_quality", "\n")
pprint.pprint(model_quality)


intercept = model.intercept_  # значение свободного параметра, те значение целевой переменной если бы все Х были = 0
print(intercept, "intercept", "\n")


""" Сравним некоторый  прогнозы с истинными значениями"""
y_pred = model.predict(X)
print(y_pred[5:])

# возврат настроек вывода
current_max_columns = pd.get_option('display.max_columns')
current_width = pd.get_option('display.width')

# sc = plt.scatter(y_pred, y)  # разброс предсказанного Y от истинного, диаграмма рассеяния
# ref = plt.plot(y, y, c="r")  # референсная прямая
# plt.show()
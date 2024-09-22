import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import random

"""Сетка x_vals - определяет, в каких точках будет оцениваться плотность для выборки b. 
Чем больше точек (в данном случае 100), 
тем более плавной будет линия на графике"""


random.seed(0)
# Выборка для оценки плотности (1000 случайных значений из нормального распределения)
mu, sigma = 0, 1
sample = np.random.normal(loc=mu, scale=sigma, size=1000)

# Для примера случайная ненормальная выборка
# sample = [random.random() for _ in range(1000)]

# Проверка среднего значения и стандартного отклонения выборки sample
print(abs(mu - np.mean(sample)))  # Разница между заданным и реальным средним
print(abs(sigma - np.std(sample, ddof=0)))  # Разница между заданным и реальным стандартным отклонением

# Передаем выборку в класс gaussian_kde для оценки плотности
kde = gaussian_kde(sample)

# Построение графика KDE на сетке значений
x_vals = np.linspace(-3, 3, 100)  # Задаем сетку значений

# Вычисляем плотность для заданного диапазона значений
density = kde(x_vals)

# Строим гистограмму для сетки с нормализацией плотности
plt.hist(sample, bins=40, density=True, alpha=0.5, label="Histogramm")

# Строим график функции плотности (KDE)
plt.plot(x_vals, density, label="KDE", color="brown")
plt.show()


# Извлечь образцы из распределения
# mu, sigma = 0, 0.1 # mean and standard deviation
# s = np.random.normal(mu, sigma, 1000)
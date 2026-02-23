import random
import math
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import scipy
from scipy.stats import norm

# TODO begin

# Задаём мат.ожидание, std, диапазон выборки
x1 = -100
x2 = 100
mu = 0
sigma = 1
data = sorted(np.random.normal(loc=0, scale=1, size=1000))  # задаём loc=0 мат.ожидание, scale=1 дисперсия
# data = [-5, -4, -3, -2, -1, -0.5, -0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 1, 2, 3, 4, 5 ]
# print(data)

"""PDF - при нормальном распределении описывает вероятность появления различных значений случайной величины.
PDF - по выборке из ген.совокупности находим x_bar и std для оценки параметров ген.совокупности,
   PDF - плотность распределения вероятности"""


# ДФР - probability density function (pdf), ф-ция плотности равномерного распределения
# вероятность наблюдать значение в определённом интервале = интегралу взятому в отм пределе
def uniform_pdf(a):  # Равномерность распределения

    print(a, "Равномерность распределения")

    return 1 if a >= 0 and a < 1 else 0


print(uniform_pdf(random.random()), "uniform_pdf")


# PDF (ДФР) нормального распределения

def normal_pdf(x, mu, sigma):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


# print(normal_pdf(2), "normal_pdf")

# Графики некоторых ДФР

xs = [x / 10.0 for x in range(x1, x2)]  # выборка для PDF, делим на 10 для масштабирования
# print(xs, "выборка")
# plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
# plt.plot(xs, [normal_pdf(x, mu, sigma) for x in xs], '--', label=f'mu={mu}, sigma={sigma}')
# plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
# plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.plot(data, [normal_pdf(x, mu, sigma) for x in data], '--', label=f'mu={mu}, sigma={sigma}')  # data - рандомная
plt.legend()

# plt.show()

"CDF вычисляет вероятность того что случайная величина X из этой выборки примет значение в интервале CDF(min) - CDF(X)"


# CDF (ИФР) - commutative distribution function (cdf), интегральная ф-ция распределения,
# определяет вероятность случайного значения  < или = некоторому значению " x ".

def uniform_cdf(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


print(uniform_cdf(random.random()), "uniform_cdf")


# ИФР нормального распределения ещё называют ф-ция ошибки

def normal_cdf(x, mu, sigma):
    # print(mu, sigma, ">>>>>>>>>>>>>>>>>>>>>>>")
    return ((1 + scipy.special.erf((x - mu) / math.sqrt(2) / sigma)) / 2)


xs = [x_ / 10.0 for x_ in range(x1, x2)]  # выборка для CDF, делим на 10 для масштабирования
# print(xs)
# plt.plot(xs, [normal_cdf(x_, sigma=1) for x_ in xs], '-', label='mu=0, sigma=1')
# plt.plot(xs, [normal_cdf(x, mu, sigma) for x in xs], '--', label=f'mu={mu}, sigma={sigma}')
# plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
# plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.plot(data, [normal_cdf(x, mu, sigma) for x in data], '--', label=f'mu={mu}, sigma={sigma}')  # data - рандомная
plt.xlabel('Значение из выборки')
plt.ylabel('Вероятность')
plt.legend()
# plt.show()


# Пример расчёта вероятности с помощью CDF
# Задаем параметры нормального распределения
mu = 0  # Среднее значение
sigma = 1  # Стандартное отклонение
# Вычисляем вероятность для значения x=
x = 5  # задаём значение для CDF для поиска вероятности что Х примет значение < или = заданному Х
probability = norm.cdf(x, loc=mu, scale=sigma)  # norm - нормальное (или гауссово) распределение
print(f"Вероятность, что случайная величина <= {x}:", probability)


# TODO Вычисление статистик через pdf
#  pdf(x) = 1 - высота распределения
#  pdf(x_i) - это высота базового прямоугольника для интеграла
#  dx - это ширина базового прямоугольника для интеграла
def pdf(x):
    return 1  # для распределения Uniform(0,1)


# сетка значений
xs = np.linspace(0, 1, 10001)
dx = xs[1] - xs[0]  # шаг между данными, ширина маленького кусочка, для вычисления интеграла

# mean = ∫ x f(x) dx
mean = np.sum(xs * pdf(xs) * dx)

# variance = ∫ (x - mean)^2 f(x) dx
var = np.sum((xs - mean) ** 2 * pdf(xs) * dx)
std = np.sqrt(var)

print('mean : ', mean, '\n', 'std : ', std)


# TODO Вероятность события в интервале из набора xs
#  Например 0.2 ≤ X ≤ 0.7

mask = (xs >= 0.2) & (xs <= 0.7)

prob = np.sum(pdf(xs[mask]) * dx)

print(prob)


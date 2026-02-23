from collections import deque, Counter
import numpy as np

import matplotlib.pyplot as plt
from scipy.stats import norm, uniform

users_interests = [
    ["MongoDB", "data science", "Spark", "Postgres", "pandas", "NoSQL" "Big Data"],
    ["Storm", "Java", "pandas", "MongoDB", "data science", "pandas", "data science"],
    [
        "C++",
        "Scikit-learn",
        "regression",
        "neural network",
        "MongoDB",
        "Big Data",
        "data science",
        "NoSQL Big Data",
    ],
    ["statistic", "R", "go", "scipy", "numpy", "MongoDB", "pandas", "data science"],
    [
        "Storm",
        "regression",
        "neural network",
        "MongoDB",
        "Big Data",
        "data science",
        "NoSQL Big Data",
    ],
    ["C++", "Scikit-learn", "regression", "neural network", "Big Data", "pandas"],
    [
        "Scikit-learn",
        "regression",
        "neural network",
        "MongoDB",
        "Big Data",
        "data science",
        "NoSQL Big Data",
    ],
    [
        "statistic",
        "R",
        "go",
        "scipy",
        "numpy",
        "data science",
        "pandas",
        "NoSQL" "Big Data",
    ],
    [
        "Python",
        "Hadoop",
        "numpy",
        "NoSQL",
        "MongoDB",
        "HBase",
        "data science",
        "NoSQL" "Big Data",
    ],
    [
        "Cassandra",
        "machine learning",
        "Haskel",
        "C++",
        "scipy",
        "data science",
        "NoSQL Big Data",
    ],
    ["Python", "Hadoop", "numpy", "NoSQL Big Data", "pandas", "NoSQL Big Data"],
    ["statistic", "Java", "pandas", "MongoDB", "data science"],
    ["numpy", "decision trees", "libsvm", "MongoDB", "probability"],
    [
        "statistic",
        "R",
        "go",
        "scipy",
        "numpy",
        "machine learning",
        "data science",
        "NoSQL Big Data",
    ],
    ["Python", "Hadoop", "numpy", "data science", "MongoDB", "NoSQL" "Big Data"],
    ["HBase", "Storm", "Java", "pandas"],
    [
        "statistic",
        "R",
        "go",
        "scipy",
        "C++",
        "MongoDB",
        "pandas",
        "data science",
        "NoSQL Big Data",
    ],
    ["Spark", "Postgres", "Cassandra", "machine learning", "Haskel", "pandas"],
    ["statistic", "R", "go", "scipy", "HBase", "pandas", "data science"],
    ["Python", "Hadoop", "numpy", "NoSQL", "HBase", "NoSQL Big Data"],
]

popular_intersts = Counter(
    interest for user_interests in users_interests for interest in user_interests
).most_common()


def most_popular_new_interests(user_interests, max_results=5):
    suggestions = [
        (interest, frequency)
        for interest, frequency in popular_intersts
        if interest not in user_interests
    ]
    return suggestions[:max_results]


print(
    most_popular_new_interests(
        ["MongoDB", "data science", "Spark", "Postgres", "pandas", "NoSQL" "Big Data"]
    )
)

# TODO data
"""PDF - при нормальном распределении описывает вероятность появления различных значений случайной величины.
PDF - по выборке из ген.совокупности находим x_bar и std для оценки параметров ген.совокупности,
PDF - плотность распределения вероятности"""
# Генерация выборки данных из нормального распределения
# data = sorted(np.random.normal(loc=0, scale=1, size=100))  # задаём loc=0 мат.ожидание, scale=1 дисперсия
# data = [ 2.36282188,  0.22990034,  1.43859994, -0.05, -1.16457742,  0.32377849
#  -0.96833643,  0.54881387, -0.2, - 0.1, -0.3, -0.4 ]
# data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1, 2, 3, 4, 5]
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(data[0], data[-1], "data[0], data[-1]")


# norm.fit - оценка параметров нормального распределения по выборке данных !!!!!!!!!!!!!!
mean, std_dev = norm.fit(data)
print(mean, "mean")
print(std_dev, "std_dev")

# Гистограмма выборки данных
plt.hist(data, bins=30, density=True, alpha=0.6, color="g")

# Распределение плотности вероятности для нормального распределения

xmin, xmax = plt.xlim()
print(xmin, xmax, ">>>>>>>>>>>>>>>")
x = np.linspace(xmin, xmax, 10000)
p = norm.pdf(x, mean, std_dev)
plt.plot(x, p, "k", linewidth=2)
plt.xlabel("Значение из выборки")
plt.ylabel("Вероятность")
plt.title("Гистограмма и плотность вероятности")
# plt.show()


"CDF вычисляет вероятность того что случайная величина X из этой выборки примет значение в интервале CDF(min) - CDF(X)"
# Параметры нормального распределения
# mu = 0  # Среднее значение
# sigma = 1  # Стандартное отклонение
mu = mean  # Среднее значение
sigma = std_dev  # Стандартное отклонение

# Создание объекта нормального распределения
distribution = norm(mu, sigma)
print(distribution, "distribution")

# Генерация значений для оси x
# x = np.linspace(-1, 1, 10)
# print(x)
x = data

# Расчет функции распределения (CDF) для каждого значения x
cdf_values = distribution.cdf(x)
print(x[-1], "-", cdf_values[-1], "cdf_values")

# Построение графика функции распределения
plt.plot(x, cdf_values)
plt.title("Функция распределения (CDF) для нормального распределения")
plt.xlabel("Значение случайной величины")
plt.ylabel("Вероятность")
plt.grid(True)
# plt.show()


""" Пример расчёта вероятности с помощью CDF"""
# Задаём параметры нормального распределения
mu = mean  # Среднее значение, взяли из выборки PDF, строка 54
sigma = std_dev  # Стандартное отклонение, взяли из выборки PDF, строка 54
# Вычисляем вероятность для значения x=
x = 1.6  # задаём значение для CDF для поиска вероятности что Х примет значение < или = заданному Х
probability = norm.cdf(x, loc=mu, scale=sigma)
print(f"Вероятность, что случайная величина <= {x}:", probability)


""" PDF если равномерное распределение то просто вычисляем вероятность что random_value будет равна Х"""
# Задаем параметры равномерного распределения
a = 0  # Минимальное значение
b = 10  # Максимальное значение

# Вычисляем вероятность для значения x=5
x = 5
probability = uniform.pdf(
    x, loc=a, scale=b - a
)  # uniform - Равномерность распределения

print(f"Вероятность, что случайная величина равна {x}:", probability)

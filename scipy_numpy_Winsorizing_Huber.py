import glob
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats.mstats import winsorize
from sklearn.linear_model import HuberRegressor
from scipy.special import huber

puth = 'D:\Eduson_data\Analisys_data_Eduson.csv'

data = pd.read_csv(puth)

df = pd.DataFrame(data)
print(df.head(5))

# TODO Среднее и boxplot выборки с выбросами до усечения
sales_before = stats.tmean(df.Sales)
print(f'Среднее до усечения :{sales_before:.2F}')

fig, axes = plt.subplots(figsize=(2, 2))
sns.boxplot(x=df.Sales)
axes.set_title(f'До усечения выборки :{sales_before:.2F}')
# plt.show()

sales_after = stats.trim_mean(df.Sales, 0.25)
print(f'Среднее после усечения :{sales_after:.2F}')

sample_after = stats.trimboth(df.Sales, 0.3)
fig, axes = plt.subplots(figsize=(2, 2))
axes.set_title(f'После усечения выборки :{sales_after:.2F}')
sns.boxplot(x=sample_after)
# plt.show()

# TODO Фильтр bool столбца Sales по МОДАЛЬНОМУ значению = 12.96
mode = df.Sales.mode()[0]  # mode - мах повтор значения
filter_mode = df.Sales == df.Sales.mode()[0]  # Булевый фильтр по mode даёт число 12.96

# TODO [0] - Индекс Series 'Sales'
# df.Sales.mode()[0] = 12.96

print(f"Число повторов моды 12.96 = {filter_mode.sum()} раз")
df.Sales.mode()

# TODO Winsorizing - все значения ниже нижнего порога заменяются на нижний перцентиль, а все выше верхнего — на верхний перцентиль
#  * Когда распределение сильно скошено (skewed)
#  * Когда есть единичные экстремальные выбросы
#  * Когда важен размер выборки

print(len(df["Sales"]))
df["Sales"] = winsorize(df["Sales"], limits=[0.05, 0.05])
print(len(df["Sales"]))

# TODO Мода в NumPy -> только для целых чисел, используем np.bincount() + np.argmax()
arr = np.array([7, 7, 7, 7, 7, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

mode_np = np.bincount(arr).argmax()
print("Мода (NumPy):", mode_np)  # 7




# TODO веса для взвешенного среднего по Хьюберу
X = np.array([10, 12, 13, 15, 20, 1000, 2000]).reshape(-1, 1)
y = np.array([10, 12, 13, 15, 20, 1000, 2000])  # Целевая переменная (та же самая)

# Вычисляем IQR для определения выбросов
q1, q3 = np.percentile(y, [25, 75])
iqr = q3 - q1
delta = 1.5 * iqr  # Порог отсечения

# Применяем Huber loss (она даёт усечённые потери)
weights = huber(delta, y - np.median(y))

# Переводим потери в веса
weights = 1 / (1 + weights)

print("Веса для каждого значения:", weights)
print("Взвешенное среднее:", np.average(y, weights=weights))

# Обучаем модель
huber = HuberRegressor()
huber.fit(X, y)

# Получаем веса
# weights = huber.outliers_

# Взвешенное среднее - предсказанное значение
weighted_mean = huber.predict(X).mean()

# print(f'Веса выбросов : {weights}')
# print("Вес каждого наблюдения:", 1 - weights)
print(f"Взвешенное среднее (по Хьюберу): {weighted_mean:.2f}")


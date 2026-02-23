from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
import pandas as pd
from sklearn.preprocessing import RobustScaler

# TODO MinMax Scaling - Используется, когда важно сохранить разницу между минимальным и максимальным значением.
data = np.array([[100], [150], [200], [250], [300]])
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

print(scaled_data)


# TODO Z-нормализация (Standard Scaling), Используется, когда данные имеют нормальное распределение.
data = np.array([[100], [200],  [300]])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print(f'Среднее стало 0, стандартное отклонение 1 : {scaled_data}')


# TODO Нормализация L1 и L2 - Используется для текстовых данных или разреженных матриц
#  L1-нормализация: сумма абсолютных значений = 1.
#  L2-нормализация: сумма квадратов значений = 1.


data = np.array([[3, 4], [1, 2]])
scaler = Normalizer(norm="l2")  # Можно norm="l1"
normalized_data = scaler.fit_transform(data)

print(f'Каждая строка теперь имеет длину 1 в евклидовом пространстве : {normalized_data}')


# TODO Робастное масштабирование
#     (Robust Scaling) - нормализации данных, который устойчив к выбросам
#     масштабирует данные, используя медиану (Q2) и межквартильный размах (IQR)
#     вместо минимального и максимального значений, как это делает MinMaxScaler.


X = np.array([[10], [20], [30], [40], [500]])  # 500 - выброс

scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)

df = pd.DataFrame({"Original": X.flatten(), "Scaled": X_scaled.flatten()})
print(f'{df} <- это Выброс  ')

# TODO Все методы
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer

# Данные с выбросами
X = np.array([[10], [20], [30], [40], [500]])

# Применяем разные методы нормализации
minmax = MinMaxScaler().fit_transform(X)
standard = StandardScaler().fit_transform(X)
robust = RobustScaler().fit_transform(X)
l1_norm = Normalizer(norm="l1").fit_transform(X.T).T
l2_norm = Normalizer(norm="l2").fit_transform(X.T).T

# Создаём DataFrame
df = pd.DataFrame({
    "Original": X.flatten(),
    "MinMaxScaler": minmax.flatten(),
    "StandardScaler": standard.flatten(),
    "RobustScaler": robust.flatten(),
    "L1 Normalization": l1_norm.flatten(),
    "L2 Normalization": l2_norm.flatten()
})

print(df)

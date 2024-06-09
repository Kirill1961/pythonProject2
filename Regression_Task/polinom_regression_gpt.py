import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Пример данных
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1, 4, 9, 16, 25])  # истинное значение, наблюдаемая оценка

# Преобразование данных в полиномиальные признаки (степень 2)
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)
print(x_poly, "x_poly")
print(y, "y")

# Обучение модели линейной регрессии на полиномиальных признаках
model = LinearRegression()
model.fit(x_poly, y)

# Прогнозирование с полиномиальными признаками, полиномиальное преобразование добавляет признаки но не атрибуты
# X_new = np.array([[280, 4, 8]])
# y_pred = model.predict(X_new)
y_pred = model.predict(x_poly)
print(y_pred, "y_pred")


# Визуализация
# plt.scatter(x, y, color='blue')
# plt.plot(x, y_pred, color='red')
# plt.show()

""" вариант с разными матрицами данных без полинома"""
# Пример данных
# X = np.array([
#     [1, 2],
#     [2, 3],
#     [3, 4],
#     [4, 5],
#     [5, 6]
# ])

# X = np.array([
#     [1],
#     [2],
#     [3],
#     [4],
#     [5]
# ])

# X = np.array([
#     [10, 2, 7],
#     [2, 30, 8],
#     [30, 4, 90],
#     [4, 50, 5],
#     [5, 6, 10]
# ])
# y = np.array([2, 3, 4, 5, 6])

# Обучение модели линейной регрессии
# model = LinearRegression()
# model.fit(X, y)

# Прогнозирование
# y_pred = model.predict(X)
# print(y_pred)

# plt.scatter(X, y, color='blue')
# plt.plot(x, y_pred, color='red')
# plt.show()
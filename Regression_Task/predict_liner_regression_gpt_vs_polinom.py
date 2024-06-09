import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Пример данных: площадь, количество комнат, возраст дома
""" Строки - объекты, столбы - признаки"""
X = np.array([
    [150, 3, 20],
    [200, 4, 15],
    [250, 4, 10],
    [300, 5, 5],
    [350, 5, 1]
])
print(X, "Строки - объекты, столбы - признаки", "\n")
# Целевая переменная: цена дома
y = np.array([300, 400, 500, 600, 700])  # истинное значение , наблюдаемая оценка
print(y, "y", "\n")


# Преобразование данных в полиномиальные признаки (степень 2)
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(X)
print(x_poly, "x_poly", "\n")
print(x_poly.shape, "x_poly.shape - видим 10 столбов те 10 признаков", "\n")


# Обучение модели линейной регрессии с преобразованными данными в полиномиальные
# model = LinearRegression().fit(X, y)  # проба через точку -  .fit(X, y)
model = LinearRegression()
model_fit = model.fit(x_poly, y)
print(model.score(x_poly, y), "score - Качество модели, Коэффициент детерминации", "\n")  # Качество модели, R**


# Предсказание для нового дома, с полиномиальными признаками, полиномиальное преобразование добавляет признаки
"""Тк полином-ое преоб-ие добавило признаки (features) до 10 то для прогноза input должен иметь тоже 10 features """
X_new = np.array([[280, 4, 8]])
# print(X_new, "X_new")
# y_pred = model.predict(X_new)
new_poly = PolynomialFeatures(degree=2)
X_new_poly = new_poly.fit_transform(X_new)
print(X_new_poly, "        преобразуем 3 три исходных признака [280, 4, 8] в 10 признаков", "\n")
y_pred = model.predict(X_new_poly)
print(y_pred, "y_pred", "\n")
print(f'Предсказанная цена для нового дома: {y_pred[0]:.2f} тыс. долларов', "\n")


# Коэффициенты модели
print(f'Коэффициенты: {model.coef_}')
print(f'Сдвиг: {model.intercept_}')

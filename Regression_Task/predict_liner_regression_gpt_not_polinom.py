import numpy as np
from sklearn.linear_model import LinearRegression

# Пример данных: площадь, количество комнат, возраст дома
X = np.array([
    [150, 3, 20],
    [200, 4, 15],
    [250, 4, 10],
    [300, 5, 5],
    [350, 5, 1]
])

# Целевая переменная: цена дома
y = np.array([300, 400, 500, 600, 700])

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X, y)
print(model.score(X, y), "score")
# Предсказание для нового дома
X_new = np.array([[280, 4, 8]])
y_pred = model.predict(X_new)
print(f'Предсказанная цена для нового дома: {y_pred[0]:.2f} тыс. долларов')

# Коэффициенты модели
print(f'Коэффициенты: {model.coef_}')
print(f'Сдвиг: {model.intercept_}')
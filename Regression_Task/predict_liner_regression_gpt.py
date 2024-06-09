# Пример кода для прогноза с использованием обученной модели
import numpy as np
from sklearn.linear_model import LinearRegression

# Обучающие данные
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([1.5, 3.2, 4.8, 6.5, 8.1])

# Создаем и обучаем модель
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказываем для нового значения
X_new = np.array([[6]])
y_pred = model.predict(X_new)
print(f'Предсказанное значение для X=6: {y_pred[0]:.2f}')

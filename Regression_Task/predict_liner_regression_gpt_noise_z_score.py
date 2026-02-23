# Пример кода для прогноза с использованием обученной модели
import numpy as np
from sklearn.datasets import load_iris, make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error


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


# Обучающие данные (три предиктора)
X_train = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7]
])
y_train = np.array([1.5, 3.2, 4.8, 6.5, 8.1])  # Целевая переменная

# Создаем и обучаем модель
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказываем для нового значения (три предиктора)
X_new = np.array([[6, 7, 8]])
y_pred = model.predict(X_new)

print(f'Предсказанное значение для X_new={X_new.tolist()[0]}: {y_pred[0]:.2f}')


# TODO IRIS
# Классификация
# Загрузка данных
data = load_iris()
X, y = data.data, data.target

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Обучение модели
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Оценка модели
train_accuracy = accuracy_score(y_train, clf.predict(X_train))
test_accuracy = accuracy_score(y_test, clf.predict(X_test))

print(f"Train Accuracy: {train_accuracy:.2f}")
print(f"Test Accuracy: {test_accuracy:.2f}")

# Регрессия
# Генерация данных
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Обучение модели
reg = LinearRegression()
reg.fit(X_train, y_train)

# Оценка модели
train_mse = mean_squared_error(y_train, reg.predict(X_train))
test_mse = mean_squared_error(y_test, reg.predict(X_test))

print(f"Train MSE: {train_mse:.2f}")
print(f"Test MSE: {test_mse:.2f}")


# TODO Поиск Шума через z-score
#  z-score - отклонение значений выборки от среднего в сигмах
#  z = xi−μ / σ
A = np.array([5,   5,   1,   6,   3,   1,   2,   4,   4,   6,   4,   9,   3,
         3,   8,   3,   1,   3,   8,   5, 100])
z = (A - np.mean(A)) / np.std(A)  # 👆 z = xi−μ / σ
outliers = A[np.abs(z) > 3]  # 👉 если больше 3 сигм от центра

print(outliers)
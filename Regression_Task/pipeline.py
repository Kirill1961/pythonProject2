import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Генерация случайных данных
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([1, 2, 3, 4, 5])

# Разделение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Определение пайплайна
pipeline = Pipeline([
    ('scaler', StandardScaler()),         # Масштабирование данных
    ('regressor', LinearRegression())     # Линейная регрессия
])

# Обучение пайплайна
pipeline.fit(X_train, y_train)

# Предсказание
predictions = pipeline.predict(X_test)
print("Предсказания:", predictions)

# Оценка модели
score = pipeline.score(X_test, y_test)
print("R^2 score:", score)

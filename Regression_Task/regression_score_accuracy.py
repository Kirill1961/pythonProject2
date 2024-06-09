"""Метод .score() в библиотеках машинного обучения и статистики,
таких как scikit-learn, используется для оценки производительности модели.
 Он возвращает метрику, характеризующую, насколько хорошо модель предсказывает данные.
 Точная интерпретация и метрика зависят от типа модели и задачи (регрессия, классификация и т.д.).
Кластеризация:
В задачах кластеризации метод .score() может использоваться для вычисления метрик,
таких как сумма квадратов расстояний до ближайшего центра кластера.
"""


"""Классификация:
Метод .score() возвращает долю правильных ответов (accuracy), то есть количество
правильных предсказаний делённое на общее количество предсказаний."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.metrics import accuracy_score, mean_squared_error

# Загрузка данных
data = load_iris()
X, y = data.data, data.target

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Обучение модели
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Оценка модели
accuracy = model.score(X_test, y_test)
print(f"Точность модели: {accuracy:.2f}")


"""Регрессия:
Метод .score() возвращает коэффициент детерминации (R²), который измеряет,
какую долю вариации в целевой переменной объясняет модель."""
# Генерация данных
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Оценка модели
r2_score = model.score(X_test, y_test)
print(f"R^2 score модели: {r2_score:.2f}")


"""Альтернативые метрики"""


# Для классификации
y_true = [0, 1, 0, 1]
y_pred = [0, 1, 0, 0]
print(f"Accuracy: {accuracy_score(y_true, y_pred):.2f}")

# Для регрессии
y_true = [2.5, 0.0, 2.1, 1.6]
y_pred = [2.4, 0.1, 2.3, 1.4]
print(f"MSE: {mean_squared_error(y_true, y_pred):.2f}")

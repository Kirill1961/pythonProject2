from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import RocCurveDisplay
import matplotlib.pyplot as plt


# Загружаем данные
# TODO готовый датасет по диагностике болезни
#  * Признаки: 30 числовых (размер, текстура, компактность и др.)
X, y = load_breast_cancer(return_X_y=True)

# TODO Функция train_test_split разбивает данные на:
#  * Обучающую выборку (X_train, y_train)
#  * Тестовую выборку (X_test, y_test) — случайно, с возможностью задать random_state и пропорцию.
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Обучаем модель
# TODO Импорт логистической регрессии — модели классификации:
#  * Предсказывает вероятность принадлежности к классу
#  * Хорошо работает при линейной разделимости
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Строим ROC-кривую
# TODO Класс для построения ROC-кривой автоматически:
#  * Используется как RocCurveDisplay.from_estimator(model, X_test, y_test)
#  * Визуализирует, насколько хорошо модель различает классы
#  🔹 AUC (Area Under Curve) — это площадь под ROC-кривой:
#     * AUC = 1.0 — идеальная модель.
#     * AUC = 0.5 — модель угадывает случайно.
#     * AUC < 0.5 — модель работает хуже случайной.
RocCurveDisplay.from_estimator(model, X_test, y_test)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import learning_curve
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# 1. Данные
X, y = make_classification(n_samples=2000, n_features=20, random_state=42)

# 2. Модель
model = LogisticRegression(max_iter=1000)

# 3. Learning curve
train_sizes, train_scores, val_scores = learning_curve(
    model, X, y,
    cv=5,                   # кросс-валидация
    scoring='accuracy',     # метрика
    train_sizes=np.linspace(0.1, 1.0, 10),  # от 10% до 100% данных
    n_jobs=-1
)

# 4. Усредняем по фолдам
train_mean = np.mean(train_scores, axis=1)
val_mean = np.mean(val_scores, axis=1)

# 5. Визуализация
plt.plot(train_sizes, train_mean, 'o-', label="Train")
plt.plot(train_sizes, val_mean, 'o-', label="Validation")
plt.xlabel("Размер обучающей выборки")
plt.ylabel("Accuracy")
plt.legend()
plt.title("Learning Curve")
plt.show()

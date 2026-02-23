import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier


# 1. Синтетические данные
X, y = make_classification(
    n_samples=300,
    n_features=2,
    n_redundant=0,
    n_clusters_per_class=1,
    n_classes=2,
    random_state=42,
)

# 2. Модель KNN с заданным k
k = 3  # можешь менять
knn = KNeighborsClassifier(n_neighbors=k, algorithm='kd_tree')
knn.fit(X, y)

# 3. Сетка значений для предсказания на всей плоскости
h = 0.05  # шаг сетки
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
grid = np.c_[xx.ravel(), yy.ravel()]

# 4. Предсказания на сетке
# Z = knn.predict(grid)
Z = knn.predict_proba(grid)[:, 1]  # вероятность класса 1 / 0
Z = Z.reshape(xx.shape)

# 5. Ты можешь визуализировать с помощью plt.contourf и plt.scatter
plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k")

# Всё готово к визуализации
plt.show()

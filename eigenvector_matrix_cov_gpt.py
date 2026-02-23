import numpy as np

# 1. Данные: два признака (столбцы), 5 наблюдений (строки)
X = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0]
])

# 2. Центрируем данные (вычитаем среднее)
X_centered = X - np.mean(X, axis=0)

# 3. Строим матрицу ковариации (признаки по столбцам → транспонируем)
cov_matrix = np.cov(X_centered.T)

# 4. Вычисляем собственные значения и собственные векторы
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# 5. Выводим
print("Матрица ковариации:")
print(cov_matrix)

print("\nСобственные значения:")
print(eigenvalues)

print("\nСобственные векторы (столбцы):")
print(eigenvectors, '\n')


v1 = eigenvectors[:, 0]  # первый собственный вектор
v2 = eigenvectors[:, 1]  # второй собственный вектор

print(v1)
print(v2)

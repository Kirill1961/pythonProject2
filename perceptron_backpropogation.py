import numpy as np


# TODO Прямое распространение сигнала


# Входной сигнал (4 признака)
x = np.array([1.0, 0.5, -1.5, 2.0])

# Весовая матрица (3 нейрона, 4 входа)
W = np.array([
    [0.2, -0.4, 0.1, 0.5],
    [-0.3, 0.8, -0.6, 0.9],
    [0.7, -0.1, 0.3, -0.2]
])

# Смещения
b = np.array([0.1, -0.2, 0.05])

# TODO  Линейная комбинация + ReLU активация, @ - перемножение матриц/векторов
z = W @ x + b
a = np.maximum(0, z)  # ReLU

print("Выход слоя:", a)


# TODO backpropogation


# --- ДАННЫЕ ---
x = np.array([1.0, -2.0, 3.0, 0.5])  # вход (shape: 4,)
W = np.array([
    [0.2, -0.4, 0.1, 0.5],
    [-0.3, 0.8, -0.6, 0.9],
    [0.7, -0.1, 0.3, -0.2]
])  # shape: (3, 4)
b = np.array([0.1, -0.2, 0.05])  # смещение (shape: 3,)
y_true = np.array([1.0, 0.0, 0.5])  # целевой вектор

# --- FORWARD PASS ---
z = W @ x + b
a = np.maximum(0, z)  # ReLU

# --- ПОТЕРЯ (MSE) ---
loss = np.mean((a - y_true)**2)
print("Loss:", round(loss, 4))

# --- BACKWARD PASS ---
# 1. Градиент по выходу ReLU
dL_da = 2 * (a - y_true) / len(y_true)  # dL/da
# TODO 2. Производная ReLU
#  * так как результат ReLU бинарный, то вычисление через булеву маску da_dz = (z > 0)
da_dz = (z > 0).astype(float)
print(da_dz, z, '>>>>>>>>>>')
# 3. dL/dz = dL/da * da/dz
dL_dz = dL_da * da_dz
# 4. dL/dW = dL/dz * x.T
dL_dW = dL_dz.reshape(-1, 1) @ x.reshape(1, -1)
# 5. dL/db = dL/dz
dL_db = dL_dz

print("\nГрадиент по W:\n", dL_dW)
print("\nГрадиент по b:\n", dL_db)


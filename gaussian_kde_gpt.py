import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


"""gaussian_kde - оценка плотности вероятности на основе ядерного сглаживания для заданной выборки данных"""
# Создаем случайную выборку
np.random.seed(0)
data = np.random.normal(loc=0, scale=1, size=100)
# data = [-50, -4, -300, -2, -1, -0.00005, -0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.00000003, 0.4, 0.5, 10, 2, 3, 4, 50000 ]
# data = [-5, -4, -3, -2, -1, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.00001, 0.05,  0.1, 0.2, 0.3, 0.4, 0.5, 1, 2, 3, 4, 5 ]
# print(data)
# Вычисляем плотность распределения выборки с помощью ядерного сглаживания
kde = gaussian_kde(data)
# kde_str = repr(kde)
# print(kde_str)
x = [0, 0.00001, 0.05,  0.1, 0.2, 0.3, 0.4, 0.5, 10]  # 10 - выброс который увеличивает std
print(f"PDF{kde.pdf(x)}")  # плотность вероятности в точке Х из данной выборки
print("Размер выборки:", kde.n)
print("Фактор сглаживания (bandwidth):", kde.factor)  # Ширина ядра
# print("Ядро:", kde.__dir__())  # все атрибуты из gaussian_kde
# Генерируем точки для построения графика
x = np.linspace(min(data), max(data), 100)
# Считаем плотность
density = kde(x)
# print(density)
# Строим график плотности распределения
plt.plot(x, density, label='KDE')
plt.hist(data, bins=30, density=True, alpha=0.5, label='Histogram')  # Добавляем гистограмму для сравнения
plt.xlabel('Значение')
plt.ylabel('Плотность')
plt.title('Плотность распределения выборки')
plt.legend()
plt.show()


"""PDF принимает на вход одномерный или многомерный массив точек и возвращает значения функции плотности вероятности
 в этих точках."""
# Создаем случайную выборку
np.random.seed(0)
data = np.random.normal(loc=0, scale=1, size=1000)

# Вычисляем оценку плотности вероятности для выборки data с помощью ядерного сглаживания
kde = gaussian_kde(data)

# Генерируем точки для вычисления значения PDF для всех значений из выборки x_values
x_values = np.linspace(-3, 3, 10)
print(f"x_values-> сгенерированные значения с linespace {x_values}")
# Вычисляем значения функции плотности вероятности в этих точках
pdf_values = kde.pdf(x_values)

# Выводим значения PDF на печать
print(f"вероятность для сгенерированных значений x_values -> {pdf_values}")


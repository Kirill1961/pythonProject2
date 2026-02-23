import numpy as np
import matplotlib.pyplot as plt

lam = 10.0                          # параметр λ
x = np.linspace(0, 10, 400)        # время между событиями
y = lam * np.exp(-lam * x)         # плотность вероятности

plt.plot(x, y)
plt.xlabel("Время между событиями (x)")
plt.ylabel("Плотность вероятности f(x)")
plt.grid(True)
plt.show()
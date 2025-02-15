import matplotlib.pyplot as plt

# График с текущим стилем
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

# Временное изменение стиля
with plt.style.context('seaborn'):
    plt.plot(["a", "b", "c"], [6, 5, 4])
    plt.show()

# Возврат к исходному стилю
plt.plot([1, 2, 3], [3, 8, 81])
plt.show()

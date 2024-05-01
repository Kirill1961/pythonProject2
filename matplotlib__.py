import math
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
from math import sqrt
# years = [1982, 1984, 1990, 1999, 2004, 2005, 2009, 2012, 2017, 2020]
# gdp = [110.2, 375, 762, 1245, 1425, 852, 9320, 18530, 45700, 64102]
# plt.plot(years, gdp, color='green')
# plt.title('Моя ЗП')
# plt.xlabel('годики')
# plt.ylabel('рублики')
# plt.show()


# years = [20, 100, 250, 400, 670, 940]
# vvp = [5, 15, 40, 84, 124, 187]
# plt.plot(years, vvp)
# plt.title('PROBE')
# plt.ylabel('this Y')
# plt.xlabel('this X')
# plt.show()


movies = ['Entony', 'Ben', 'Kasablanka', 'Handy', 'West']
num_oscars = [5, 11, 3, 8, 10]

# xs = [i + 0.1 for i, _ in enumerate(movies)]
# plt.bar(xs, num_oscars)
# plt.xticks([i + 0.5 for i,_ in enumerate(movies)], movies)
# plt.ylabel('MEDAL')
# plt.xlabel('FILMS')
# plt.show()

grades = [91, 15, 20, 74, 30, 40, 0, 58, 63, 87, 112]
decil = lambda grade: grade // 10 * 10  # деление без остатка и оставили десятую часть числа
histogramm = Counter(decil(grade) for grade in grades)
print(histogramm)


# num_friends = [3]
# num_friends = [100, 92, 87, 74, 56, 37, 21, 12, 2]
# friend_counts = Counter(num_friends)
# xs = range(101)
# ys = [friend_counts[x] for x in xs]  # friend_counts это словарь из Counter, если ключ [x]
# # не соотв ключам из словаря то ys - равен 0
# # print(xs)
# print(friend_counts, '  friend_counts')
# print(ys, ' ys')
# plt.bar(xs, ys)
#
# plt.axis([0, 101, 0, 20])  # пределы оси Х и У,  / axis([xmin, xmax, ymin, ymax]) /
# plt.show()



# import matplotlib.pyplot as plt
#
# from matplotlib.patches import Rectangle
#
# fig, axs = plt.subplots(2, 5, layout='constrained', figsize=(6.4, 3.2))
#
# hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']


# def hatches_plot(ax, h):
#     ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
#     ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
#     ax.axis('equal')
#     ax.axis('off')
#
# for ax, h in zip(axs.flat, hatches):
#     hatches_plot(ax, h)
#
# plt.show()


# Передаём изображение квадрата Rectangle, оси - 0,5, заполненость от края до края 1 и 1,
ax = plt.gca()
for i in range(2):
    for j in range(2):
        print(i, j)
        ax.add_patch(matplotlib.patches.Rectangle((j - 0.5, i - 0.5), 1, 1, hatch='o', fill=False, color='red'))
# plt.show()

import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

fig, axs = plt.subplots(2, 5, layout='constrained', figsize=(6.4, 3.2))

hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']


def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')

for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)

plt.show()
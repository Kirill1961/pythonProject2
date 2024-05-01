import itertools
import itertools as it
import operator
import numpy as np
a = [[0, 1], [0, 0], [1, 0], [1, 1]]


# accumulate - Накопление в список элементов из другого списка
def b(x):
    for j in a:
        print(j)
    r = list(it.accumulate(x))
    return r


print(b([[i] for i in a])[-1], " accumulate - Накопление в список элементов из другого списка ", "\n")

c = [["qwer"], ["asdf"], ["zxcv"]]

def b(x):
    r = list(it.accumulate(x))
    return r


print(b([[i] for i in c])[-1], " accumulate - Накопление в список элементов из другого списка ", "\n")

# Генераторы комбинаций чисел
combi = list(it.product([0, 1], repeat=2))
print(combi, "product ; Генераторы комбинаций чисел", "\n")
arr = np.array(combi)
print(arr, " комбинацию в матрицу ", "\n")

for i in arr:
    print(i)
print("for loop матрицы", "\n")
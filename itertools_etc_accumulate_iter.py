import itertools
import itertools as it
import operator
import numpy as np
import random


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



# iter - остановка генератора  по заданному значению
def foo():
    return random.randint(1, 3)


for i in iter(foo, 1):
    print(i, "остановка генератора  по заданному значению < 1 >")




def generate_number():
    # Функция-генератор для чисел от 0 до 10
    current_number = 0
    while current_number <= 10:
        yield current_number
        current_number += 1

# Создаём генератор
number_generator = generate_number()

# Используем iter с методом next и контрольным значением 11
for number in iter(number_generator.__next__, 7):
    print(f"остановка генератора  по заданному значению: {number}")

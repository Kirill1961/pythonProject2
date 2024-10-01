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

#  Chaine Выбрать два отрезка из списка
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 36, 37, 38,
        39, 40, 41, 42, 43, 44, 45, 46, 47,
        48, 49, 50, 51, 52, 53, 54, 55, 56,
        57, 58, 59, 60, 61, 62, 63, 64, 65,
        66, 67, 68, 69, 70, 71, 72, 73, 74,
        75, 76, 77, 78, 79, 80, 81, 82, 83,
        84, 85, 86, 87, 88, 89, 90, 91, 92,
        93, 94, 95, 96, 97, 98, 99, 100]

print(list(itertools.chain(lst[9: 15], lst[49: 55])))
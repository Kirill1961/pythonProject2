import numpy as np


# Полный код с комментариями
def fibonacci_generator():
    # Инициализация первых двух чисел Фибоначчи
    a, b = 0, 1
    while True:
        yield a  # Вернуть текущее значение a и приостановить выполнение
        a, b = b, a + b  # Обновить a и b для следующего числа Фибоначчи


# Создание экземпляра генератора
fib_gen = fibonacci_generator()

# Печать первых 10 чисел Фибоначчи
for _ in range(5):
    print(next(fib_gen))


# Фибо - просто
def foo(a):
    x, y = 0, 1
    for i in range(a):
        x, y = y, x + y
        yield y


print(list(foo(5)), "Фибо - просто", "\n")

# Фибо - ещё проще c while
a, b = 0, 1
while b < 5:
    a, b = b, a + b
    print(b, "Фибо - ещё проще c while")

# Фибо - ещё проще c for
c, b = 0, 1
for _ in range(5):
    c, b = b, c + b
    print(b, "Фибо - ещё проще c for")

#  1_reduce с выводом промежуточных рез
from functools import reduce


def sum_with_print(acum, x):
    new_acc = acum + x
    print(f"{acum} + {x} = {new_acc}")
    return new_acc


# Начальное значение - 0, чтобы начать суммирование с первого элемента
a = [1, 2, 3, 4]
result = reduce(sum_with_print, a, 0)
print(result, "reduce с выводом промежуточных рез", "\n")


#  2_reduce с выводом промежуточных рез
def sum_with_save(acum, x):
    current_sum = acum[-1] + x
    acum.append(current_sum)
    return acum


a = [1, 2, 3, 4]
intermediate_sums = reduce(sum_with_save, a, [0])[
                    1:
                    ]  # Начинаем с [0], убираем начальный 0

print("Промежуточные суммы:", intermediate_sums, "\n")


# Фибо с while
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Использование генератора
fib_gen = fibonacci_generator()

# Печать первых 10 чисел Фибоначчи
for _ in range(5):
    print(next(fib_gen), "Фибо с while", "\n")


# Рекурсия простенькая
def foo(c):
    print(c)
    if c > 5:
        return c
    else:
        foo(c + 1)
    print(c)
    return c


print(foo(1), "Рекурсия простенькая", "\n")


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


# Факториал просто 1
def foo(x):
    if x == 1:  # базовый случай
        return x
    return x * foo(x - 1)  # рекурсивный случай


print(foo(3), "Факториал просто 1")


# Факториал просто 2
def foo(x):
    return x * foo(x - 1) if x else 1  # рекусивный случай и базовый в одном реторне


print(foo(5), "рекусивный случай и базовый в одном return", "\n")
#%%
# Факториал с циклом for
factorial = 4
for i in range(1, factorial):
    factorial *= i
    print(factorial, "Факториал с циклом for", "\n")

#%%
# Факториал с циклом for обернули в функцию
def fc(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res


print(fc(5), "Факториал с циклом for обернули в функцию", "\n")


# Мой варриант: Факториал с циклом for обернули в функцию
def fc(x):
    fact = x
    for i in range(1, fact):
        fact *= i
    return fact


print(fc(5), "Мой варриант: Факториал с циклом for обернули в функцию", "\n")

# ФИБО с while
a, b = 0, 1
n = 0
while n < 4:
    n += 1
    a, b = b, a + b
print(b, "ФИБО с while", "\n")

# TODO Записать наибольший или наименьший результат операции drop = x_ * y_
#  -np.inf или np.inf -> инициализация от которой зависит результат

x = [10, 200, 55, 700]
y = [100, 1, 2, 1]


# Наименьший результат операции +np.inf и условие со знаком <
def foo(x_, y_):
    x_best = np.inf
    y_best = None
    for x_, y_ in zip(x_, y_):
        drop = x_ * y_
        if drop < x_best:
            x_best = drop
            y_best = y_
    return f'y = {y_best},x = {x_best}'


print('Наименьший результат операции : \n', foo(x, y), '\n')


# Наибольший результат операции -np.inf и условие со знаком >

def foo(x_, y_):
    x_best = -np.inf
    y_best = None
    for x_, y_ in zip(x_, y_):
        drop = x_ * y_
        if drop > x_best:
            x_best = drop
            y_best = y_
    return f'y = {y_best},x = {x_best}'


print('Наибольший результат операции : \n', foo(x, y))


#%% TODO fibonachi from doc python
def fib():
    y, x = 0, 1

    while 1:
        yield x
        y, x = x, y + x


f = (fib())

next(f)
# next(f)
# next(f)
# next(f)

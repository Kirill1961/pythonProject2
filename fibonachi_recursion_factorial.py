

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
intermediate_sums = reduce(sum_with_save, a, [0])[1:]  # Начинаем с [0], убираем начальный 0

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
print(foo(5), "рекусивный случай и базовый в одном return")
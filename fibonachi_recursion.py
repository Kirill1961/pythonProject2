

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

#  1_reduce с выводом промежуточных рез
from functools import reduce


def sum_with_print(acumulator, x):
    new_acc = acumulator + x
    print(f"{acumulator} + {x} = {new_acc}")
    return new_acc


# Начальное значение - 0, чтобы начать суммирование с первого элемента
a = [1, 2, 3, 4]
result = reduce(sum_with_print, a, 0)
print(result, "reduce с выводом промежуточных рез", "\n")


#  2_reduce с выводом промежуточных рез
def sum_with_save(acumulator, x):
    current_sum = acumulator[-1] + x
    acumulator.append(current_sum)
    return acumulator

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

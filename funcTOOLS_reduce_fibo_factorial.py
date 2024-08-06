from functools import wraps, cache, lru_cache
import functools
import random
import logging

logging.basicConfig(level=logging.DEBUG, filename="x_o_r.log", filemode="w")
logger = logging.getLogger("X_O_R")
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

" Кэширование - запоминаем предыдущие результаты вычисления используем их для след вычисления "


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


print(factorial(5), "с помощью @cache отображает результат предыдущего кэшированного значения")
logger.debug(factorial(10))  # не кэшированный ранее результат, делает 11 рекурсивных вызовов
logger.debug(factorial(5))  # просто отображает результат кэшированного значения
logger.debug(factorial(12))  # делает два новых рекурсивных вызова, другие 10 кэшированы


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)  # возврат ряда Фибоначи


[fib(n) for n in range(16)]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
print([fib(n) for n in range(16)], " возврат ряда Фибоначи")


# logger.debug([fib(n) for n in range(16)])


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print("Calling decorated function 1")
        logger.debug("Calling decorated function")

        return f(*args, **kwds)

    return wrapper


@my_decorator  # вместо присваивания переменной внешней ф-ции используем декоратор
def example():
    """Docstring"""

    return ("Called example function 2")


print(example(), "вместо присваивания переменной внешней ф-ции используем декоратор")
logger.debug((example(), example.__name__, example.__doc__))


def foo(x, y):
    return x + y


# в reduce две переменные это аккумулирующая и прибавляющееся value и element
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


print(reduce(foo, [1, 2, 3, 4], 2), "reduce")


# reduce - с выводом промежуточных значений
#  initializer - добавляется к последовательности как начальный элемент
#  перед которым проходят все элементы исходной последовательности.
def sum_with_save(acc, x):
    current_sum = acc[-1] + x  # Суммируем последнее значение из аккумулятора с текущим элементом x
    acc.append(current_sum)  # Добавляем новый промежуточный результат в аккумулятор
    return acc  # Возвращаем обновлённый аккумулятор


a = [10, 20, 30, 40]
result = reduce(sum_with_save, a, [0])  # [0] - начальный элемент, Инициализация пустого списка для аккумуляции "acc"
print(result, "reduce - с выводом промежуточных значений")

""" """
a = [10, 20, 30, 40]


def sum_with_save(x, y):
    print("\t" * 4, x, "x - аккумулирующая переменная, [0] - заданная структура аккумулятора")
    print(y, "y - итерация ОБ из коллекции < a > ")
    return x, y  # Возвращаем обновлённый аккумулятор


result = reduce(sum_with_save, a, [0])
print(result, "[0] - заданная структура аккумулятора")

# использования initializer в reduce c lambda
from functools import reduce


# Применение reduce с начальным значением (например, 10)
a = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, a, 10)
print(result, "Применение reduce с начальным значением (например, 10)")  # Выведет 20 (10 + 1 + 2 + 3 + 4)


# Применение reduce с начальным значением (например, "Start: ")
strings = ["one", " ", "two", " ","three"]
result = reduce(lambda x, y: x + y, strings, "Start: ")
print(result)  # Выведет "Start: onetwothree"


# reduce - сумма квадратов
lst = [1, 2, 3]
def sum_of_squares(nums):
    return reduce(lambda x, y: x + y**2, nums, 10)
print(f"reduce - сумма квадратов = {sum_of_squares(lst)}")
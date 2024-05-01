from functools import wraps, cache, lru_cache
import functools

import logging

logging.basicConfig(level=logging.DEBUG, filename="x_o_r.log", filemode="w")
logger = logging.getLogger("X_O_R")
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

" Кэширование - запоминаем предыдущие результаты вычисления используем их для след вычисления "


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


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

logger.debug([fib(n) for n in range(16)])


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        logger.debug("Calling decorated function")

        return f(*args, **kwds)

    return wrapper


@my_decorator  # вместо присваивания переменной внешней ф-ции используем декоратор
def example():
    """Docstring"""

    return ("Called example function")


logger.debug((example(), example.__name__, example.__doc__))

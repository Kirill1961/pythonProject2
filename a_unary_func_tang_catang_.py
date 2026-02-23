
# Унарное отрицание ф-ции a(x)

def a(x):
    return x ** 2


def n(f):
    return (-f) # возвращает отрицание ф-ции a(x)


print(n(a(3)))

# Угловой коэфф переводим в градусы
# Угловой коэфф он же  Тангенс угла - отношение катетов

from math import atan, pi
import random
tg_ = 0.45

print(atan(0.45)) # перевод из коэфф в радианы
print ((atan(0.45 ) * (180 / pi))) # перевод из радиан в градусы

""" LIST """
d = list(range(5))
print(d)

""" shuffle перемешивание"""
r = list(range(5))
random.shuffle(r)
print(r)
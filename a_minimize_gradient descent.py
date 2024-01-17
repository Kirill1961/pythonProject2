
from turtle import distance
import random
import turtle
import matplotlib.pyplot as plt
from functools import partial

# Шаг градиента, двигаемся в направлении АНТИградиента

# Для примера взяли ф-цию одной переменной y = x^2

def square(x):
    # print(x, ' square')
    return x[0] ** 3


# Производная y = x^2
def derivative(x):
    return [(3 * x)**2 for x in v ]


def step(v, direction, step_size):
    # двигаться с шагом step_size в направлении от v
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]# direction х -0.01 изм напр градие

# Градиент суммы квадратов
def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]
# Произвольная отправная точка
v = [random.randint(-10, 10) for i in range(2)]


""" для вывода (next_v, v)"""
gradient = sum_of_squares_gradient(v)
next_v = step (v, gradient, -0.01)

print(next_v, v, ' next_v, v')

tolerance = 0.00001 # константа точности расчёта


while True:
    gradient = sum_of_squares_gradient(v) # вычислить градиент в v
    # print(gradient,v, ' gradient')
    next_v = step (v, gradient, -0.1) # сделать отрицательный шаг градиента
    # print(turtle.distance(next_v[0], v[0])) # растение от '0' до точки с координатами (next_v[0], v[0])
    if distance (next_v[0], v[0]) < tolerance: # останов при достижении приемлемого уровня (схождения)
        break
    v = next_v # продолжить если нет



def safe(f):  # Вернуть ф-ю safe_f() только если она не возвращает бесконечность
    def safe_f(*args, **kwargs):
        try:
            # print(f, ' ffff')
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f


# Пакетная минимизация,
# минимизация функции ошибок

def minimize_batch (target_fn, gradient_fn, theta_0, tolerance):
    # print(theta_0, ' theta_0')
    # print( target_fn, ' target_fn')
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0 # стартовая точка градиента, theta - вектор параметров, theta_0 - исх значение
    print(theta, ' theta')
    target_fn = safe(target_fn) # вернулась проверенная ф-я target_fn()
    value = target_fn(theta) # ф-ия в стартовой точке theta_0
    # print(value, ' value ')
    while True:
        gradient = gradient_fn(theta) # ▼ в последующих точках ф-ии
        print(gradient, ' gradient')
        next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]
        print(next_thetas, ' next_thetas')
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)
        print(value, ' value',  next_value, ' next_value')
        if abs(value - next_value) < tolerance:
            print(theta, ' theta' , next_theta, ' next_theta')
            return theta
        else:
            theta, value = next_theta, next_value

minimize_batch(square, derivative, v, tolerance=0.00001)


# отрицание результата на выходе
def negate(f):
    return lambda *args, **kwargs: -f(*args, **kwargs)# при любом Х возращаем - f(x)
    # print(unar(2))
# print(negate(derivative(2)))



# Отрицание списка результатов

def negate_all(f):
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]
# print(negate(derivative), ' drv drv drv')


# Минимизация отрицания

def maximize_bath(target_fn, gradient_fn, theta_0, tolerance):
    return  minimize_batch((target_fn), negate_all(gradient_fn), theta_0, tolerance)

# print(maximize_bath(square, sum_of_squares_gradient, v, tolerance=0.00001), ' max max max')


# Стохастическая минимизация

# def random_order(data):
#     indexes = [i for i,_ in enumerate(data)]
#     random.shuffle(indexes) # перемешивание индексов данных для случайного выбора
#     for i in indexes:
#         # print(data[i])
#         yield data[i]
# for y in random_order([11,22,33]):
#     print(y)
# print(random_order([11,22,33]))



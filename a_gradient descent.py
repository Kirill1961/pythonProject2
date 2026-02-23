from turtle import distance
import random
import turtle
import matplotlib.pyplot as plt
from functools import partial



# sum_jf_squares - принимает в аргумента вектор значений 'v'
def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v  )


# print(sum_of_squares([2, 4, 6]))

# Отношение приращений (производная при условии ▲х -> 0)
# производная - это касательная в точке с координатами   х ; f(x), отношение ▲у / ▲х -имеет тоже касательную с
# наклоном, но отличную от касательной в точке х ; f(x), если ▲х -> 0 то касательные стремятся друг к другу
# h - это ▲х, чем меньше h (▲х) тем ближе касательные х ; f(x) и у / ▲х

def different_guotient(f, x, h): # в f ф-я 1-й переменной, подставляется square
    # print(f, x, '- x ;', x + h, '- x + h ;', (x + h) - x, '- ▲x')
    return (f(x + h) - f(x)) / h  # h - это '▲ х', приращение на оси х, f(x + h) - f(x)) - это '▲ у'


# Для примера взяли ф-цию одной переменной y = x^2
def square(x):
    # print(x, ' square')
    return x ** 2


# Производная y = x^2
def derivative(x):
    return 2 * x





# Оценка производной
derivative_estimate = partial(different_guotient, square, h=0.00001)

# Сравниваем на графике производную с оценкой производной
xs = range(-10, 10) # Создаём диапазон значений для функции square
plt.title('qqq')
plt.plot(xs, [derivative(x) for x in xs], 'rx')  # производная
plt.plot(xs, [derivative_estimate(x) for x in xs], 'b+')  # оценка производной
# plt.show()



# Рассмотрим ф-ю многих переменных

# Вычислим i-е частное отношение приращения (i-ю частную производную)в векторе v
def partial_difference_quotient(f, v, i, h):
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w)[i] - f(v)[i]) / h # (f(w)[i] - f(v)[i]) это ▲у i-тое , h это ▲х i-тое

# Оценка градиента
def estimate_gradient(f, v, h = 0.00001):
    return [partial_difference_quotient(f, v, i,  h) for i, _ in enumerate(v)]

print(estimate_gradient(derivative, v=[1,2,3,4,5,6,7]), ' градиентный подъём')



# Использование градиента

# ШАГ градиента, двигаемся в направлении АНТИградиента


def step(v, direction, step_size):  # direction - это Градиент
    # двигаться с шагом step_size в направлении от v
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]# direction х -0.01 изм напр градие

# Градиент суммы квадратов
def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]
# Произвольная отправная точка
v = [random.randint(-10, 10) for i in range(3)]  # Тои параболы
print(v, ' произвольная точка старта')

tolerance = 0.00001 # константа точности расчёта


while True:
    gradient = sum_of_squares_gradient(v)  # вычислить градиент в v
    next_v = step(v, gradient, -0.01)  # сделать отрицательный шаг градиента
    # print(turtle.distance(next_v[0], v[0])) # растение от '0' до точки с координатами (next_v[0], v[0])
    if distance(next_v[0], v[0]) < tolerance:  # останов при достижении приемлемого уровня (схождения), distance - измерение расстояния
        break
    v = next_v  # продолжить если нет


# Оптимальный размер шага
# безопасня версия,

def safe(f):  # Вернуть ф-ю safe_f() только если она не возвращает бесконечность
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f


# Пакетная минимизация

def minimize_batch (target_fn, gradient_fn, theta_0, tolerance):
    print(theta_0, ' qqqqq')
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0 # стартовая точка градиента
    target_fn = safe(target_fn) # вернулась проверенная ф-я target_fn()
    value = target_fn(theta) # ф-ия в стартовой точке theta_0
    while True:
        gradient = gradient_fn(theta) # ▼ в последующих точках ф-ии
        next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value

minimize_batch(square, sum_of_squares_gradient, v, tolerance=0.01)






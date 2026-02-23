import random
import math
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import binom

# наступление события, что оба ребёнка девочки
def random_kid():
    return random.choice(['boy', 'girl'])


# print(random_kid())

both_girls = 0
older_girl = 0
either_girl = 0
younger_girl = 0
both_boys = 0
either_boy = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == 'girl':  # условие если старший ребёнок девочка
        older_girl += 1
    if older == 'girl' and younger == 'girl':  # условие если старший и младший ребёнок девочки
        both_girls += 1
    if older == 'girl' or younger == 'girl':  # условие если старший илиё младший ребёнок девочки
        either_girl += 1
    if younger == 'girl':
        younger_girl += 1
    if older == 'boy' and younger == 'boy':
        both_boys += 1
    if older == 'boy' or younger == 'boy':
        either_boy += 1
print('younger_girl / младшая', younger_girl)
print('older_girl/старшая', older_girl)
print('both_girls/ обе девочки', both_girls)
print('either_girl/ любая из них', either_girl)
print('both_boys / обa мальчика', both_boys)
print('either_boy / любой из мальчиков', either_boy)


# ДФР - probability density function (pdf), ф-ция плотности равномерного распределения
# вероятность наблюдать значение в определённом интервале = интегралу взятому в этом пределе
def uniform_pdf(a):  # Равномерность распределения

    print((a))
    return 1 if a >= 0 and a < 1 else 0


print(uniform_pdf(random.random()))


# ДФР нормального распределения

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


print(normal_pdf(2, 2, 2))

# Графики некоторых ДФР

xs = [x / 10.0 for x in range(-50, 50)]
print(xs)
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.legend()
plt.show()


# ИФР - commutative distribution function (cdf), интегральная ф-ция распределения,
# определяет вероятность случайного значения  < или = некоторому значению " x ".

def uniform_cdf(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


print(uniform_cdf(random.random()))


# ИФР нормального распределения ещё называют ф-ция ошибки

def normal_cdf(x, mu=0, sigma=1):
    # print(x, 'qqqqq')
    return ((1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2)


# xs = [x_ / 10.0 for x_ in range (-50, 50)]
# # print(xs)
# plt.plot(xs, [normal_cdf(x_, sigma=1) for x_ in xs], '-', label='mu=0, sigma=1')
# plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
# plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
# plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
# plt.legend()
# plt.show()


# Обращаем normal_cdf, двоичный поиск, по заданной вероятности ищем
# значение случайной величины Z, выборка Z -10 / 10
# tolerance - это константа точности.

def invers_normal_cdf(p, mu=0, sigma=1, tolerance=0.0001):
    # print('\t' * 8, p)
    if mu != 0 or sigma != 1:
        return mu + sigma * invers_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10, 0
    hi_z, hi_p = 10, 1
    while hi_z - low_z > tolerance:
        # print(hi_z,low_z,  ' hi_z, low_z - заданные нижн и верхн граница z ')
        mid_z = (low_z + hi_z) / 2
        # print('\t' * 2, mid_z, ' mid_z  - среднее случайной величины z ')

        mid_p = normal_cdf(mid_z)
        # print('\t' * 4,mid_p, ' mid_p - вероятность ср велечины z')
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
            # print(low_z, low_p, ' low_z, low_p')
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
            # print(hi_z, hi_p, '  hi_z, hi_p')
        else:
            break
    return mid_z


# print(invers_normal_cdf(0.1), ' invers_normal_cdf')


# Распределение Бернулли, Независимое испытание Бернулли в котором два исхода 1 и 0
# , с постоянной вероятностью

def bernoulli_trial(p):
    # print(random.random(), ' random.random')
    return 1 if random.random() < p else 0


# print(bernoulli_trial(0.5), ' bernoulli_trial')
#
#
#
#
# Биноминальное распределение

def binominal(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

# n - кол-во опытов, p - вероятность успеха
print(binominal(100, 0.5), ' binominal')


def make_hist(p, n, num_points):
    # print(num_points, ' num_points')
    data = [binominal(n, p) for _ in range(num_points)]
    histogram = Counter(data)
    # print(histogram)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()], 0.5, color='0.8')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    # plt.show()


make_hist(0.75, 100, 1000)


#
# Апроксимация биноминальной случайной величины Х к нормальному распределению

def normal_aproxim_to_binominal(n, p):
    # mu - среднее, вероятность * на общее число опытов
    mu = p * n
    # sigma - это  sd
    sigma = math.sqrt(p * (1 - p) * n)
    print(mu, sigma, ' normal_aproxim_to_binominal(n, p)')
    return mu, sigma


print(normal_aproxim_to_binominal(10, 0.5), ' normal_aproxim_to_binominal')
print('')

# Вероятность что значение нормальной случ величины Х лежит ниже порогового значения
normal_probability_below = normal_cdf


# Норм случ величина выше порогового значения если не ниже его

def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)


# print(normal_probability_above(0.1))

# " Х " - лежит между если ниже hi, но выше lo

def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# " Х " - лежит за пределами если оно не внутри

def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


# Верхняя граница нормальной величины
def normal_apper_bound(probability, mu=0, sigma=1):
    """ возвращает z для которого P(Z <= z) = prodability """
    return invers_normal_cdf(probability, mu, sigma)


print(normal_apper_bound(0.9), ' apper возвр верхн границу величины Z при заданной вероятности')


# Нижняя граница нормальной величины
def normal_lower_bound(probability, mu=0, sigma=1):
    """ возвращает z для которого P(Z >= z) = prodability """
    return invers_normal_cdf(1 - probability, mu, sigma)


print(normal_lower_bound(0.9), ' lower возвр нижн границу величины Z при заданной вероятности')


# Двусторонние границы нормальной случайной величины
def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """ возвращает симметричные границы в которых находится указанная вероятность"""
    tail_probability = (1 - probability) / 2

    # Верхняя граница должна иметь значение хвостовой вероятности
    # tail_probability выше её

    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # Нижняя граница должна иметь значение хвостовой вероятности
    # tail_probability ниже её
    lower_bound = normal_apper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound


# print(normal_two_sided_bounds (0.9))

# 2х сторонние границы нормальной случайной величины Z
mu_0, sigma_0 = normal_aproxim_to_binominal(1000, 0.5)
print(mu_0, sigma_0)
print(normal_two_sided_bounds(0.95, mu_0, sigma_0), ' 2х сторонние границы Z')

# 95% границы при условии что р = 0,5
lo, hi = normal_two_sided_bounds(0.5, mu_0, sigma_0)
print(normal_two_sided_bounds(0.5, mu_0, sigma_0), ' 95% границы при условии что р = 0,5')

# Фактические mu и  sugma при р = 0,55
mu_1, sigma_1 = normal_aproxim_to_binominal(1000, 0.55)
print(normal_aproxim_to_binominal(1000, 0.55), ' Фактические mu и  sugma при р = 0,55')


# 2х стороннее р - значение
def two_side_p_value(x, mu=0, sigma=1):
    print(x, ' two_side_p_value')
    if x >= mu:
        # если х больше среднего значения то значения в хвосте больше х
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # если х меньше среднего значения то значения в хвосте меньше х
        return 2 * normal_probability_below(x, mu, sigma)


print(two_side_p_value(529.5, mu_0, sigma_0), ' При 1000 бросков выпадение 530 орлов с  р = 0.062')


# A / B Тестирование, испытание Бернули
# А - реклама 1, В - реклама 2, N - общее число просмотров, n - число кликов
# n / N нормальная случ величина с вероятностьо " р "

#  Оценочные параметры
def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma


# print(estimated_parameters(1000, 180))


# Статистика а / b тестирования
def a_b_best_statbatic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    # print(p_B - p_A, p_B, p_A)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)


z = a_b_best_statbatic(1000, 200, 1000, 150)
print(z)
print(two_side_p_value(z))

print('')

""" БЕТА РАСПРЕДЕЛЕНИЕ"""


# Стат вывод Байеса, априорное распределение берём из бета-распределения
# ВЕРОЯТНОСТЬ ВРОЯТНОСТИ,


# в данном примере считаем вероятность орлов при подбросе монеты 10 раз из них - 3 орёл и соотв 7 - решка
# значит альфа = 3, бета - 7,
def B(alfa, beta):
    return math.gamma(alfa) * math.gamma(beta) / math.gamma(alfa + beta)


# print(B(3, 7), 'В-функция')


# вес данного распределения / мат ожидание,
# это расчёт для значения априорной случайной вероятности 'х'б для использования в beta_pdf(x, alfa, beta)
def expected_for_beta_distribution(alfa, beta):
    return alfa / (alfa + beta)


# ДФР(PDF), апосториорная плотность распределения для бета-распределёной случайной вероятности 'х'
def beta_pdf(x, alfa, beta):
    if x < 0 or x > 1:
        return 0
    print(x ** (alfa - 1) * (1 - x) ** (beta - 1) / B(alfa, beta), 'по оси У, PDF для бета-распределёной величины х')
    print(expected_for_beta_distribution(alfa, beta), 'по оси Х, вес данного распределения / мат ожидание')
    return x ** (alfa - 1) * (1 - x) ** (beta - 1) / B(alfa, beta), expected_for_beta_distribution(alfa, beta)


print(beta_pdf(0.2, 4, 16), ' beta_pdf')


# Биномиальное распределение scipy.stats import binom
# n - количество испытаний, p - вероятность успеха
n = 10
p = 0.7

# Вероятность получить ровно 5 успехов из 10 испытаний
prob_5_successes = binom.pmf(5, n, p)
print(f"Вероятность 5 успехов из 10 испытаний: {prob_5_successes:.4f}")

# Генерация случайного числа успехов из 10 испытаний
binom_rv = binom.rvs(n, p, size=10)  # Генерация 10 испытаний
print(binom_rv)
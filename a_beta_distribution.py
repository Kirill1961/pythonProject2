import math
import matplotlib.pyplot as plt

""" БЕТА РАСПРЕДЕЛЕНИЕ"""

# в данном примере считаем вероятность орлов при подбросе монеты 10 раз из них - 3 орёл и соотв 7 - решка
# значит альфа = 3, бета - 7,
def B(alfa, beta):
    return math.gamma(alfa) * math.gamma(beta) / math.gamma(alfa + beta)
# print(B(10, 10), 'В-функция')


# вес данного распределения / мат ожидание,
# это расчёт для значения априорной случайной вероятности 'х'б для использования в beta_pdf(x, alfa, beta)
def expected_for_beta_distribution(alfa, beta):
    return alfa / (alfa + beta)


# ДФР(PDF), апосториорная плотность распределения для бета-распределёной случайной вероятности 'х'
def beta_pdf(x, alfa, beta):
    if x < 0 or x > 1:
        return 0
    print(x**(alfa - 1)* (1 - x)**(beta - 1) / B(alfa, beta), 'по оси У, PDF для бета-распределёной величины х')
    print(expected_for_beta_distribution(alfa, beta), 'по оси Х, вес данного распределения / мат ожидание')
    return x**(alfa - 1)* (1 - x)**(beta - 1) / B(alfa, beta)
# print(beta_pdf(0.46, 23, 27), ' beta_pdf')



""" Графики PDF бета-распределенной величины  'x'  """

# Графики некоторых ДФР
xs = [x / 100 for x in range (100)]
# print(xs)
plt.plot(xs, [beta_pdf(x, 4, 8) for x in xs], ':', label='alfa=4 beta=8 Е=0.33')
plt.plot(xs, [beta_pdf(x, 10, 10) for x in xs], '-.', label='alfa=10 beta=10 Е=0.5')
plt.plot(xs, [beta_pdf(x, 16, 4) for x in xs], '-', label='alfa=16 beta=4 Е=0.8')
plt.title('Графики PDF бета-распределенной величины  X ')
plt.legend()
plt.show()
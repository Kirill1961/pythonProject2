import math

import matplotlib.pyplot as plt
from collections import Counter
from math import sqrt

num_friends = [13, 9, 7, 5, 3, 10]
daily_minutes = [31, 30, 21, 20, 12]


def mean_x_y(x_):
    return sum(x_) / len(x_)


print(mean_x_y(num_friends), ' среднее варриационного ряда')
print('  ')


def de_mean(x_y):
    x_y_bar = mean_x_y(x_y)  # Среднее арифметическое коллекции
    print(x_y_bar, '   x_bar среднее арифметическое варриационного ряда')
    print('  ')
    return [i - x_y_bar for i in x_y]  # среднее результата будет равно нулю


# print(de_mean(num_friends), '  отклонение от среднего = варианта минус среднее ')


def variance_for_correlation(x_y_dev):  # ДИСПЕРСИЯ Или variance
    n = len(x_y_dev)
    deviations = de_mean(x_y_dev)
    print(n, ' длинна списка', deviations, ' deviations')
    sum_of_squares = [xi_yi ** 2 for xi_yi in deviations]  # прокручиваем отклонения и возводим в квадрат
    print('  ')
    print(sum_of_squares, ' квадрат отклонения от среднего')
    print('  ')
    print(sum(sum_of_squares), '       сумма квадратов')
    print('  ')
    variance_su_sq = (sum(sum_of_squares))
    print ("\t" * 7, variance_su_sq / (n - 1),' ДИСПЕРСИЯ или variance это сумма квадратов отклонений / n - 1' )
    return variance_su_sq / (n - 1)  # возврат вычисленного значения в точку вызова standart_deviations(х)

def variance(x):  # ДИСПЕРСИЯ Или variance
    n = len(x)
    deviations = de_mean(x)
    print(n, ' длинна списка', deviations, ' deviations')
    sum_of_squares = [y ** 2 for y in deviations]  # прокручиваем отклонения и возводим в квадрат
    print('  ')
    print(sum_of_squares, ' квадрат отклонения от среднего')
    print('  ')
    print(sum(sum_of_squares), '       сумма квадратов')
    print('  ')
    variance_su_sq = (sum(sum_of_squares)) / (n - 1)
    print( "\t" * 4, variance_su_sq, 'ДИСПЕРСИЯ (variance) - это сумма квадратов отклонения / (n - 1) для', num_friends)
    # print('  ')
    # std = math.sqrt(variance_su_sq)
    # print(std, '    std вычисление в теле ф-ции')
    print('  ')
    return sum(sum_of_squares) / (n - 1)  # возврат вычисленного значения в точку вызова standart_deviations(х)



def standart_deviations(x_y):
    return math.sqrt((variance_for_correlation(x_y)))  # вызов ф-ции variance(x_)
    # return math.sqrt((variance(x_y)))  # вызов ф-ции variance(x_)

print( "\t" * 5, standart_deviations(num_friends), ' >>>>>>>>>>>  std со значением дисперсии из  variance(x_)')


def covariance(x_, y_):
    n = len(x_)
    x_bar = mean_x_y(x_)
    y_bar = mean_x_y(y_)
    print(x_bar, y_bar, '<<<<<<<<<<<<<<<<<<  Среднее д/ вариационных рядов " num_friends " и " daily_minutes "')
    x_dev = [x_i - x_bar for x_i in x_]  # Отклонение от среднего для х
    y_dev = [y_i - y_bar for y_i in y_]  # Отклонение от среднего для у
    print('  ')
    print(x_dev, y_dev, '  deviations - Отклонение от среднего д/ вариационных рядов " х " и " у "', "\n")
    sum_mult = [i * k for i, k in zip(x_dev, y_dev)]
    print('  ')
    return (sum(sum_mult) / (n - 1))


print('  ')
print("\t" * 5, covariance(num_friends, daily_minutes), ' KОВАРИАЦИЯ для x_, y_', "\n")

print(num_friends, daily_minutes, ' вариационные ряды для Ковариации')


def correlation(x_, y_):
    stdev_x = standart_deviations(x_)
    stdev_y = standart_deviations(y_)
    print("\t" * 6, stdev_x, stdev_y, 'standart_deviations stdev_x, stdev_y', " \n")
    print('  ')
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x_, y_) / stdev_x / stdev_y
    else:
        return 0


print("\t" * 5, 'correlation = ', correlation(num_friends, daily_minutes))

# Фильтр кореляции от выброса


outlier_index = num_friends.index(13)
print(outlier_index)

num_friends_good = [num_friends[k] for k, i in enumerate(num_friends) if k != outlier_index]

print(num_friends_good, ' удаление выброса из вар ряда num_friends')

daily_minutes_good = [daily_minutes[k] for k, i in enumerate(daily_minutes) if k != outlier_index]

print(daily_minutes_good, ' удаление выброса из вар ряда daily_minutes')

print('correlation = ', correlation(num_friends_good, daily_minutes_good),
      ' Удалили выброс из выборки коэфф увеличился')

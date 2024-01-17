import  math


num_friends_three = [100, 49, 41, 40, 25]
daily_minutes = [31, 32, 37, 34, 20]

mode = 0
print(num_friends_three, daily_minutes, ' вариационные ряды для Ковариации')

def mean(x_):
    return sum(x_) / len(x_)


print(mean(num_friends_three), ' среднее варриационного ряда')
print('  ')
def de_mean(x_):
    x_bar = mean(x_) # Среднее арифметическое коллекции
    print(x_bar, '   x_bar среднее арифметическое варриационного ряда')
    print('  ')
    return [x_ix - x_bar for x_ix in x_] # среднее результата будет равно нулю
print(de_mean(num_friends_three ), '  отклонение от среднего = варианта минус среднее ')

def variance(x_):  # ДИСПЕРСИЯ Или variance
    n = len(x_)
    deviations = de_mean(x_)
    print(n, ' длинна списка', deviations, ' deviations')
    sum_of_squares = [y_iy**2 for y_iy in deviations] # прокручиваем отклонения и возводим в квадрат
    print('  ')
    print(sum_of_squares, ' квадрат отклонения от среднего')
    print('  ')
    print(sum(sum_of_squares), '       сумма квадратов')
    print('  ')
    variance_su_sq = (sum(sum_of_squares))/(n - 1)
    print (variance_su_sq,'         ДИСПЕРСИЯ или variance это сумма квадратов / n - 1' )
    return sum(sum_of_squares)/(n-1)  # возврат вычисленного значения в точку вызова standart_deviations(х)
print('  ')

def standart_deviations(x_):
    return math.sqrt((variance(x_))) # вызов ф-ции variance(x_)
print(standart_deviations(num_friends_three ), '    std со значением дисперсии из  variance(x_)')

print('  ')
def covariance(x_, y_):
    n = len(x_)
    x_bar = mean(x_)
    y_bar = mean(y_)
    print('  ')
    print(x_bar, y_bar, '   Среднее д/ вариационных рядов " х " и " у "')
    x_dev = [x_i - x_bar for x_i in x_]   # Отклонение от среднего для х
    y_dev = [y_i - y_bar for y_i in y_]    # Отклонение от среднего для у
    print('  ')
    print(x_dev , y_dev, '  deviations - Отклонение от среднего д/ вариационных рядов " х " и " у "', "\n")
    sum_mult = [i * k for i, k in zip(x_dev , y_dev)]
    return (sum(sum_mult)/(n - 1))

print('  ')
print(covariance(num_friends_three, daily_minutes ), '                  KОВАРИАЦИЯ ')
print('  ')
print(num_friends_three, daily_minutes, ' вариационные ряды для Ковариации', "\n")

def correlation(x_, y_):
    stdev_x = standart_deviations(x_)
    stdev_y = standart_deviations(y_)
    print('  ')
    print(stdev_x, stdev_y, '  standart_deviations for x_,y_')
    print('  ')
    if stdev_x>0 and stdev_y>0 :
        return  covariance(x_, y_)/ stdev_x / stdev_y
    else:
        return 0
print('correlation = ' ,correlation(num_friends_three, daily_minutes))

# Фильтр кореляции от выброса


outlier_index = num_friends_three.index(100)

num_friends_good = [num_friends_three[k] for k, i in enumerate(num_friends_three) if k != outlier_index]
print('  ')
print(num_friends_good, ' удаление выброса из вар ряда num_friends_three')

daily_minutes_good = [daily_minutes[k] for k, i in enumerate(daily_minutes) if k != outlier_index]

print(daily_minutes_good, ' удаление выброса из вар ряда daily_minutes')
print('  ')
print('correlation = ', correlation(num_friends_good, daily_minutes_good),
      ' Удалили выброс из выборки коэфф увеличился')

def predict(alfa, beta, x_i):
    return x_i * beta + alfa  # прогнозируемый  Ypredict


def total_sum_of_squares(y_mean):
    return sum([(y_total - y_mean)**2 for y_total in daily_minutes])
# print(total_sum_of_squares(mean(daily_minutes)), " total_sum_of_squares")


def sum_least_squares(alfa, beta, y_mean):
    return sum([(predict(alfa, beta, y_predict) - y_mean)**2 for y_predict in daily_minutes])
# print(sum_least_squares(mean(daily_minutes)), " sum_least_squares")


def r_square(alfa, beta ):
    print(sum_least_squares(alfa, beta, mean(daily_minutes)), " sum_least_squares")
    print(total_sum_of_squares(mean(daily_minutes)), " total_sum_of_squares")
    return 1 - (sum_least_squares(alfa, beta, mean(daily_minutes)) / total_sum_of_squares(mean(daily_minutes)))
print(r_square(22.95, 0.903))

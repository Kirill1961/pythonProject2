import math
import random

num_friends_three = [100, 49, 41, 40, 25]
# daily_minutes = [31, 32, 37, 34, 20]
daily_minutes = [31, 32, 37, 34, 20]


print(num_friends_three, daily_minutes, " вариационные ряды для Ковариации", "\n")


def mean(x_):
    return sum(x_) / len(x_)


print(mean(num_friends_three), " среднее варриационного ряда", "\n")


def de_mean(x_):
    x_bar = mean(x_)  # Среднее арифметическое коллекции
    print(x_bar, "   x_bar среднее арифметическое варриационного ряда", "\n")

    return [x_ix - x_bar for x_ix in x_]  # Отклонение У наблюдаемое


# print(de_mean(num_friends_three ), '  отклонение от среднего Уobserver = варианта минус среднее ', "\n")


def variance(x_):  # ДИСПЕРСИЯ Или variance
    n = len(x_)
    deviations = de_mean(x_)
    print(n, " длинна списка", deviations, " deviations", "\n")
    sum_of_squares = [
        y_iy**2 for y_iy in deviations
    ]  # прокручиваем отклонения и возводим в квадрат

    print(sum_of_squares, " квадрат отклонения от среднего", "\n")

    print(sum(sum_of_squares), "       сумма квадратов", "\n")

    variance_su_sq = (sum(sum_of_squares)) / (n - 1)
    print(
        variance_su_sq,
        "         ДИСПЕРСИЯ или variance это сумма квадратов deviations / n - 1",
        "\n",
    )
    return sum(sum_of_squares) / (
        n - 1
    )  # возврат вычисленного значения в точку вызова standart_deviations(х)


def standart_deviations(x_):
    return math.sqrt((variance(x_)))  # std, стандартное отклонение - √ из дисперсии


# print(standart_deviations(num_friends_three ), '  std, стандартное отклонение это √ из дисперсии - variance(x_)')


def covariance(x_, y_):
    n = len(x_)
    x_bar = mean(x_)
    y_bar = mean(y_)
    print(" ")
    print(x_bar, y_bar, '   Среднее д/ вариационных рядов " х_ " и " у_ "', "\n")
    x_dev = [x_i - x_bar for x_i in x_]  # Отклонение от среднего для х_
    y_dev = [y_i - y_bar for y_i in y_]  # Отклонение от среднего для у_
    print(
        x_dev,
        y_dev,
        '  deviations - Отклонение от среднего д/ вариационных рядов " х_ " и " у_ "',
        "\n",
    )
    print(
        [i for i in zip(x_dev, y_dev)],
        " >>> пары отклонений от среднего Х и У >>>",
        "\n",
    )
    sum_multiply = [
        i * k for i, k in zip(x_dev, y_dev)
    ]  # произведение разбросов x_dev и y_dev
    return sum(sum_multiply) / (
        n - 1
    )  # covariance - сумма произведений отклонений Х и У от среднего


print(
    covariance(num_friends_three, daily_minutes), "                  KОВАРИАЦИЯ ", "\n"
)

print(num_friends_three, daily_minutes, " вариационные ряды для Ковариации", "\n")


def correlation(x_, y_):
    stdev_x = standart_deviations(x_)
    stdev_y = standart_deviations(y_)
    print(stdev_x, stdev_y, "  standart_deviations for x_,y_", "\n")
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x_, y_) / stdev_x / stdev_y
    else:
        return 0


print("correlation = ", correlation(num_friends_three, daily_minutes), "\n")


# Фильтр кореляции от выброса

outlier_index = num_friends_three.index(100)
print(
    outlier_index, " индекс выброса значения сильно отличающегося от всего ряда", "\n"
)
num_friends_good = [
    num_friends_three[k] for k, i in enumerate(num_friends_three) if k != outlier_index
]
print(num_friends_good, " удаление выброса из вар ряда num_friends_three", "\n")

daily_minutes_good = [
    daily_minutes[k] for k, i in enumerate(daily_minutes) if k != outlier_index
]
print(daily_minutes_good, " удаление выброса из вар ряда daily_minutes", "\n")

print(
    "correlation = ",
    correlation(num_friends_good, daily_minutes_good),
    " Удалили выброс из выборки коэфф увеличился",
)


def predict(alpha, beta, x_i):
    return x_i * beta + alpha  # прогнозируемый  Ypredict


def error(alpha, beta, x_i, y_i):
    y_predict_of_residual = y_i - predict(alpha, beta, x_i)  # отклонение Ypredict
    print(y_predict_of_residual, " отклонение Ypredict" "\n")
    return y_predict_of_residual


# x_lo = [ 49, 41, 40, 25]u
# y_lo = [ 32, 37, 34, 20]


def sum_of_square_error(*alpha_beta):
    return sum(
        [
            error(
                *alpha_beta,
                x_i,
                y_i,
            )
            ** 2
            for x_i, y_i in zip(num_friends_three, daily_minutes)
        ]
    )


print(
    sum_of_square_error(27.849969715324047, 0.05784373107207752)
)  # *alpha_beta - подставляем коэф alpha и beta
# , вычисленные МНК


def least_squares_fit(x, y):
    # print(x,y, "  о ц е н о ч н ы е коэффициенты", "\n")
    beta = (
        correlation(x, y) * standart_deviations(y) / standart_deviations(x)
    )  # beta - коэффициент регрессии
    alpha = mean(y) - beta * mean(x)  # alpha - смещение
    print(
        "  о ц е н о ч н ы е к о э ф ф и ц и е н т ы",
        alpha,
        " - alpha",
        beta,
        " - beta",
        "\n",
    )
    return alpha, beta


print(
    "\t" * 4,
    least_squares_fit(num_friends_three, daily_minutes),
    " alpha и beta методом " "- суммы наименьших квадратов",
    "\n",
)


def total_sum_of_squares(y_mean):
    return sum([(y_total - y_mean) ** 2 for y_total in daily_minutes])


# print(total_sum_of_squares(mean(daily_minutes)), " total_sum_of_squares")


def sum_least_squares(alpha, beta, y_mean):
    return sum(
        [(predict(alpha, beta, y_predict) - y_mean) ** 2 for y_predict in daily_minutes]
    )


# print(sum_least_squares(mean(daily_minutes)), " sum_least_squares")


def r_square(alpha, beta):
    print(sum_least_squares(alpha, beta, mean(daily_minutes)), " sum_least_squares")
    print(total_sum_of_squares(mean(daily_minutes)), " total_sum_of_squares")
    return 1 - (
        sum_least_squares(alpha, beta, mean(daily_minutes))
        / total_sum_of_squares(mean(daily_minutes))
    )


print("\t" * 6, r_square(27.849969715324047, 0.05784373107207752), " r_square")


def r_r_square(alpha, beta):
    print(sum_least_squares(alpha, beta, mean(daily_minutes)), " sum_least_squares")
    print(total_sum_of_squares(mean(daily_minutes)), " total_sum_of_squares")
    return 1 - (
        sum_of_square_error(alpha, beta) / total_sum_of_squares(mean(daily_minutes))
    )


print("\t" * 6, r_r_square(27.849969715324047, 0.05784373107207752), " r_r_square")


def squared_error(alpha, beta, x_i, y_i):
    # for i, j in zip(num_friends_three, daily_minutes): return error(alpha, beta, i, j) ** 2
    return [
        error(alpha, beta, i, j) ** 2 for i, j in zip(num_friends_three, daily_minutes)
    ]


print(squared_error(0, 1, num_friends_three, daily_minutes), " squared_error")


# Квадратичная ошибка
def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    print(alpha, beta, " ***************************************")
    return error(alpha, beta, x_i, y_i) ** 2


# Градиент квадратичной ошибки
def squared_error_gradient(x_i, y_i, theta):

    alpha, beta = theta
    print(alpha, beta, " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return [-2 * error(alpha, beta, x_i, y_i), -2 * error(alpha, beta, x_i, y_i) * x_i]


# print ([squared_error_gradient(i, j, theta = [random.random(),
#                                               random.random()]) for i, j in zip(num_friends_three, daily_minutes)])

# random.seed(0)

theta = [random.random(), random.random()]

# alpha, beta = minimize_stohastic(squared_error, squared_error_gradient, num_friends_good,
#                                  daily_minutes_good, theta, 0.0001)

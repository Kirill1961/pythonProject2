import math as mt
import numpy as np
from scipy.stats import t
from scipy import stats


# d = {1: 65, 2: 72, 3: 81, 4: 88, 5: 65, 6: 72, 7: 76, 8: 88, 9: 92, 10: 7}
d = {1: 23, 2: 27, 3: 25, 4: 30, 5: 22, 6: 28, 7: 26, 8: 29, 9: 24, 10: 31,
      11: 20, 12: 32, 13: 28, 14: 26, 15: 30, 16: 21, 17: 27, 18: 29, 19: 25,
      20: 33, 21: 22, 22: 28, 23: 24, 24: 31, 25: 26, 26: 30, 27: 23, 28: 29,
      29: 32, 31: 21, 32: 27, 33: 26, 34: 30, 35: 24, 36: 28, 37: 22, 38: 31, 39: 25, 40: 29}

# sample 30%
# d = dict(list(d1.items())[0:14])

# Среднее
mean = sum([j for j in d.values()]) / len(d)
print(f"mean {mean}")

# Подсчёт частоты повторов
count = {}
for i in d.values():
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

# Мода
mode = [key for key, val in count.items() if val == max(count.values())]
print(f"mode {mode}")

# Дисперсия
var = sum((i - mean) ** 2 for i in d.values()) / (len(d) - 1)
print(f"variance {var:.2f}")

# Стандартное отклонение
sd = mt.sqrt(var)
print(f"sd {sd:.2f}")

# Стандартная ошибка среднего
se = sd / mt.sqrt(len(d))
print(f"se {se:.2f}")

# CI для n=39, по таблице коэффициент Стьюдента для уровня доверия 95% при n=39 -> t=2.0211
ci_below, ci_higher = mean - se * 2.2011, mean + se * 2.0211
print(f"ci {ci_below:.2f}, {ci_higher:.2f}")

# Нулевая Ho -> mu=28, Ha -> mu!= 28
# Калькулятор для Р-значения -> при t_score=-2.24 p=0.033
mu = 28
t_score = (mean - mu) / se
print(f"t_score {t_score:.2f} Уровень P-значимости = 0.033 < 0.05, предположение mu=28 статистически незначимо", "\n")




""" Анализ scipy.stats"""
# Данные
production_time = np.array([23, 27, 25, 30, 22, 28, 26, 29, 24, 31, 20, 32, 28, 26, 30, 21, 27, 29, 25, 33, 22, 28, 24, 31, 26, 30, 23, 29, 25, 32, 21, 27, 26, 30, 24, 28, 22, 31, 25, 29])

# Выборочное среднее
average_time = np.mean(production_time)

# Выборочная дисперсия
time_variance = np.var(production_time, ddof=1)

# 95%-й доверительный интервал для математического ожидания
# ddof=1 уменьшение степеней свободы
standard_bias = np.std(production_time, ddof=1) / np.sqrt(len(production_time))
confidence_interval = t.interval(0.95, len(production_time) - 1, average_time, standard_bias)

# t-тест
mu_0 = 28  # Предполагаемое среднее время. Вы можете проверить эту или другую гипотезу.
t_statistic, p_value = stats.ttest_1samp(production_time, mu_0)

# Вывод результатов
print(f"Выборочное среднее: {average_time}")
print(f"Выборочная дисперсия: {time_variance}")
print(f"95%-й доверительный интервал: {confidence_interval}")
print(f"t-статистика: {t_statistic}")
print(f"p-значение: {p_value}")
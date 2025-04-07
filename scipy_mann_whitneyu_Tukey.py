import numpy as np
from scipy.stats import mannwhitneyu
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

'''
Задача:
Предположим, у нас есть данные по результатам тестов двух групп студентов (группа A и группа B), 
и мы хотим понять, есть ли различие между ними. Мы применяем U-критерий Манна — Уитни 
для проверки гипотезы.
'''

# Данные для двух групп
group_a = [55, 63, 67, 59, 74, 69, 63, 71, 68, 67]
group_b = [83, 91, 85, 76, 92, 80, 89, 77, 91, 88]

# Применение теста Манна-Уитни
stat, p_value = mannwhitneyu(group_a, group_b)

print(f"U-статистика: {stat}")
print(f"P-значение: {p_value}")

# Интерпретация результатов
if p_value < 0.05:
    print("Есть статистически значимая разница между группами")
else:
    print("Нет статистически значимой разницы между группами")


# TODO Тьюки, Tukey's Honest Significant Difference (HSD) test.

# Примерные данные
data = pd.DataFrame({
    'value': [12, 13, 15, 10, 9, 8, 17, 18, 16],
    'group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C']
})

# Tukey HSD
tukey_result = pairwise_tukeyhsd(endog=data['value'],
                                 groups=data['group'],
                                 alpha=0.05)

print(tukey_result)


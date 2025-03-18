import csv
from ydata_profiling import ProfileReport
# from pandas_profiling import ProfileReport
import numpy as np
import pandas as pd
import scipy.stats as stats




print(pd.__version__)

# TODO Читаем файл heart.csv по указанному пути
puth = 'D:\Eduson_data\heart.csv'

# df = pd.read_csv(puth)
# print(df.head(5))


df = pd.DataFrame(
    np.random.rand(4, 3),
    columns=['a', 'b', 'c']
)

profile = ProfileReport(df, title='Pandas ProfileReport')
print(profile)


# TODO  Cramér's V измеряет силу зависимости, если она есть.
#  Хи-квадрат проверяет есть ли зависимость между двумя категориальными переменными.

# Таблица сопряжённости
table = pd.DataFrame({
    "First": [136, 80],
    "Second": [87, 97],
    "Third": [119, 372]
}, index=["Survived", "Not Survived"])

# Расчёт хи-квадрат
chi2, p, dof, expected = stats.chi2_contingency(table)

# Расчёт Cramér's V
n = table.to_numpy().sum()
k = min(table.shape)
cramers_v = np.sqrt(chi2 / (n * (k - 1)))

print(f"Хи-квадрат p-value: {p:.4f}")
print(f"Cramér's V: {cramers_v:.4f}")

import numpy as np
import pandas as pd

print(' Создание data')

data = ['Pan,', 12, 'matpl']
s = pd.Series(data)
print(' data', s)

# Присваивание индексов
print(' Присваивание индексов')
s = pd.Series([2, 'ok', -3, 0.5], index=['a', 'b', 'c', 'd'])
print(s)


# Рандомный генератор с присваиванием индексов
print(' Рандомный генератор с присваиванием индексов')
s = pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd'])
print(s)


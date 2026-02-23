import numpy as np

# TODO выборки из параметризованного биномиального распределения,
#  где каждая выборка равна числу успехов в n попытках.
#  n - где это количество испытаний, p - вероятность успеха
print('binomial :\n', np.random.binomial(10, 0.1, 5), '\n')

# TODO Генерирует случайную выборку из заданного одномерного массива
#  a - диапазон из которого берутся случайные числа, эквивалент np.arange(a)
#  p - Вероятности, связанные с каждой записью в "a", общая сумма вероятностей равна 1
print('choice :\n', np.random.choice(7, 3, p=[0.1, 0, 0.3, 0.2, 0.1, 0.1, 0.2]), '\n')

# TODO Случайная выборка заданного размера от 0 до 1
print('random_sample :\n', np.random.random_sample(10), '\n')

# TODO Выборка из нормального распределения
print('normal :\n', np.random.normal(0, 1, size=10), '\n')

# TODO генерирует случайные числа на интервале [low, high) из равномерного распределения
print('uniform :\n', np.random.uniform(1, 10, size=10), '\n')

# TODO linspace делит заданный набор чисел на заданное кол-во интервалов
#  start, stop - границы набора чисел
#  num - кол-во интервалов
print('linspace :\n', np.linspace(1, 10, 4), '\n')


# TODO  Уникальные значения numpy
np.random.seed(0)
b = np.array(list(np.random.randint(1, 10, size=12))).reshape(3, 4)
print('Исходный array : \n', b, '\n')
print('Уникальные значения : \n', np.unique(b, return_counts=True), '\n')

print('Версия numpy : ', np.__version__)
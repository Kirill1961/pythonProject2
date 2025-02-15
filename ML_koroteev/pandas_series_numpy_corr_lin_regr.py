import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


print(" Создание data")

data = ["Pan,", 12, "matpl"]
s = pd.Series(data)
print(" data", s)

# Присваивание индексов
print(" Присваивание индексов")
s = pd.Series([2, "ok", -3, 0.5], index=["a", "b", "c", "d"])
print(s, " Присваивание индексов")

# Рандомный генератор с присваиванием индексов
print(" Рандомный генератор с присваиванием индексов")
s = pd.Series(np.random.randn(4), index=["a", "b", "c", "d"])
print(s)

""" Читаем файл  csv, добавляем заголовки, выводим с заголовками"""
data_1 = pd.read_csv("data_base_1.csv")  # прочитали файл без заголовков
data_1.to_csv(
    "data_base_1_new.csv",
    header=[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
    ],
    index=False,
)  # добавили заголовки и создали новый файл

data_1 = pd.read_csv("data_base_1_new.csv")  # прочитали новый файл с заголовками

data_3 = pd.DataFrame(data_1)  # передали "data_base_1_new.csv" в DataFrame

# Настройка отображения
pd.set_option("display.max_columns", None)  # Показывать все столбцы
pd.set_option("display.width", 1000)  # Установить ширину вывода
pd.set_option("display.max_colwidth", None)  # Установить максимальную ширину столбца

print(data_3.head())  # вывод файла с заголовками
# Полное описание данных
print(data_3.describe(), "describe")
print(data_3.info())

"""axis pandas и numpy, 
axis=1 для удаления проходим индексы столбов, для sum() проходим значения строк
axis=0 наоборот"""
# DataFrame - это словарь, где ключ имя признаков/столбов, величина - признаки
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})

# Сумма по строкам

print(df, "в DataFrame передаём заголовок + строка, вывод заголовок + столбец ")

# Вырезаем строку и сохраняем в переменную d, вывод удалённый столбец
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
d = df.drop("A", axis=1)
print(d, "Удаляем строку, вывод без удалённого  столба")


# Линейная регрессия, корреляция, Транспонирование DataFrame
# Создание DataFrame
# d = {i: [x, y, z] for i, x, y, z in zip(["Алиса", "Боб", "Клара", "Дэвид", "Эмма", "Феликс"],
#                                         [85, 78, 90, 88, 82, 95],
#                                         [90, 82, 92, 86, 80, 9],
#                                         [10, 8, 12, 11, 9, 13])}

d = {i: [x, y, z] for i, x, y, z in zip(["Алиса", "Боб", "Клара", "Дэвид", "Эмма", "Феликс"],
                                        [15, 18, 10, 18, 12, 15],
                                        [0, 2, 2, 6, 0, 9],
                                        [10, 8, 12, 11, 9, 13])}


# Индексы / Имена строк
labels = ["make", "prog", "time"]
data = pd.DataFrame(d, index=labels)
print(data)

# 1. Транспонирование DataFrame
data_transposed = data.T
print("Транспонированный DataFrame:")
print(data_transposed)

# 2. Корреляция между 'make' и 'prog'
correlation = data.loc['make'].corr(data.loc['prog'])  # loc - доступ к группе строк или столбов
print(f"\nКорреляция между 'make' и 'prog': {correlation}")

# Выделяем предикторы и целевую переменную ДАТАСРЕЗОМ, получаем 2х мерные массивы
X = np.array(data.loc['make']).reshape(-1, 1)
y = np.array(data.loc['prog'])

print(data.loc["make":"time", "Алиса"], "\n")  # Значения в строке/индексе/объекте Алиса в столбцах от "make" до "time"
print(data_transposed.loc["Боб":"Эмма", "time"], "\n")  # все значения time от Боб до Эмма


# 3. Линейная регрессия между 'make' и 'prog'
model = LinearRegression().fit(X, y)
print(f"\nКоэффициент наклона: {model.coef_[0]}")
print(f"Перехват (intercept): {model.intercept_}", '>>>>>')

# Предсказываем Целевую
y_predict = model.predict(X)
print(f'Предсказываем Целевую: {y_predict}')

# Множественная регрессии

# Данные
data = {
    'make': [85, 78, 90, 88, 82, 95],
    'prog': [90, 82, 92, 86, 80, 9],
    'time': [10, 8, 12, 11, 9, 13]
}

df = pd.DataFrame(data)

# Независимая переменная
X = df[['time']]

# Добавляем константу (перехват)
X = sm.add_constant(X)

# Зависимые переменные (make и prog)
y_make = df['make']
y_prog = df['prog']

# Линейная регрессия для make
model_make = sm.OLS(y_make, X).fit()

# Линейная регрессия для prog
model_prog = sm.OLS(y_prog, X).fit()

# Вывод результатов
print('Регрессия для make:')
print(model_make.summary())

print('\nРегрессия для prog:')
print(model_prog.summary())

# PDF
# kde сгладила гистограмму
kde = gaussian_kde(data["make"])
min_max = np.linspace(min(data["make"]), max(data["make"]), 20)
# на основе kde строим  pdf
pdf = kde.pdf(min_max)
plt.hist(data["make"], bins=10, density=True, alpha=0.5, label='Histogram')
# plt.plot(min_max, pdf)
# plt.show()


# KDE
# Данные для сетки
data_kde = np.random.normal(loc=15, scale=30, size=100)
# предали выборку в класс gaussian_kde
kde_key = gaussian_kde(data["time"])
# Задаём шкалу для kde графика
scale_rang = np.linspace(-5, 20, 100)
# Считаем плотность
density = kde_key(scale_rang)
# Строим гистограмму
plt.hist(data_kde, bins=8, density=True)
# plt.plot(scale_rang, density)
# plt.show()


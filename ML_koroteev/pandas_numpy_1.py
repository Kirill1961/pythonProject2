import numpy as np
import pandas as pd

print(" Создание data")

data = ["Pan,", 12, "matpl"]
s = pd.Series(data)
print(" data", s)

# Присваивание индексов
print(" Присваивание индексов")
s = pd.Series([2, "ok", -3, 0.5], index=["a", "b", "c", "d"])
print(s)


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


# Удаляем строку, вывод удалённый столбец
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
d = df.drop("A", axis=1)
print(d, "Удаляем строку, вывод без удалённого  столба")

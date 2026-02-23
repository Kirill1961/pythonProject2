import pandas as pd

num = 42
str_num = ("{}".format(num), ' def')
print(str_num)
print(type(str_num))

""" _______________________________f - строка"""
num = 77
string_num = (f"{num}" + 'abc')
print(string_num)
print(type(string_num))

set = {i for i in range(10)}
print(set)

""" _____________________________f - строка"""
set2 = {(f'{k}', 'FormaT' ) for k in set}
print(set2)

price = 46.99
tag = 'is a real bargain'

""" ___________________Кокотенация, с помощью " + " соединяем строчные символы"""

mag = 'AT' + str(price) + ',' +  tag + '-' + 'good programmer'
print(mag)

"""форматировочная строка .2f используется для форматирования числовых значений с плавающей точкой (float) """
accuracy = 0.75321
print(f"Accuracy: {accuracy:.2f}")  # .2 количество знаков после десятичной точки, f указывает на форматирование
# числа как значения с плавающей точкой


str = "Name {}, Old {}, weigh {}"
name = "Kirill"
old = "51"
weigh = "80"
res = str.format(name, old, weigh)
print(res, " -> Фу-ция format")
str_ = "Name {0}, Old {1}, weigh {2}"
print(str_.format(name, old, weigh), " -> Тоже самое с индексами")

# варианты использования формат
print(" Это число : {0:.2f}".format(2.7418241824), "варианты использования формат")
print(" Это число : {1:.2f}".format(2.7418241824, 3.1487962), "варианты использования формат")

# Использование Табуляции {i:15} — это способ выровнять текст в столбцах для лучшей читаемости.
data = {'col1': ['1', '2', '3'], 'col2': ['4.5', '5.5', '6.5', '7.5']}
for i in data:
    print(f"key {i:15} : vale {data.get(i)} - {i:15}", "\n")

# Использование Табуляции {i:15} для вывода читаемого dataframe
df = {i: j for i, j in zip(["big_column", "col", "column"], ([1, 2, 3], [10, 20, 30], ["qwert", "as", "zxc"]))}
df = pd.DataFrame(df)

print("Без Использования Табуляции{i:15} :", "\n")
for i in df.columns:
    colum_type = df[i].dtype
    print(f"Столбец {i} тип {colum_type}")


print("С Использованием Табуляции {i:15}:", "\n")
for i in df.columns:
    colum_type = df[i].dtype
    print(f"Столбец {i:15} тип {colum_type}")


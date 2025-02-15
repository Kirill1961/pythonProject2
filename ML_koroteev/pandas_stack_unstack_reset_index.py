import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt










df = pd.DataFrame({
    "A": [1, 2, pd.NA],
    "B": [4, None, pd.NA],
    "C": [7, 8, 9]
})
df1 = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})
df2 = pd.DataFrame({"A": ["yes", "no", "no"], "B": [10, "20" , "30"], "C": ["0", 0, 1]})
df3 = pd.DataFrame({"A": [2, 2, 3, 2, 3], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})
df33 = pd.DataFrame({"A": ["F", "F", "W","F", "W"], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})
df4 = pd.DataFrame({"A": [5, 2, 2, 4, 5], "B": [50, 20, 50, 40, 50], "C": [300, 300, 300, 400, 300]})
df5 = pd.DataFrame({"A": [50, 20, 2, 4, 5], "B": [50, 20, 300, 40, 5], "C": [50, 300, 300, 400, 5]})
df55 = pd.DataFrame({"A": ["F", "F", "G", "G", "W"], "B": [20, 20, 300, 20, 5], "C": [5, 300, 300, 400, 5]})
df333 = pd.DataFrame({"A": ["F", "F", "W","F", "W"],
                      "B": [20, 20, 30, 40, 50],
                      "C": [300, 200, 300, 300, 500]})
df7 = pd.DataFrame({
    'Age': [23, 45, 31, 22, 34, 40, 50, 28, 33, 42, 38, 25],
    'Sex': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female',
            'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
})
df77 = pd.DataFrame({
    'A': [1, 9, 5, 5, 2, 6, 2, 3, 10, 6, 7, 1, 9, 2],
    'B': [11, 6, 8, 10, 15, 11, 8, 8, 12, 7, 50, 50, 50, 50]
})
df777 = pd.DataFrame({
    'A': [34, 44, 40, 20, 32, 32, 49, 44, 34, 30, 45, 48, 36, 38, 47, 27, 24, 28, 25, 46],
    'B': ['M', 'F', 'F', 'F', 'M', 'F', 'F', 'F', 'F', 'M', 'M', 'M', 'M', 'F', 'F', 'F', 'M', 'M', 'F', 'F']
})

df7777 = pd.DataFrame({
    'A': [34, 44, 40, 20, 32, 32, 49, 44, 34, 30, 45, 48, 36, 38, 47, 27, 24, 28, 25, 46],
    'B': ['M', 'W', 'W', 'F', 'M', 'F', 'W', 'F', 'W', 'M', 'M', 'S', 'S', 'F', 'F', 'F', 'M', 'M', 'F', 'S']
})


df44 = pd.DataFrame({"A": [5, 2, 2, 4, 5],
                     "B": [50, 20, 50, 40, 50],
                     "C": [300, 300, 300, 400, 300]},
                    index=["Avrg", "Bin", "Cnt", "Foo", "Dt"]
                    )

df22 = pd.DataFrame({"A": [0, "no", "no"], "B": [0, 0 , 0], "C": [0, 0, 1]})


df11 = pd.DataFrame({
    "A": [2, 2, 3, 2, 3],
    "B": [10, 20, pd.NA, 40, 50],
    "C": [pd.NA, 200, 300, 400, pd.NA]
})


# Долевое распределение столбцов А и В
grouped = df333.groupby(["A", "B"]).size()
percent = grouped.groupby(level=0).apply(lambda x: x * 100 / float(x.sum()))
print(grouped)
print(percent)

#  one-hot encoding
encod_categor = pd.get_dummies(df333, columns=["A"])  # Выйдет False и True
encod_zero_one = encod_categor.astype(int)  # Преобразование False и True в 0 и 1
print(encod_categor)
print(encod_zero_one)


# Сравнение Индекса Группировки и Средного
mean_a = df11.groupby(['A']).mean()
print(mean_a)
df11_cop = df11.copy()
for col in df11.columns[1:]:
    df11_cop['NEW'+'_' + col] = df11[col] != df11['A'].map(mean_a[col])
    print(df11_cop)


# Столбикова Частотная Диаграмма без hue='B' все столбцы подписаны
ax = sns.countplot(x='B', data=df7777)
ax.bar_label(ax.containers[0])
# plt.show()


# Столбикова Частотная Диаграмма с hue='B', используем итерацию для подписи столбов
ax = sns.countplot(x='B', hue='B', data=df7777)
for contain in ax.containers:
    ax.bar_label(contain)
# plt.show()


# Вывод DF со строками фильтрованных по заданному значению в нужной колонке
print(df777[df777['B'] == 'F'])


# Указываем просто индекс'Bin' -> Возвращает строку по индексу
print(df44.xs('Bin'))

__doc__ = ''' x s ( ) аналог loc  Используется для извлечения данных из Индекса или Мультииндекса'''
# DF с МультиИндексом
d_multi_index = df44.groupby(['A', 'B']).count()

print(d_multi_index)

# Указываем просто Индекс из МультиИндекса
print(d_multi_index.xs(4))

# Указываем уровень МультиИндекса и Индекс
print(d_multi_index.xs(key=50, level=1))
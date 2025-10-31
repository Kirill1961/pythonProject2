import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from scipy.stats import f
import random
from sklearn.preprocessing import OrdinalEncoder


df = pd.DataFrame({
    "A": [1, 2, pd.NA],
    "B": [4, None, pd.NA],
    "C": [7, np.nan, 9]
})
df1 = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})
df2 = pd.DataFrame({"A": ["yes", "no", "no"], "B": [10, "20", "30"], "C": ["0", 0, 1]})
df3 = pd.DataFrame({"A": [2, 2, 3, 2, 3], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})
df33 = pd.DataFrame({"A": ["F", "F", "W", "F", "W"], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})
df4 = pd.DataFrame({"A": [5, 2, 2, 4, 5], "B": [50, 20, 50, 40, 50], "C": [300, 300, 300, 400, 300]})
df5 = pd.DataFrame({"A": [50, 20, 2, 4, 5], "B": [50, 20, 300, 40, 5], "C": [50, 300, 300, 400, 5]})
df55 = pd.DataFrame({"A": ["F", "F", "G", "G", "W"], "B": [20, 20, 300, 20, 5], "C": [5, 300, 300, 400, 5]})
df555 = pd.DataFrame({"A": ["F", "F", "G", "F", "W"],
                      "B": [20, 20, 300, 20, 5],
                      "C": [5, 5, 300, 5, 5]})
df333 = pd.DataFrame({"A": ["F", "F", "W", "F", "W"],
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

df707 = pd.DataFrame({
    'A': [1, 9, 5, 5, 2, 6, 2, 3, 10, 6, 7, 1, 9, 2],
    'B': pd.Series(list('QAWSEDRFTGYHUK'))
})

df70 = pd.DataFrame({
    'A': [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40],
    'B': ['M', 'W', 'F', 'V', 'M', 'F', 'F', 'D', 'F', 'M', 'M', 'M', 'M', 'F', 'F', 'F', 'M', 'M', 'F', 'F']
})

df44 = pd.DataFrame({"A": [5, 2, 2, 4, 5],
                     "B": [50, 20, 50, 40, 50],
                     "C": [300, 300, 300, 400, 300]},
                    index=["Dt", "Bin", "Foo", "Cnt", "Avrg"]
                    )
df404 = pd.DataFrame({"A": [5, 2, 2, 4, 5],
                      "B": [50, 20, 50, 40, 50],
                      "C": [300, 300, 300, 400, 300]},
                     index=["AA", "Bin", "CC", "Foo", "Dt"])

df22 = pd.DataFrame({"A": [0, "no", "no"], "B": [0, 0, 0], "C": [0, 0, 1]})

df111 = pd.DataFrame({
    "A": ["Avrg", "Bin", "Cnt", "Foo", "Dt"],
    "B": ['M', 'F', 'F', 'F', 'M'],
    "C": ['Male', 'Female', 'Male', 'Female', 'Male']
})

df11 = pd.DataFrame({
    "A": [2, 2, 3, 2, 3],
    "B": [10, 20, pd.NA, 40, 50],
    "C": [pd.NA, 200, 300, 400, pd.NA]
})

# Долевое распределение столбцов А и В
grouped = df333.groupby(["A", "B"]).size()
percent = grouped.groupby(level=0).apply(lambda x: x * 100 / float(x.sum()))
print('Группировка : \n', grouped)
print('Группировка в процентах : \n', percent)

#  one-hot encoding
encod_categor = pd.get_dummies(df333, columns=["A"])  # Выйдет False и True
encod_zero_one = encod_categor.astype(int)  # Преобразование False и True в 0 и 1
print('one-hot encoding : \n', encod_categor)
print('encod_zero_one :  \n', encod_zero_one)

# Сравнение Индекса Группировки и Средного
mean_a = df11.groupby(['A']).mean()
print(mean_a)
df11_cop = df11
for col in df11.columns[1:]:
    df11_cop['NEW' + '_' + col] = df11[col] != df11['A'].map(mean_a[col])
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


# TODO Фильтруем весь df777, выводим строки df777 заданному значению в колонке 'B'
print(df777[df777['B'] == 'F'], 'Вывод DF со строками фильтрованных по заданному значению в нужной колонке')

# TODO Выводим строки/значения столбца 'B' по заданному значению в колонке 'А'
print(df11['B'][df11['A'] == 3], 'значения столбца B по заданному значению в колонке A')

# Указываем просто индекс'Bin' -> Возвращает строку по индексу
print(df44.xs('Bin'))

# TODO ''' x s ( ) аналог loc  Используется для извлечения данных из Индекса или Мультииндекса'''
# DF с МультиИндексом
d_multi_index = df44.groupby(['A', 'B']).count()

print(d_multi_index)

# Указываем просто Индекс из МультиИндекса
print(d_multi_index.xs(4))

# Указываем уровень МультиИндекса и Индекс
print(d_multi_index.xs(key=50, level=1))

# TODO Датасрез
print(f"Датасрез df777 : {df777[(df777['A'] > 30) & (df777['A'] < 40)]}")

# TODO percentile quantile
print(f"percentile 25%, 75% : {np.percentile(df777['A'], [25, 75])}")
print(f"quantile 25%, 75% : {np.quantile(df777['A'], [0.25, 0.75])}")

# TODO ▶ Отбор по заданной частоте повторов значений в заданном столбце
df44_counts = (df44.value_counts() > 1).reset_index()
res = (df44_counts.loc[df44_counts['count'] == True, 'A'])
# print(res)
print(f'Значение столбца А : {res.values} повторяются больше одного раза ')

# TODO Это не просто конкатенация, а создание нового столбца в DataFrame путём объединения
#  (через сложение или любую другую операцию) данных из уже существующих столбцов
#  Например:
#  df['sum'] = df['math'] + df['science']        # числовая сумма
#  df['flag'] = df['passed'] & df['attended']    # логическая операция
#  df['age_group'] = df['age'].astype(str) + ' лет'  # строка + число
#  df['combo'] = df['city'] + ', ' + df['country']   # строка + строка.

df7['new_column'] = df7.Sex + ' ' + '/' + ' ' + df7.Age.astype(str)
print(df7)

# TODO p-value от F вручную
#  F_value — это значение F-статистики, которое мы получаем при проведении F-теста

F_value = 0.1
p_value = 1 - f.cdf(F_value, df1.A, df1.B)
print(p_value)

# TODO Выявление, Удаление и Просмотр дубликатов Дубликатов
dubl_quantity = df555.duplicated().sum()
print(f'Выявление дубликатов : {dubl_quantity} duplicates', '\n')
dubl_viewing = df555[df555.duplicated()]
print(f'Просмотр дубликатов{dubl_viewing}', '\n')
dubl_drop = df555.drop_duplicates()
print(f'Удаление дубликатов{dubl_drop}', '\n')

# TODO Метод .squeeze() преобразует:
#  * DataFrame с одной колонкой → в Series
#  * DataFrame с одной строкой и одной колонкой → в скаляр


df_one = pd.DataFrame({'Age': [25, 30, 35]})

# Выборка как DataFrame
df_onecol = df_one[['Age']]  # <-- DataFrame
print(type(df_onecol))  # <class 'pandas.core.frame.DataFrame'>

# Преобразуем в Series
s = df_onecol.squeeze()
print(type(s), '\n')  # <class 'pandas.core.series.Series'>

# TODO Итерация Одного Группированного cat_feat
for name, data in df7.groupby('Sex'):
    print(name, '\n')

# TODO Итерация Двух и более Группированных cat_feat
df_7 = pd.DataFrame({
    'Test': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No'],
    'Age': [23, 45, 45, 23, 45, 23, 23, 45, 45, 23, 45, 25],
    'Sex': ['Male', 'Female', 'Male', 'Female', 'Female', 'Female',
            'Male', 'Female', 'Male', 'Female', 'Female', 'Female']
})

for name, data in df_7.groupby((['Sex', 'Age', 'Test'])):
    print(name)  # Имена сгруппированных данных

    # print(data, '\n')  # Все группы после группировки

# TODO Центрирование в ручную, вычитание среднего из значений колонок
df77_scaler = df77 - (df77.A.mean(), df77.B.mean())
print('Центрирование в ручную, вычитание среднего из значений колонок', '\n', f'{df77_scaler[:5]}')

# TODO Создание через list - index и columns в DF
df_list = pd.DataFrame([[1, 2], [10, 20], [100, 200]], columns=[list('AB')], index=list('abc'))

print('\n', 'Создание через list - index и columns в DF :', '\n', f'{df_list}')

# TODO Eduson Попарное сложение признаков
df = pd.DataFrame([['a', 'b', 'e', 'v'], ['c', 'd', 'f', 'w']], columns=list('ABCD'))
col = df.columns
for n in range(len(col)):
    for m in range(n + 1, len(col)):
        col1, col2 = col[n], col[m]
        df[f'{col1 + col2}'] = df[col1] + df[col2]
print(df, '\n')

# TODO MY Попарное сложение признаков
df = pd.DataFrame([['a', 'b', 'e', 'v'], ['c', 'd', 'f', 'w']], columns=list('ABCD'))
cols = df.columns
for idx in range(len(cols)):
    for col_next in cols[idx + 1:]:
        df[cols[idx] + col_next] = df[cols[idx]] + df[col_next]
print(df, '\n')

# TODO reindex(для Series) + reindex_like(для DF)
print('reindex : \n', df44.reindex(df404.index), '\n')
print('reindex_like : \n', df44.reindex_like(df404), '\n')

# TODO pd.date_range - колленкция дат в заданном интервале
#  * здесь используется как index
index = pd.date_range(start='2014-02-12', end='2014-02-15', freq='D')
print('Индексы даты :\n', pd.DataFrame({'One': list(range(1, 5)), 'Two': list(range(10, 50, 10))}, index=index), '\n')

print('Сгенерирванные даты с шагом Месяц :\n', pd.date_range(start='2014-02-12', end='2014-07-12', freq='M'), '\n')

# TODO Создание DF
#  из списка
#  из Series
#  из ndarray

a = np.array(list('gud'))

print(pd.DataFrame([a], index=['Kirill'], columns=list('ABC')), '\n')

s = pd.Series(list('very'))

print(pd.DataFrame([s.values], index=['He'], columns=list('ABCD')), '\n')

ls = list('pops')
f
print(pd.DataFrame([ls], index=['Here'], columns=list('ABCD')), '\n')

# TODO OrdinalEncoder
df = pd.DataFrame(
    {'A': ['asdf'[random.randint(0, 3)] for _ in range(5)],
     'B': ['qwer'[random.randint(0, 3)] for _ in range(5)]
     }
)

enc = OrdinalEncoder()

print('OrdinalEncoder для DataFrame :\n', enc.fit_transform(df), '\n')
print('OrdinalEncoder для Series через array :\n', enc.fit_transform(np.array(df.A).reshape(-1, 1)), '\n')
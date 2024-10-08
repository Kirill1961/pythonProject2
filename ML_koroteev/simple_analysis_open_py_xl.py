import pandas as pd
import openpyxl
import glob
import matplotlib.pyplot as plt
import os
import re



print(os.getcwd(), " Р а с п о л о ж е н и е данного файла ", "\n")
path = r"D:\downloads\SPAM Assassian\data_koroteev\data3.xlsx"
# path = r"D:\downloads\price_cena4_2024-03-28.xlsx"

print(os.path.exists(path))  # Проверить, существует ли файл по этому пути

files = glob.glob(path)
print(files)

pd.set_option("display.max_columns", None) # Показывать все столбцы
pd.set_option("display.width", 1000)  # Установить ширину вывода

# Открытие файла Excel
wb = openpyxl.load_workbook(files[0])

# Выбор активного листа
sheet = wb.active

# Чтение значения из определённой ячейки (например, A1)
value = sheet['A10'].value
print(value, "\n")

# Чтение файла Excel
tabl = pd.read_excel(files[0], engine='openpyxl', skiprows=2)
df = pd.DataFrame(tabl)

# количество строк и столбцов, ненулевых значений, объем памяти, используемый вашим DataFrame.
info = df.info()
print(info)

# Вывести имена всех колонок
print(df.columns, "\n")
print(df.keys(), ">>", "\n")
print(df.head())

#TODO initial data

# Извлечение столбцов по именам
column_scores = df['Балл']
failed_score = df['Минимальный балл'][0]
sex = df['Пол']
num_school = df["№ школы"]
task_brief = df["Задания с кратким ответом"]
task_expand = df["Задания с развёрнутым ответом"]


# Извлечение столбца по индексу (нумерация начинается с 0)
# column_data_ind = df.iloc[:, 9]

#  Статистики колонки 'Балл'
print(column_scores.describe(), "\n")


" Задача 2 "
# Статистики всего DataFrame
print(df.describe().head(8), "\n")

# средний балл 52
mean_score = column_scores.mean()

# объект Series, возвращает bool
scores_below_average = pd.Series(column_scores) < mean_score

# размер выборки до 52 баллов
below_average = len(column_scores[column_scores < 52])

# размер выборки total
total_score = len(column_scores)

"Задача 3"
# % учащихся до среднего балла
fraction_below_average = below_average / total_score
print(f"% учащихся ниже среднего среднего балла: {fraction_below_average*100:.2f}")

"Задача 4"
# % учащихся не сдавших экзамен
failed_exam = (column_scores < int(failed_score) ).mean()*100
print(f"% учащихся не сдавших экзамен: {failed_exam:.2f}", "\n")

"Задача 5"
# % учащихся сдавших экзамен
passed_exam = 100 - failed_exam
print(f"% passed exam {passed_exam:.2f}", "\n")

# Создаём DataFrame с двумя значениями x-сдавшие и y-не сдавшие
data = {'Values': [92.29, 7.71]}

# Разметка значений 'Values'
df_chart = pd.DataFrame(data, index=['passed_exam', 'failed_exam'])

# Строим круговую диаграмму
df_chart.plot.pie(y='Values', labels=df_chart.index, autopct='%1.1f%%', startangle=90)

# Отображаем диаграмму
plt.ylabel('')  # Убираем название оси для чистого отображения
# plt.show()

"Task 6"
# KDE распределения баллов
column_scores.plot.kde()
# plt.show()

"Task 7"
# % соотношения «отлично», «хорошо», «удовлетворительно», «неудовлетворительно»

one_percent = (100 / total_score)
excellent = len(column_scores[column_scores >= 35]) * one_percent
bad = len(column_scores[column_scores <= 10]) * one_percent
middle = (len(column_scores[column_scores <= 22]) - bad ) * one_percent
good = (len(column_scores[column_scores <= 34]) - middle - bad) * one_percent

print(f"отлично {excellent:.2f}%, хорошо {good:.2f}%, удовлетворительно {middle:.2f}%, плохо  {bad:.2f}%")

"Task 8"
# % ratio male and female

# Разные способы подсчёта уникальных символов "М" и "Ж"
# считаем количество unic через True = 1
male = sum(sex.values == "М")
# считаем количество unic М и Ж
people_sex = sex.value_counts()
people_sex_percent = sex.value_counts(normalize=True)

print(f"man {male}")
print(f"{people_sex}")
print(f"{people_sex_percent}")

"Task 9"
# Сколько школ принимало участия в экзаменах

# dropna() - Удаление nan из колонки
num_school = num_school.dropna()

# Множеством оставляем уникальные номера школ для подсчёта
total_school = len(set(num_school))
print(f"количество школ учавствующих в экзаменах {total_school}")

"Task 10"
# Сколько всего заданий с кратким ответом? С развернутым ответом?

# replace - по шаблону удаляем символ "(3)", ! ставить экран обеих скобок "\( \)"
df_clean = task_expand.str.replace(r"\(3\)", "", regex=True)

# extractall - извлекаем все цифры из очищенных строк
task_expand_total = df_clean.str.extractall(r"(\d)")

# тк символ в очищенной строке это одна задача, то число символов = числу задач
num_tasks = len(task_expand_total)
print(f"число задач С развернутым ответом {num_tasks}")


# value_counts - счёт количества уникальных символов
task_expand_total_count = task_expand_total.value_counts(ascending=True)
print(f"число решённых заданий с развёрнутым ответом: \n{task_expand_total_count}")


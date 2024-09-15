import pandas as pd
import openpyxl
import glob
import matplotlib.pyplot as plt
import os



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

# Извлечение столбцов по именам
column_scores = df['Балл']
failed_score = df['Минимальный балл'][0]


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
print(passed_exam, "\n")

# Создаём DataFrame с двумя значениями x и y
data = {'Values': [92.29, 7.71]}

# Разметка значений 'Values'
df_chart = pd.DataFrame(data, index=['passed_exam', 'failed_exam'])

# Строим круговую диаграмму
df_chart.plot.pie(y='Values', labels=df_chart.index, autopct='%1.1f%%', startangle=90)

# Отображаем диаграмму
plt.ylabel('')  # Убираем название оси для чистого отображения
# plt.show()


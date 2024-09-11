import pandas as pd
import openpyxl
import glob

path = r"D:\downloads\SPAM Assassian\data_koroteev\*"
# path = r"D:\downloads\price_cena4_2024-03-28.xlsx"

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
print(value)

# Чтение файла Excel
tabl = pd.read_excel(files[0], engine='openpyxl')
df = pd.DataFrame(tabl)

# Вывести имена всех колонок
print(df.columns)

# Извлечение столбцов по именам
column_scores = df['Балл']
failed_score = df['Минимальный балл'][0]


# Извлечение столбца по индексу (нумерация начинается с 0)
# column_data_ind = df.iloc[:, 9]

# Статистики всего DataFrame
print(df.describe())

#  Статистики колонки
print(column_scores.describe())  # Статистики total


""" Задание """
# средний балл 52
mean_score = column_scores.mean()

# объект Series, возвращает bool
scores_below_average = pd.Series(column_scores) < mean_score

# размер выборки до 52 баллов
below_average = len(column_scores[column_scores < 52])

# размер выборки total
total_score = len(column_scores)

# % учащихся до среднего балла
fraction_below_average = below_average / total_score
print(f"% учащихся ниже среднего среднего балла: {fraction_below_average*100:.2f}")

# % учащихся не сдавших экзамен
failed = (column_scores < int(failed_score) ).mean()*100
print(f"% учащихся не сдавших экзамен: {failed:.2f}")
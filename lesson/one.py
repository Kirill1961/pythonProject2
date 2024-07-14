import glob, re
import runpy
import subprocess


""" перевод числа в строку,2й аргумент это
основание системы счисления, 16 это :
0123456789abcdef, """

print(int('4aa', 16))

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ]

result = [elem for elem in a if elem in b]

resultt = set(a).intersection(set(b))

resulttt = list(set(a) & set(b))

print(result, resultt, resulttt)

c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ress = [item for item in c if item < 5]
print(ress)

path = r"C:\Users\Kirill\PycharmProjects\pythonProject2\a_ae.py"
print(glob.glob(path), "|||||")

path = r"C:\Users\Kirill\PycharmProjects\pythonProject2\a_ae.py"
files = glob.glob(path)

print(files, "*******")

# Указываем путь к файлу
path = r"C:\Users\Kirill\PycharmProjects\pythonProject2\a_ae.py"

# Находим файл
files = glob.glob(path)

# Проверяем, что файл найден
if files:
    file_path = files[0]  # Получаем путь к первому найденному файлу

    # Открываем файл и читаем его содержимое
    with open(file_path, 'r') as file:
        content = file.read()
        print(content, ">>>>>>>>>>>>>")
else:
    print("Файл не найден.")


# Указываем путь к файлу
path = r"C:\Users\Kirill\PycharmProjects\pythonProject2\a_ae.py"

# Читаем содержимое файла
with open(path, 'r') as file:
    code = file.read()

# Выполняем код
exec(code)




# Указываем путь к файлу
path = r"C:\Users\Kirill\PycharmProjects\pythonProject2\a_ae.py"

# Выполняем код в файле
runpy.run_path(path)

# Добавляем путь к директории, содержащей файл
sys.path.append(r"C:\Users\Kirill\PycharmProjects\pythonProject2")

# Импортируем модуль (имя файла без расширения .py)
import file

# Вызываем функции или используем переменные из модуля
file.some_function()




# Указываем путь к файлу
path = r"C:\Users\Kirill\PycharmProjects\pythonProject2\a_ae.py"

# Выполняем файл
result = subprocess.run(['python', path], capture_output=True, text=True)

# Выводим результат
print(result.stdout)
print(result.stderr)

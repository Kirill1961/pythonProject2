import glob
import os.path
import runpy
import subprocess
import sys
from logg import log_uru


path = r"/simple_analysis_open_py_xl.py"
print(glob.glob(path), "|||||")

path = r"/simple_analysis_open_py_xl.py"
files = glob.glob(path)

print(files, "*******")

# Указываем путь к файлу
path = r"/simple_analysis_open_py_xl.py"

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
path = r"/simple_analysis_open_py_xl.py"

# Читаем содержимое файла
with open(path, 'r') as file:
    code = file.read()

# Выполняем код
print(exec(code), "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")




# Указываем путь к файлу
path = r"/simple_analysis_open_py_xl.py"

# Выполняем код в файле
runpy.run_path(path)

# Добавляем путь к директории, содержащей файл
sys.path.append(r"C:\Users\Kirill\PycharmProjects\pythonProject2")

# Импортируем модуль (имя файла без расширения .py)
from ML_koroteev import simple_analysis_open_py_xl

# Вызываем функции или используем переменные из модуля
koroteev_open_py_xl.ou(2)




# Указываем путь к файлу
path = r"/simple_analysis_open_py_xl.py"

# Выполняем файл
result = subprocess.run(['python', path], capture_output=True, text=True)

# Выводим результат
print(result.stdout)
print(result.stderr)


path_1 = r"C:\Users\Kirill\PycharmProjects\pythonProject2\logg\log_uru.py"

sys.path.append(os.path.join(os.getcwd(), "logg", "m"))

print(sys.path)

log_uru.m()

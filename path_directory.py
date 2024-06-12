from pathlib import Path
import glob
import os
import fnmatch


# Функция для поиска файлов с нужным расширением
def find_files(directory, extension):
    pattern = f'{directory}/**/*.{extension}'
    return glob.glob(pattern, recursive=True)


# Пример использования
directory = '.'  # Текущий каталог
# directory = r'C:\Users\Kirill\PycharmProjects\pythonProject1'  # Текущий каталог
extension = 'txt'  # Искомое расширение
files = find_files(directory, extension)

print(files, "\n")


# Функция для поиска файлов с нужным расширением
def find_files(directory, extension):
    path = Path(directory)
    return list(path.rglob(f'*.{extension}'))


# Пример использования
directory = '.'  # Текущий каталог
extension = 'txt'  # Искомое расширение
# extension = 'csv'  # Искомое расширение
files = find_files(directory, extension)

print(files, "\n")


# Функция для поиска файлов с нужным расширением
def find_files(directory, extension):
    matches = []
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, f'*.{extension}'):
            matches.append(os.path.join(root, filename))
    return matches


# Пример использования
directory = '.'  # Текущий каталог
extension = 'txt'  # Искомое расширение
files = find_files(directory, extension)

print(files, "\n")

# * - Ищет все файлы и каталоги в указанной директории и указанного расширения
path = r"C:\Users\Kirill\PycharmProjects\pythonProject1\*.txt"
files_and_dirs = glob.glob(path)

print(files_and_dirs, "\n")



path = r"C:\Users\Kirill\PycharmProjects\pythonProject1\*.txt"

# glob
files = glob.glob(path)
print(files, "\n")  # Найдет все файлы с расширением .txt


# pathlib
directory = Path(r"C:\Users\Kirill\PycharmProjects\pythonProject1")
files = list(directory.glob('*.txt'))

print(files, "\n")  # Найдет все файлы с расширением .txt

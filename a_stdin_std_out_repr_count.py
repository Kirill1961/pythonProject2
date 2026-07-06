'''
sys.stdin (ввод), sys.stdout (вывод), sys.stderr (ошибки). Это файлоподобные объекты
'''

import sys, re
import csv
from collections import Counter


""" Из коносли аргументы перемещаются в список argv """
""" Передать текст из консоли в пайтон-код можно через sys.stdin
    Вывод из кода в консоль можно через sys.stdout, """

# print(len(sys.argv), ' >>>>>>>>>>>>>>>')
# print("Имя скрипта:", sys.argv[0])
# print("Аргументы командной строки:", sys.argv[1:])
#
# regex = sys.argv[1]   # в переменную regex сохраняем 1-й аргумент из списка argv
# print(regex, ' regex')
# for line in sys.stdin:   #  из консоли ВВОД помещается в sys.stdin
#     print(line, ' line')
#     if re.search(regex, line): sys.stdout.write(line),
#     # sys.stdout.write((line))
#
#     count = 0
#     for line in sys.stdin:
#         count += 1
#         print(count, ' count')


""" Рабочий скрипт"""
# stdin_fileno = sys.stdin # в переменную stdin_fileno сохраняем  аргумент из sys.stdin
#
#
# for line in stdin_fileno:
#     # Remove trailing newline characters using strip()
#     if 'exit' == line.strip():
#         print('Found exit. Terminating the program') # это печать если встречается в line - 'exit'
#         exit(0)
#     else:
#         print('Message from sys.stdin: ---> {} <---'.format(line))# это печать если не встречается в line - 'exit'




""" Наиболее распространёные слова :: most_common_words.py"""
""" Вывод из кода в консоль можно через sys.stdout,
    Передать текст из консоли в пайтон-код можно через sys.stdin"""

''' Конвеерная передача - type eek.txt | py.exe .\a_stdin_std_out.py 4'''

# type eek.txt | python egrep.py'[0-9' | python line_count.py
try:
    num_words = int(sys.argv[1]) # Вводим число самых частых слов
except:
    print(' Применение : most_common_words.py nu_words')
    sys.exit(1)
counter = Counter(word.lower() for line in sys.stdin
                  for word in line.strip().split() if word) # через sys.stdin из консоли передаём текст в счётчик

for word, count in counter.most_common(num_words): #  через sys.stdout выводим в консоль most_common_words
    sys.stdout.write(str(count))
    sys.stdout.write('\t')
    sys.stdout.write(word)
    sys.stdout.write('\n')



#%%
# TODO sys.stdin (ввод), sys.stdout (вывод), sys.stderr (ошибки). Это файлоподобные объекты

import sys
from collections import Counter

def read_line():
    return sys.stdin.readline().rstrip('\n')  # Ввод строки в код


def write(value):
    print(f'Самая Частая Категория :')
    sys.stdout.write(str(value))  # Вывод строки из кода
    # sys.stdout.write(str(value))


def writeln(value=''):
    sys.stdout.write(str(value) + '\n')  # - Лишняя операция


def solve():
    n = [i for i in read_line().split(',')]  # Список элементов для передачи в Counter

    cnt = Counter(n)  # Счёт числа элементов коллекции
    print(cnt)
    val_max = max(cnt, key=cnt.get)  # Ключ с наибольшим value

    write(val_max)  # Преобразование в строку и Передача данных в Интерпретатор

    # writeln(val_max)  # - Лишняя операция


if __name__ == '__main__':
    solve()
# 'category1, category3, category3, category2, category2,'

#%%
# TODO HERE Анализ Конверсии
#  0 - Клиент не произвёл действие, 1 - клиент произвёл действие
#  Сколько % не произвёли действие
import sys

def read_line():
    return sys.stdin.readline().rstrip('\n')
    # return int(sys.stdin.readline().rstrip('\n'))  # str to int на лету


def write(value):
    sys.stdout.write(str(value))


def writeln(value=''):
    sys.stdout.write(str(value) + '\n')


def solve():
    str = read_line().strip("'")  # Если ввод в консоль строка, то strip("'") нужен
    # str = read_line()  # Если ввод в консоль числа, то strip("'") не нужен

    print(repr(str))

    data = list(map(int, str.split(' ')))
    print(data)

    total = len(data)
    zeros = data.count(0)

    percent = (zeros / total) * 100

    writeln(f"{percent:.2f}")


if __name__ == '__main__':
    solve()
    # '1 1 1 0 1 0 1 1' или 1 1 1 0 1 0 1 1

#%%
# TODO Потоки, sys.stdin, sys.stdout
import sys


def r_line():
    return sys.stdin.readline()


def write(x):
    return sys.stdout.write(x)


def solve():
    d = r_line().strip("'\n")  # Обрезка не нужных символов
    print('Получил из потока в Код :', repr(d))  # Контроль Не нужных символов через repr
    data = int(d) * 2
    write(str(data))


if __name__ == '__main__':
    solve()


# TODO MY через Преобразование str - int - str
#  Потоки, sys.stdin, sys.stdout
import sys


def r_line():
    return sys.stdin.readline()


def write(x):
    return sys.stdout.write(x)


def solve():
    d = r_line().strip("'\n")  # Обрезка не нужных символов
    print('Получил из потока в Код :', repr(d))  # Контроль Не нужных символов через repr

    data = d.split(' ')  # Деление по Пробелам
    print(repr(data))
    data = list(map(int, data))  # Преобразование str to int

    print(repr(data))

    n_total = len(data)

    n_0 = data.count(0)

    res = n_0 / n_total

    write(str(res))  # Вывод в Поток результата


if __name__ == '__main__':
    solve()
# 1 1 1 0 1 0 1 1

#%%
# TODO MY Анализ Конверсии
#  0 - Клиент не произвёл действие, 1 - клиент произвёл действие
#  Сколько % не произвёли действие
import sys


def r_line():
    return sys.stdin.readline()


def write(x):
    return sys.stdout.write(x)


def solve():
    d = r_line().strip("'\n")  # Обрезка не нужных символов
    print('Получил из потока в Код :', repr(d))  # Контроль Не нужных символов через repr

    n_0 = d.count('0')  # Число Нулей в строке
    n_1 = d.count('1')  # Число Единиц в строке
    n_total = n_0 + n_1

    res = n_0 / n_total

    write(str(res))  # Вывод в Поток результата


if __name__ == '__main__':
    solve()
# 1 1 1 0 1 0 1 1
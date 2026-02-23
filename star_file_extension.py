"""В выражении path = r"D:\downloads\SPAM Assassian\hard_ham\*", символ * используется как универсальный
подстановочный знак или маска для поиска файлов. В контексте работы с путями и файлами, * означает "соответствует любому
 количеству любых символов". Это позволяет вам найти все файлы или каталоги внутри указанного пути, удовлетворяющие
 этому шаблону.
Подробное объяснение использования *:
* (звезда): Соответствует нулевому или более количеству любых символов.
Примеры: file* найдет file, file1, file2.txt, file_xyz.jpg, и т. д."""
import os
import pandas as pd
import numpy as np


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(*a, " распаковали из списка")

a = ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(*a, " распаковали из кортежа")

def add_file(*args):
    arg = args  # args уже является кортежем, так что дополнительная распаковка не нужна
    for i in arg:
        print(i)

add_file("13", "14", "15")


def add_file(*args):
    arg1, arg2, arg3 = args  # Распаковываем кортеж в отдельные переменные
    print(arg1)
    print(arg2)
    print(arg3)

add_file("13", "14", "15")

# фильтрация по расширению файла
#os.path.splitext, чтобы разделить имя файла и его расширение
files = ["13.txt", "23.txt", "25.pdf", " ", "14.txt", "xls_x.xlsx"]
for file in files:
    if os.path.splitext(file)[1] == ".txt":
        print(file)

# фильтрация по расширению файла
files = ["13.txt", "23.txt", "25.pdf", " ","14.txt", "xls_x.xlsx"]
for i in files:
    if i[-4:] == ".txt":
        print(i)


l = [1, 2, 3, 4]
a, b, c, d = l
print(a, b, c, d)

a_, *d_ = l
print(a_, *d_)

a1, *b1, c1 = l
print(*b1)


a2, b1, *c2 = l
print(*c2)

# TODO
#  / → всё слева = только позиционные аргументы
#  * → всё справа = только именованные аргументы
ls = list(range(5))

def foo(x, /, *, n=0):
    x.append(n)
    return ls
print(foo(ls, n=100))

d = {'A': list(range(1, 5)), 'B': list(range(10, 50, 10))}

print(dict(**d))
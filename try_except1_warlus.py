"""     Try: он запускает блок кода, в котором ожидается ошибка.
    Except: здесь определяется тип исключения, который ожидается
            в блоке try (встроенный или созданный).
    Else: если исключений нет, тогда исполняется этот блок
            (его можно воспринимать как средство для запуска кода
            в том случае, если ожидается, что часть кода приведет к исключению).
    Finally: вне зависимости от того, будет ли исключение или нет,
            этот блок кода исполняется всегда."""
""" Имитация ошибки NameError  """

with open('my_txt.txt', 'w') as _flow:
    print('ok ok ok', file=_flow)
with open('my_txt.txt') as _flow:
    try:
        for i in _flo:
            print(i, " _flo _flo _flo")
    except:
        print('NameError change _flo on _flow ')
my_try = open('vsearch.txt', 'w')
my_try.write('All right')
my_try = open('vsearch.txt')
read_mt = my_try.read()
my_try.close()
print(read_mt)

""" Имитация ошибки ValueError _fl / _f  
вместо "except ValueError:" пишем - except Exception as err: 
где err это переменная в которую будет вносится тип ошибки 
из класса Exception  """

with open('my_t.txt', 'a') as _fl:
    file_my_txt = _fl.write('no no no')
try:
    with open('my_t.txt') as _f:
        my_txt = _fl.read()
        # a = int(input())
        # print(my_txt) if a == 123 else print('Is unable call')
        print((my_txt))
except Exception as err:
    print(' ValueError change _f on _fl', str(err), " >>>>>>>>>>>>>>>>>>>>>>")

""" Имитация ошибки 'open('C:')' для получения ошибки
 PermissionError"""

with open('my_ttxt', 'w') as __fl:
    # print('ez ez ez', file=__fl)
    __fl.write('ye ye ye ')
try:
    with open('C:') as __fl:
        txt_f = __fl.read()
        print(txt_f, ">>>>>>>>>>")
except PermissionError:
    print('Permissionerror change C: on my_ttxt ')
# demof =  open('demo.txt', 'r')
# getcontentoffile = demof.read()
# print(getcontentoffile)
# demo.close()

""" модуль sys открывает доступ к внутренним
механизмам интерпретатора набору функций и переменных
 ф-ция sys.exc_info() извлекает данные по активному
  на данный момент исключению """

import sys

try:
    1 / 0
except:
    err = sys.exc_info()
    for e in err:
        print(e)

"""<class 'ZeroDivisionError'>
division by zero
<traceback object at 0x000001821F8B0F80>"""


# Читаем из txt и обрабатываем строки в своей директории
with open('file.txt') as f:
    while line := f.readline():
        print(f"Прочитана строка: {line.strip()}")


# Список, в котором нужно находить и сохранять длины строк больше 3
data = ["abc", "de", "fghi", "jklm"]
long_strings = [length for s in data if (length := len(s)) > 3]
print(long_strings)  # Выведет: [4, 4]


# Присваивание переменной внутри выражения, Пример использования в цикле
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(f"Длина списка: {n}")
    numbers.pop()


# Пример использования в условии if
numbers = [1, 2, 3, 4, 51, 2, 3, 4, 5]
if (m := len(numbers)) > 0:
    print(f"Длина списка: {m}")


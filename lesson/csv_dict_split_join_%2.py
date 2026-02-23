import csv
import pprint
from datetime import datetime

""" Библиотека pretty - printing даёт нам удобочитаемый вывод"""
# with open('c_data.csv', 'r') as file:

""" ignor = file.readline() пропускает 1-ю строку, тк чтение строк с readline() начинается с 1-й строки """
#
# ignor = file.readline()
# reader = csv.DictReader(file, fieldnames=['TIME', ' DESTINATION'])
# for i in reader:
#     print(i)

""" Заполнение словаря с помощью for  и .split, /str.split(sep=None, maxsplit=-1)/, sep - это разделитель
в нашем случае это ' , '. split - возвращает строку преобразованную в список состоящий из строк значений
из исходной строки / строку 'a, b, c' преобразует в список ['a', 'b', 'c']
в нашем случае '09:35,FRIPORT' преобразуются в '09:35', 'FRIPORT'  
    .strip(chars) - метод который вернёт строку с удалёнными символами вначале и в конце строки,
аргумент chars может быть любым символом /<, >, \n, и тд /.
    .title - метод который строчное значение первую букву преобразует в upper"""

# with open('c_data.csv', 'r') as file:
#     ignor = file.readline()
#     flights = {}
#     for line in file:
#         k, v = line.strip().split(',')  # Методы в ряд это цепочка методов
#         # print(line)
#         flights[k] = v.title()
#     pprint.pprint(flights)

""" _______________________заполнение словаря с помощью csv.reader(file)"""

# with open('c_data.csv', 'r') as file:
#     ignor = file.readline()
#     reader = csv.reader(file)
#     flights = {}
#     for k, v in reader:
#         flights[k] = v.title()
#     """ ________________pprint форматирует словарь из строки в удобочитаемую колонку """
#     pprint.pprint(flights)

""" Перевод из 24 часового в 12 часовой формат, я сделал с тернарным оператором, Бэрри
предлагает с datetime.
    .strptime(format) метод создает и выводит соответствующий объект даты/времени из строки, соответствующей формату format,
в нашем случае из строки '18:30' в формате '%H:%M' 
    .strftime(format) метод преобразует из 24 часового формата (котор сформирован strptime) в 
12 часовой формат.
    %H и %M 24-часовой формат, %I и %M 12-часовой формат, %p - АМ и РМ """


def t24(time24):
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


print(t24('18:30'))

t = datetime.strptime('06:30', '%H:%M').strftime('%I:%M%p')
print(t)

dt = datetime.now()
print(dt.strftime('%H:%M - %m.%d.%Y года'))

""" Мой вариант преобразования из 24-час формата в 12-час и слов из верхн регистра в нижний 
начинающихся с заглавных букв"""


# from _datetime import datetime
#
# with open('c_data.csv', 'r') as f:
#     ignor = f.readline()
#     reader = csv.DictReader(f, fieldnames=['TIME', 'DESTINATION'])  # ключи для "время вылета" и "пункт назначения"
#     for k in reader:  # fieldnames=['TIME', 'DESTINATION']
#         # dt = str(k['TIME'])
#         distination_for_scoreboat = (k['DESTINATION']).title()  # преобразуем 1-е буквы в заглавные
#         time_distination = datetime.strptime(str(k['TIME']), '%H:%M').strftime('%I:%M%p')  # 24-час в 12-час формат
#         print(time_distination, distination_for_scoreboat)
#
# """ Преобразование из 24 час в 12 час формат, по учебнику через ф-ю convert24_12, цепочка методов, """


def convert24_12(time24):
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('c_data.csv', 'r') as file:
    ignor = file.readline()
    flights = {}
    for line in file:
        """ !!!! Разъяснение по split(',') - цикл помещает в line из 'c_data.csv' целую строку из 2х значений,
            компилятор видит один объект(строку) поэтому что бы приравнять к двум переменным k и v надо
            значения в строке разделить запятой """
        k, v = line.strip().split(',')  # Методы в ряд это цепочка методов, split(',') делит запятыми,
        # strip() убирает лишние символы
        flights[k] = v
        # pprint.pprint(flights)
        flights2 = {}
        # print(k, v)
for k, v in flights.items():  # items очищает словарь от кавычек и скобок, извлекает из словаря key и value
    flights2[convert24_12(k)] = v.title()
pprint.pprint(flights2)

""" _______________________Преобразование 24 / 12 с помощью генератора словаря"""
more_flights = {convert24_12(k): v.title() for k, v in flights.items() if v == 'WEST END'}
print(more_flights)

""" НЕЗАКОНЧЕНО Моё преобразование 24 / 12 с помощью генератора словаря"""

with open('c_data.csv', 'r') as fil:
    ignor = fil.readline()

    # for i in fil:
    #     # print(i)
    #     kk, vv = i.strip().split(',')
    #     print(kk, vv)
    fl = [{(i.strip().split(','))[0]: (i.strip().split(','))[1]} for i in fil]
    print(fl)

""" ','.join используется при конвертации списка в строку. Метод принимает итерируемый объект в качестве аргумента
    например список и преобразует его в строку как бы вытягивая из списковых кавычек строчные значения.
    Разделить преобразованные значения можно запятой указав это в ' ' перед join """
l_s = ['ab', 'cd']
print(','.join(l_s), ' join join join')

""" Ещё способ преобразования списка в строку с join"""
mylist = [u'a', u'b', u'c']
result = "('%s')" % "','".join(mylist)
print(result, '  % join % join % join')

s = 'Welcome to the python world'
name = s[10:]
print(name)
A1 = s.split()
print(A1, '  split A1 A1 A1')


""" Оператор % выполняет деление по модулю те возвращает только остаток, 
    if %2 == 0 - деление на 2 без остатка значит чётное, if х % 2 - условие 
    если х делится на 2 с остатком, if not  х % 4 - если x делится на 4 без остатка
    Деление по модулю - 23 : 4 = 4/делитель/ * 5/неполное частное/ + 3/остаток/
    3%4 >>> 3 расшифровка: З = 0 * 4 + 3. Коэффициент равен 0, а остаток равен 3.
    ЕСЛИ ДЕЛИМОЕ МЕНЬШЕ ДЕЛИТЕЛЯ то деление по модулю % = ДЕЛИМОМУ
    выражения if %2 == 0  и  if not х%2  ОДИНАКОВЫ по смыслу
isinstance() - ф-я возвращает тип объекта на на который ссылается переменная"""

""" определение чётного/нечётного значения"""
dsta = [1, 2, 3, 4, 5, 6, 7, 8]
new_data = []
for num in dsta:
    if not num % 2:
        print(num, num % 2)
        new_data.append(num)
print(new_data)

""" то же самое но с генератором list comprehension"""

new_data = [num for num in dsta if num % 2 == 0]
print(new_data)

""" Проверяем тип объекта c isinstance() """

dsta = [1, 'two', 3, 4, 'five', 6, 'seven', 8]
new_data = []
for num in dsta:
    if isinstance(num, str):
        new_data.append(num)
print(new_data)

""" то же самое но с генератором isinstance(num, type)"""

new_data = [num for num in dsta if isinstance(num, str)]
print(new_data)

""" Разбиваем tuple на строчные объекты и преобразуем все стр ОБ в строки с заглавными буквами """

data = ('So long and thanks for all the fish'.split())
new_data = []
for word in data:
    new_data.append(word.title())
print(new_data)

""" ____________________то же самое но с генератором """

new_data = [word.title() for word in data]
print(new_data)

""" .keys  и  .values методы возвращают ключи и значения словарей, с помощью цикла for"""

m_dict = {dk for dk in more_flights.values()}
print(m_dict)

""" _______________________Преобразование 24 / 12 с помощью генератора словаря,
   но главное в этом генераторе что мы поменяли местами key и value, и тк ключи в словаре уникальны 
   ОБ с повторными ключами не выводятся"""

fts_swap = {v.title(): convert24_12(k) for k, v in flights.items()}
print(fts_swap)

""" my_fts в данном случа - SET (множество), тк в множестве все элементы уникальны и повторения не возможны,
    то ко-во ОБ сократилось"""
my_fts = {dk for dk in fts_swap.values()}
print(my_fts)

""" передали ф-ции set сокращённый словарь fts_swap и извлекли из него ключи,
    получили множество с  ключами из fts_swap"""
my_ftss = set(fts_swap.keys())
print(my_ftss, '//')

fts = {convert24_12(k): v.title() for k, v in flights.items()}  # Полное расписание д/дальнейших действий
pprint.pprint(fts)

""" Мой вариант , обмен местами key и value, key - должны стать пункты назначения
    а value - время вылета и прилёта, в таком варианте fts.values() можно не помещать в set тк
    в словаре одинаковые ключи удаляются"""
new_dict = {}
for i in fts.values():
    tlist = []
    for k, v in fts.items():
        if i == v:
            tlist.append(k)
            new_dict[v] = tlist
pprint.pprint(new_dict)

""" Мой вариант с генератором, взамен tlist = [] и tlist.append(k) используем list comprehension (генератор),
    словарь заполняется инициализацией через переменные"""

new_score = {}
for i in set(fts.values()):
    new_score[i] = [k for k, v in fts.items() if i == v]
print(new_score)

""" Вариант Бэрри - обмен местами  key и value, ключами становятся повторяющиеся ОБ (destination) а тк в dict
    ключи уникальны то все повторы ключей удаляются и здесь на один ключ получается 2 значения ,
    например - 'West End': '09:55AM', '07:00PM'. Поэтому для реализации задачи мы отдельно вытаскиваем ключи,
    помещаем их в set где повторы сразу сокращаются(set(fts.values()), это set перебираем циклом for
    в который включаем другой цикл перебирающий исходный dict по key и value с помощью fts.items().
    Фильтр состоящий из условия if отбирает значения принадлежащие ключам i"""

""" Полуфабрикат для словаря"""
for i in set(fts.values()):
    print(i, [k for k, v in fts.items() if i == v])

""" Создаём словарь по Бэрри через заполнение пустого  """
new_score = {}
for i in set(fts.values()):
    new_score[i] = [k for k, v in fts.items() if i == v]
print(new_score)

""" Создаём словарь генератором в одну строку, где i - это клю взятый 
из цикла for i in (set(fts.values())), значения ключа i  помещены 
в список [k for k, v in fts.items() if v == i] и отфильтрованы условием if v == i"""

new_score2 = {i: [k for k, v in fts.items() if v == i] for i in (set(fts.values()))}
pprint.pprint(new_score2)

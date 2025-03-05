
import re
from bs4 import BeautifulSoup


# TODO Правило:
#  Даты и Телефоны группируются по заданным разделителям / или -  (dd/mm/yyyy или 8-ххх-хх-хх)
#  Каждая группа состоит из разрядов
#  Для каждого разряда диапазон только [0-9],
#  {4} - Фигурные скобки это кол-во повторов Цифры


# TODO Задача: извлечь корректные даты и телефоны
text_data = '''Сегодня на календаре 02/03/2025, а вчера было 01/03/2025.  
Встреча запланирована на 15/04/2024, а отчёт сдадим до 30/06/2023.  
Некорректные даты: 99/99/9999, 32/13/2025, 7/3/2024.  
Допустим, в логе есть 05/08/2020 и 25/12/2019.'''


phones = """+7 909-212-9930", "+3*9272160048", "7^999999a", +7 910-212-9930, +9 920-216-00-48, 8 920-216-0048"""


# TODO Жёсткая Примитивная Регулярка
res = "".join(re.findall(r"\d+\W", text_data))
res1 = "".join(re.findall(r"[\d+/ ]", text_data))


print(res, '\n')
print([i for i in res1.split(" ") if i[0:2] < "32" and i[3:6] < "13" and i[7:] < "2025" and i != ""], '\n')


#  TODO Костыли, c помощью итерации удаляемых символов
res2 = []
for p in ".,":
    text_data = text_data.replace(p, " ")
data = text_data.split(" ")
for i in data:
    if i[0:2] < "32" and i[3:6] < "13" and i[7:] < "2025" and i != "":
        res2.append(i)
print(res2, '\n')


# TODO Вывод даты
res3 =re.findall(r'[0-9]{2}[^0-9][0-9]{2}[^0-9][0-9]{4}', text_data)
res4 =re.findall(r'\d{2}\W\d{2}\W\d{4}', text_data)
res5 =re.findall(r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b', text_data)
print(res3, '\n')
print(res4, '\n')
print(res5, '\n')


# TODO Вывод телефона
res6 = re.findall(r'(?:\+7|8) (?:9[012][09]-)(?:2[01][026]-)(?:\d{4})', phones)
res7 = re.findall(r'(?:\+7|8)[\s-]?(9\d{2})[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})', phones)
print(res6, '\n')
print(res7, '\n')

# TODO Преобразование списка кортежей res7, в удобочитаемый формат
n = 0
while n < len(res7):
    n += 1
    r = '-'.join([i for i in res7[n-1]])
    print(r)


s = 'aC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'

res = re.match('AC/DC', s, flags=re.I) # поиск подстроки В НАЧАЛЕ СТРОКИ s
print(res, res.group(), " res.group()>>>>>>>>")

res = re.search('/DC', s) # поиск ВО ВСЕЙ СТРОКЕ и выводит первую попавшуюся подстроку
print(res, " search('/DC', s)")
print(res[0]) # что бы вывести без описания пишем так res[0]

res = re.findall('CA', s) # поиск ПОВСЕЙ СТРОКЕ всех заданных подстрок
print(res, " findall('CA', s)")

res = re.split('A', s) # делит строку по заданному разделителю
print(res, " split")

st = 'что бы! вывести? без Петрова Ё. Е. описания  пишем& так ** res[0]'
# " r " - сырая строка, отключено экранирование
res = re.findall(r'вы',st, flags=re.I)
print(res, " findall res 1")



st = 'что бы! 15вывести? без Петрова Ё. Е. описание548  пишем& так ** res[0]'
# pattern = r'\w+\s[А-ЯЁа-яё]{1}\.\s*[А-ЯЁа-яё]{1}\.'


res = re.findall(r'(\w+)\s[А-ЯЁа-яё]{1}\.\s*[А-ЯЁа-яё]{1}\.', st)
print(res, " findall res 2")


res = re.search(r'\d+[а-о]', st)
print(res, " search res 3")


# Находим и возвращаем одни цифры
s = " test_sub 0 test_sub 1 test_sub 2 test_sub 3 test_sub 4 "
res = re.findall( "\d", s)
print(res, " Находим и возвращаем одни цифры findall( '\d', s) ")



# sub - самое простое использование re.sub("что надо заменить","чем надо заменить", "строка где надо заменить")
# .
#  больше вариантов применения в док-ции.

pattern = 'aa'
s = 'aabb'
result = re.sub(pattern,'>>>>',s)

print(result, " 1й вариант замена pattern на s")


pattern = 'fg'
s = 'fgbb'
res = re.sub(pattern,'***',s)

print(res, " 2й вариант замена pattern на s")



phone_no = '(212)-456-7890'
pattern = '\D'               # '\D' - всё кроме цифр меняем в строке
result = re.sub(pattern,'*',phone_no)

print(result, " замена дефисов на  звёздочки")


# возводим в квадрат цифры в строках, d+ это цифры в строке
def square(match):
    num = int(match.group()) # group() -  возвращает полное совпадение конкретной подгруппы
    print(num, " NUM")
    return str(num*num)

l = ['A1','A2','A3']
pattern = r'\d+'    # d это цифры в строках, '+' - это несколько символов d

new_l = [re.sub(pattern, square, s) for s in l] # re.sub(что, чем, где)

print(new_l, " возводим в квадрат цифры в строках")


# меняем в строке А на В
# group() - Возвращает одну или несколько подгрупп совпадения
# Через системную переменную match из ОБ re.Match можно выводить методом group() группы
#  если в скобках group() нет числа то возвращается вся группа.
def square(match):
    num = int(match.group())
    return str(num*num)

l = ['A1','A2','A3']
pattern = r'\D'

new_l = [re.sub(pattern, " B", s) for s in l]

print(new_l, " меняем в строке А на В")



# group() - Возвращает одну или несколько подгрупп совпадения
# Группа определяется помещением выражения в круглые скобки ().

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m.group(0)       # The entire match

m.group(1)       # The first parenthesized subgroup.

m.group(2)       # The second parenthesized subgroup.

m.group(1, 2)    # Multiple arguments give us a tuple.


print(m.group())
print(m.group(0)) # в скобках № группы
print(m.group(1))
print(m.group(2))
print(m.group(0, 2))



# Поиск, замена  и возврат  чисел из строки
def func(x):
    print(x)
    return " 500 "
s = " test_sub 0 test_sub 1 test_sub 2 test_sub 3 test_sub 4 "
res = re.sub( r"(test_sub) (\d)", func,  s)
print(res, " Поиск, замена  и возврат  чисел из строки")


# Поиск и просто замена чисел в строке
def func(x):
    print(x)
    return " 500 "
s = " test_sub 0 test_sub 1 test_sub 2 test_sub 3 test_sub 4 "
res = re.sub( r" (\d)", func,  s)
print(res, " Поиск и просто замена чисел в строке")


# Группа определяется помещением выражения в круглые скобки ()
# в ОБ re.Match группам присваивается порядковый номер (test_sub) - первая, (\d) - вторая.
def func(match):
    print(match.group(2))
    integ = match.group(2)
    return integ
s = " test_sub 0 test_sub 1 test_sub 2 test_sub 3 test_sub 4 "
res = re.sub( r"(test_sub) (\d)", func,  s)
print(res, " Поиск и просто замена чисел в строке")


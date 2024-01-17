
import re
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
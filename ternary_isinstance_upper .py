

a = 3
b = -12


var = 0 if a == b else 1 if a > b else -1
c = a if a > b else b
print(c)
c = a if b % 2 == 0 else b
print(c)
c = max(2, 3, a if a > b else b, 10)
print(c)
""" ______________перевод времени из 24 в 12 часовой формат """
e = 15 # input время в 24 часовом формате
f = 12
c = f'{0} AM' if e - f == 12 else f'{e - f} PM' if e - f > 0 else f'{e} AM'
""" Разъяснение: с = 0 если  e - f = 12, иначе с = e - f и если e - f > 0, то c = e ;
    АМ и РМ форматируем integer в str и подставляем для вывода нужный параметр"""
print(c)

print(a if b < a else b)

print(a if abs(b) < a else b)

u = 'upiter'
l = 'luna'
print(l.upper() if l == 'upper' else u.upper())

print('Mars'.upper() if 'Mars' == 'upper' else 'Vienna'.upper())

print('luna' + 'upiter')  # конкотенация

print('vienna ' + (l.upper() if l == 'upper' else u.upper()) + f'{1}')

""" ________________Изменение первых строчных символов c   UPPER
 .title — возвращает копию строки, в которой каждое слово начинается с заглавной буквы,
        инф по всем методам строк в справочниках"""

y = ' good day VORONEG'
print(y.title())


""" Проверяем тип объекта c isinstance() """

dsta = [1, 'two', 3, 4, 'five', 6, 'seven', 8]
new_data = []
for num in dsta:
    if isinstance(num, str):
        new_data.append(num)
print(new_data)

""" то же самое но с генератором list comprehension"""

new_data = [num for num in dsta if isinstance(num, str)]
print(new_data)
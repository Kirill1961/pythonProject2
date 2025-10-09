from operator import attrgetter, itemgetter
from collections import namedtuple

# itemgetter позволяет вам одновременно получить доступ к нескольким элементам из списка
# извлекаем элементы по индексу
templist = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
f = itemgetter(0, 3, 6, 15, 18, 19)
sublist = list(f(templist[0]))
print(sublist, " operator.itemgetter извлекает элементы по индексу", "\n")

ps = [(2, 4), (-1, 7), (4, 5), (3, -4), (-1, -5)]
got = itemgetter(0, 2, 3)(ps)
print(got, " доступ к нескольким элементам из списка")


def dist(x):
    return (x[0] ** 2 + x[1] ** 2) ** 0.5


ps = [(2, 4), (-1, 7), (4, 5), (3, -4), (-1, -5)]
filtered = list(filter(lambda x: dist(x) > 6.0, ps))
print(filtered)

# TODO Извлекаем заданные вложенные словари
d = {'A': {'a': 100, 'b': 1, 'd': 10}, 'B': {'a': 2, 'd': 3, 'b': 40}, 'C': {'d': 21, 'a': 30, 'b': 555}}
print('Извлекаем заданные вложенные словари : \n', itemgetter('B', 'C')(d))

# TODO Извлекаем атрибуты с attrgetter
Person = namedtuple('Person', ['name', 'age'])
p1 = Person('Лиса', 25)
p2 = Person('Kirill', 54)
p3 = Person('Sveta', 18)

print(p1.name)  # Юля
print(p2.age)  # 25

print('Извлекаем атрибуты с getattr : \n', getattr(p2, 'name'))
print('Извлекаем атрибуты с attrgetter : \n', attrgetter('name')(p2), attrgetter('name')(p3))
print('Извлекаем атрибуты с attrgetter : \n', p1.name, p3.name)

# TODO Мой пример для закрепления

dog = namedtuple('dog', ['name', 'breed', 'color'])
cat = namedtuple('cat', ['name', 'breed', 'color'])

p1 = cat('Lisa', 'dnt know', 'Red')
p2 = dog('Bim', 'dnt know', 'cheprack')

print('Извлекаем атрибуты с attrgetter : \n', attrgetter('name')(p1), attrgetter('color')(p1))
print('Извлекаем атрибуты с attrgetter : \n', attrgetter('name')(p2), attrgetter('color')(p2))


# TODO attrgetter - работает с классами

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def output(self, x):
        return x


p1 = Cat('Masya', 'gray')
p2 = Cat('Lisa', 'red')

print('attrgetter - работает с классами : \n', attrgetter('name', 'color')(p1))
print('Вывод атрибута через объект : \n', p2.color)

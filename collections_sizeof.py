""" COLLECTION пакет для обработки словарей,списков,множеств и тд"""
import csv
from collections import defaultdict, deque, OrderedDict, Counter, namedtuple, ChainMap
from itertools import islice


# defaultdic нужен для создания словаря со значением по умолчанию, значение подставляется
# при обращении к несуществующему ключу.То есть можно наклепать ключей без значений с последующей вставкой значений
# указываем функцию (или тип) по умолчанию, которая будет использоваться для создания значений для новых ключей.

counts = defaultdict(lambda: [0, 0])  # lambda возвращает в словарь counts - value [0, 0], инициализируем словарь
for j in range(2):
    for i in range(5):
        counts[j][0] += 1  # раздельно суммируем value [0, 0] с индексом [0] и индексом [1]
        counts[i][1] += 1

print(counts, "раздельно суммируем value [0, 0] с индексом [0] и индексом [1]")

d = defaultdict(list)
s = [d[_] for _ in range(5)]
print(d, "Инициировали пустые словари с ключами из  range(5)")

# Инициализация Словаря со всатвкой Value
d1 = defaultdict(list)
s1 = [d1[j].append(i) for i, j in enumerate("asdf")]
print(d1, "Инициализация Словаря со всатвкой Value")

g = defaultdict()  # инициализация словаря без key и без value
g[88] = 55  # присваивание key 88 - value 55
print(g)

g = defaultdict(list)  # если указываем ТИП данных в скобках, то генерируемые значения будут иметь ИХ свойства
g[88].append(55)
print(g, ' append(55)')

g = defaultdict(set)
g[88].add(55)
print(g)

g = defaultdict(int)
g[88]
g[77] = 'aa'

g.default_factory = int  # default_factory  структура/тип данных указанная в аргументе defaultdict - int, set, list и тд
g[500] = [1, 2]

print(g, ' ////  defaultdict(int)')

a = [(50, 'Hadoop'), (50, 'Python'), (50, 'HBase'), (50, 'Java'), (50, 'Spark'), (50, 'Storm'),
     (10, 'NoSQL'), (10, 'MongoDB'), (10, 'HBase'), (10, 'data science'), (10, 'Java'), (10, 'Storm'),
     (20, 'Hadoop'), (20, 'numpy'), (20, 'pandas'), (20, 'Java'), (20, 'HBase'), (20, 'Python'),
     (30, 'pandas'), (30, 'Python'), (30, 'data science'), (30, 'numpy'), (30, 'Spark'), (30, 'NoSQL'),
     (40, 'Java'), (40, 'Python'), (40, 'Storm'), (40, 'numpy'), (40, 'HBase'), (40, 'NoSQL')]
b = ((50, 'Hadoop'), (50, 'Python'), (50, 'HBase'), (50, 'Java'), (50, 'Spark'), (50, 'Storm'),
     (10, 'NoSQL'), (10, 'MongoDB'), (10, 'HBase'), (10, 'data science'), (10, 'Java'), (10, 'Storm'),
     (20, 'Hadoop'), (20, 'numpy'), (20, 'pandas'), (20, 'Java'), (20, 'HBase'), (20, 'Python'),
     (30, 'pandas'), (30, 'Python'), (30, 'data science'), (30, 'numpy'), (30, 'Spark'), (30, 'NoSQL'),
     (40, 'Java'), (40, 'Python'), (40, 'Storm'), (40, 'numpy'), (40, 'HBase'), (40, 'NoSQL'))

print(a.__sizeof__(), ' //// a.__sizeof__')
print(b.__sizeof__(), ' //// b.__sizeof__')

# По факту создание нового словаря, с ключами из символов строки и значениями
# создаваемые циклом a_dict[char] += 1

a_dict = defaultdict(int)
s = 'hellowword'
for char in s:
    a_dict[char] += 1
print(a_dict, '  //// a_dict')

d = defaultdict(list)

e = defaultdict()
# e['d']
e[22] = ' Hi '

e.default_factory = lambda: [1.2, 3]  # Переопределение value если ключ без значения, переопределяем с list на [1.2,3]

e['d']
e['ff']
print(e, ' |||||||||||||||| lambda: [1.2, 3]  # Переопределение value')

c = [(10, 'NoSQL'), (20, 'numpy'), (40, 'Storm'), (40, 'numpy'), (30, 'Storm')]
d = defaultdict(list)
for k, v in c:
    # print(k, v)
    # d[v] += k # суммирует значения, при  defaultdict(int)
    # d[v] += [k] # добавляет ОБ в  значение в виде списка, при defaultdict(list)
    d[v].append(k)  # то же что и " d[v] += [k] "  при defaultdict(list)
print(d, ' //// d[v].append(k)')

v = {'g': 45, "c": 14, 'd': 88, 'a': 2, }
print(sorted(v.items(), key=lambda x: x[0]), '  //// key=lambda x: x[1]')

# most_common

# deque(), это двунаправленная очередь. Быстро вставляет и берёт элементы с двух  концов. Потокобезопасная

b = [(50, '*************'), (50, 'Python'), (50, 'HBase'), (50, 'Java'), (50, 'Spark'), (50, 'Storm'),
     (10, 'NoSQL'), (10, 'MongoDB'), (10, 'HBase'), (10, 'data science'), (10, 'Java'), (10, 'Storm')]

a_deque = deque()
for ide in b:
    a_deque.append(ide)
a_deque.appendleft("okokokokokokokookokok")  # Вставляем слева
a_deque.appendleft("9595959")
a_deque.popleft()  # забираем значения и слева и справа. здесь удалено "9595959"
a_deque.appendleft("888888888888888888888")
# a_deque = deque(a_deque, maxlen=4)
print(a_deque, '  //// a_deque')

with open('c_in_data.csv') as file:
    a_deque = deque(file, maxlen=3)
    for line in a_deque:
        # print( '//// a_deque CSV    ', line, end='')
        print(line.rstrip())

# OrderedDict, упорядоченный словарь. Нужен для действий со словарём, где необходим порядок элементов,
# например, сравнение с учётом порядка или перестановки элементов с сохранением порядка, но платим памятью

first = {1: 1, 2: 2, }
second = {2: 2, 1: 1}
third = {1: 1, 2: 22, 3: 300}

print(first == second, ' //// OrderedDict сравниваем словари, но не порядок')  # сравниваем словари, но не порядок

order1 = OrderedDict(first)
order2 = OrderedDict(second)
order3 = OrderedDict(third)

print(order1 == order2, ' //// OrderedDict сравниваем порядок словарей')  # сравниваем порядок словарей

print(order2.popitem(last=False))  # дёргаем первый или последний элемент

order3.move_to_end(2, last=False)  # перемещаем i-й элемент в конец или начало
print(order3, ' //// OrderedDict')

# ChainMap, Нужен для логического объединения словарей и для поиска информации,
# но при изменениях меняется только 1-й словарь.

chain = ChainMap(first, second, third)
print(chain[3])  # Отыскивает 1-й попавшийся ключ
chain[3] = 100  # Изменяет 1-й словарь
print(chain, '  //// ChainMap', "\n")

# Counter, Нужен для подсчёта элементов в последовательности
# или для частотного анализа текста. Работает только hashable.

counter = Counter('Yellow Blue black 1282297033')
print(counter, ' //// Counter', "\n")

print(f'Преобразование объекта Counter в словарь ->>>>>{dict(counter)}')

#   (3) - выводит список кортежей с тремя самыми повторяемыми символами, [2] -  индекс нужного кортежа из списка
print(counter.most_common(3)[2][0], ' //// most_common', "\n")  # [0] - индекс значения из выбраного кортежа

#  Создание списка счётчиков для каждого вложенного списка
topic = [[2, 2, 0], [0, 2], [3, 1, 4, 2, 4]]
documents = [['s', 'd', 's'], ['w', 'd'], ['s', 'e', 'n', 'w', 'd']]
document_topic_counts = [Counter() for _ in documents]
print(document_topic_counts, " создали список объектов Counter для каждого вложенного LIST")
for k in range(len(documents)):
    for doc, word in zip(documents[k], topic[k]):
        document_topic_counts[k][word] += 1  # [k] - индекс ОБ Counter, [word] - ключ, value - количество тем в doc
        print(document_topic_counts[k], "\n")

# Создание объекта Counter для подсчета слов из файла
with open('cdata.csv', 'r') as file:

    word_counter = Counter(file.read().split())

print(word_counter, "Создание объекта Counter для подсчета слов из файла", "\n")


# Сложение и вычитание объектов Counter
counter1 = Counter(['a', 'b', 'c', 'a', '123'])
counter2 = Counter(['a', 'b', 'a', 'd'])
counter3 = Counter(['123'])

print(counter1 + counter2 + counter3, "Сложение и вычитание объектов Counter", "\n")


# Сложение словарей с Counter
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict(Counter(dict1) + Counter(dict2))
print(merged_dict, "Сложение словарей с Counter")

# namedtuple нужен для создания структуры данных, нечто среднее между стандартными типами
# и самописанным классом, неизменный, позволяет обращаться по имени атрибута,
# позволяет использовать индексы.

Dog = namedtuple('Dog', 'name breed age color')  # сюда диа аргумента ТИП и ПРИЗНАКИ
sandy = Dog('sandy', 'rizen', '15', 'balck')  # наименования признаков
print(sandy, " наименования признаков")
print(sandy[0:2], " обращение по индексу")  # обращение по индексу
print(sandy.color, " Обращение по атрибуту", '\n')  # Обращение по атрибуту

Point = namedtuple('Point', 'x y z')  # Любое количество атрибутов x, y, z и так далее
with open('point.csv') as file:
    for line in csv.reader(file):
        point = Point._make(line)
        print(point, '\n')


d2 = defaultdict(list)
# [d2[i].append(j) for i, j in zip(['a', 'f', 'w'], [11, 205, 0.3])]
for i, j in zip(['a', 'f', 'w'], [11, 205, 0.3]):
    d2[i].append(j)
print(d2, '\n')

# Скользящее окно, n - ширина окна
a = 'asdqwer'
def sliding_window(iterable, n):
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)
print(list(sliding_window(a, 3)), '\n')
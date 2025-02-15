
vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Provide a word to search for vowels:'
# word=input('Provide a word to search for vowels:')
found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, v)
gg = {}
gg[1] = 'flkhjlllpp'  # инициализация ключа  1
gg[2] = 'poiuytre'  # инициализация ключа 2
print(gg[1], gg[2])  # вывод значений из словаря gg с помощью ключей
print('////////////')
print(2 in gg)  # in - наличие в словаре gg ключа с именем 2
print(gg)

""" Вырезаем указанный ключ с помощью .pop () удаляет ключ и возвращает значение"""
ftg = {1: 'pop', 2: 'bob', 3: 'mop'}
print(ftg.pop(2, []))
print(ftg)

""" .popitem() - удаляет и возвращает  пару (ключ, значение),последние которые стоят в конце. 
    Если словарь пуст, бросает исключение KeyError."""

print(ftg.popitem())
print(ftg)

"""Шаблон с заполнения пустого словаря преобразованными данными из предыдущего словаря.
 Новый пустой словарь можно заполнить с помощью цикла извлекая с items() key и  value
    c последующей инициализацией перебираемых k и v """
# dict_for_iter2 = {}
dict_for_iter = {'j': 14, 'a': 1, 'b': 5, 'f': 3, }
dict_for_iter2 = {}
for k_d, v_d in dict_for_iter.items():
    dict_for_iter2[k_d] = v_d
print(dict_for_iter2)

""" Запись в список ключей /.keys/ и значений /.values /из словаря 
            МОЙ ПРИКОЛ - список из int значений и str ключей"""
list_t = []
for i_l in dict_for_iter2.values():
    list_t.append(i_l)
for i_l in dict_for_iter2.keys():
    list_t.append(i_l)
print(list_t)

""" Генератор списков или Списочное включение или list comprehension смысел в том что ставим всё выражение в [ ] вместо 
    метода append тем самым уменьшаем ко-во строк кода, генератор вызывает append автоматически"""
list_key = [i_l.title() for i_l in dict_for_iter.keys()]
print(list_key)

"""Список СЛОВАРЕЙ , добавим в  каждый dict из списка кортежей frdsh новое свойство с ключом 'frds'.
    из datasience пример с сотрудниками"""
frdsh = [(0, 1), (2, 1), (0, 2), (0, 3)]  # создаём друж / связи сотрудников по индексам из списка usrs
usrs = usrs = [{'id': 0, 'name': 'aa'}, {'id': 1, 'name': 'bb'}, {'id': 2, 'name': 'cc'}, {'id': 3, 'name': 'dd'}]

for us in usrs:  # перебрав список usrs через переменную us получим словари из users
    us['frds'] = []  # вставим в каждый словарь ключ 'frds' и назначим ему в качестве value - пустой список
for i, j in frdsh:  # перебираем кортежи из frdsh
    #     frds = [usrs[i],usrs[j]]

    usrs[i]['frds'].append(j)  # usrs[i] - выбираем ОБ  по индексу из списка usrs, тк выбранный ОБ - словарь, а ['frds']
    usrs[j]['frds'].append(i)  # это ключ с value в виде пустого списка, то можно вставить  значение append(i) или (j)
print(usrs)

# Замена просто value на список из value
d = {30 : 33, 10 : 11, 20 : 22}
dc = {k: [i] for k, i in d.items()}
print((dc, " Замена просто value на список из value"))

# Добавка в список к value ещё 1го значения
dc_append = {k: i.append("a") for k, i in dc.items()}
print(dc, " Добавка в список к  value ещё 1го значения")

# Получение значения из словаря по заданному ключу
print(d.get(30, "Kirill"), " - Получение значения из словаря по заданному ключу")
print(d.get(31, "Kirill"), " - Второй аргумент это возврат если указанного ключа нет")


# update - добавление в словарь нескольких ключей и значений
my_dict = {}  # Создание пустого словаря

# Добавление нескольких ключей и значений
my_dict.update({'key1': 'value1', 'key2': 'value2'})

print(my_dict, "update - добавление в словарь нескольких ключей и значений")


# isinstance - Сортировка value словаря
d ={'a': 555, 'b': "qwer", 'c': -33, 'd': 770}
res = [i for i in d.values() if isinstance(i, str)]
print(res, "isinstance - Сортировка value словаря ")

# fromkeys - Создание словаря с заданными ключами и значением по умолчанию
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict, "fromkeys - Создание словаря с заданными ключами и значением по умолчанию")

# Создание словаря с ключами и значением, которое является списком
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, [])
print(new_dict)

# Изменение одного из списков в словаре повлияет на все ключи, так как они ссылаются на один и тот же объект
new_dict['a'].append(1)
print(new_dict, "Изменение одного из списков в словаре повлияет на все ключи")


# ВАЖНО! один из главных способов добавления, переинициализация ключа
dict1 = {1: 2, 10:3}
dict2 = {2: 4, 20:5}
#  добавим в dict2 элемент 1: 2
dict2[1] = dict1[1]
print(dict2, "ВАЖНО! один из главных способов добавления, переинициализация ключа")

# Преобразование Словаря в Список, по Умолчанию св список ключей
l_dic = list(dict1)
print(l_dic, "Преобразование Словаря в Список, по Умолчанию св список ключей")

# Преобразование Словаря в Список, по Заданию в список значений
l_dic = list(dict1.values())
print(l_dic, "Преобразование Словаря в Список, по Заданию в список значений")
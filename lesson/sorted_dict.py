my_dict = {'z': 15, 'a': 2, 'y': 9, 'j': 0}

""" Отсортировать словарь по значению"""

""" итерация словаря и вывод ключа со значением
через ks проходя ключи, подставляя в my_dict[ks]
 получаем значение value, не забыть {}"""
for ks in my_dict:
    print(ks, '->', my_dict[ks])

""" ________________________Тоже самое но отсортированное по ключу """

for ks in sorted(my_dict):
    print(ks, '->', my_dict[ks])

"""Сортировка производится ф-цией sorted,в аргументф ф-ции передаём:
    1й арг СЛОВАРЬ my_dict,
    2й арг метод get применённый к словарю my_dict который возвращает
    value соответствующее key котор на данный момент проходит сортировку
    dict.get(key[, default]) - возвращает значение для ключа"""

dic_sort = {}
sor_get = sorted(my_dict, key=my_dict.get)

for ii in sor_get:
    """ Приравняв dic_sort[ii] = my_dict[ii] в новом словаре заполнили новый словарь 
    ключами dic_sort[ii] и значениями my_dict[ii]"""
    dic_sort[ii] = my_dict[ii]
    print(my_dict[ii], ' my_dict[ii]')
print(dic_sort, ' dic_sort')

""" Если в аргумент sorted добавить reverse=True, то выведется  отсортированный словарь наоборот  """

dic_sort = {}
sor_get = sorted(my_dict, key=my_dict.get, reverse=True)
for ii in sor_get:
    dic_sort[ii] = my_dict[ii]
    print(my_dict[ii])
print(dic_sort)


""" произведена сортировка только value
c помощью dict.items() - который возвращает пары (ключ, значение)."""
sort_it = sorted(my_dict.items())
for i_s in sort_it:
    print(i_s, '*')
for iss in sorted(my_dict.values()):
    print(iss)

"""Сортировка с помощью ф-ции itemgetter из модуля operator, получаем список кортежей:
[('j', 0), ('a', 2), ('g', 9)]
с помощью dict перед скобками преобразуем в словарь.
itemgetter можно использовать вместо лямбда-функции для
достижения аналогичной функциональности. Выводит аналогично sorted() и lambda,
но имеет другую внутреннюю реализацию.
Он берет ключи словарей и преобразует их в кортежи.
в аргументе key=itemgetter(1) стоит цифра "1" -это индекс сортируемого кортежа,
индекс "1" это value словаря значит sorted будет по значениям, если будет "0" ,
этот индекс первого знач в кортеже те ключа в словаре,
sorted будет по ключам """

rooms = {'a': 2, 'j': 0, 'g': 9, 'b': 5}
from operator import itemgetter

sorted_rooms = dict(sorted(rooms.items(), key=itemgetter(1)))
print(sorted_rooms)

""" Сортировка с помощью lambda ф-ции, в переменную ite_m
 поочерёдно передаются пары из dict в виде кортежа
 например первая пара ('a', 2), цифра в [ ] это индекс,
 если 0 то sorted по key, если 1 то по value,
 в конце список кортежей трансформ в словарь,
 sorted в обратном порядке с пощ ф - ции reversed """

dict_lamb = {'a': 2, 'j': 0, 'g': 9, 'b': 5}
sort_lamb = dict(reversed(sorted(dict_lamb.items(), key=lambda ite_m: ite_m[1])))
print(sort_lamb)

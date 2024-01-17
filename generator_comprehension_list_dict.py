
""" Генератор списков или Списочное включение или list comprehension смысел в том что ставим всё выражение в [ ] вместо 
    метода append тем самым уменьшаем ко-во строк кода, генератор вызывает append автоматически,
    то же самое можно делать со словарями"""

ls1 = [1, 2000, 'john', 3, 'a', 'bob']
ls2 = [(y, x) for x in ls1 for y in [ls1.index(x)]]
ls3 = {k: v for k, v in ls2}
print(ls3, ' ls3ls3ls3ls3ls3')
print(ls3[2], ' ls3[2]ls3[2]ls3[2]')
print(ls2, ' ls2ls2ls2ls2ls2')
tp = ('id', 'fo')
r = [l for l in tp]
print(r)

dict_for_iter = {'js': 14, 'av': 1, 'bh': 5, 'fp': -3, }

""" ___________________Генератор списков, Запись в list key и value из словаря"""

list_t = []
for i_l in dict_for_iter.keys():
    list_t.append(i_l)
print(list_t)

""" ___________________то же самое только с list comprehension"""

list_key = [i_l.title() for i_l in dict_for_iter.keys()]
print(list_key)

""" _______________Генератор словарей, преобразовав старый /dict_for_iter/ получаем новый словарь
    key  из прежнего словаря преобразовали с title(), а value увеличили на 100 """

dict_dif = {kd.title(): vd + 100 for kd, vd in dict_for_iter.items()}
print((dict_dif))

""" ___________Расширенные генераторы с фильтрами , условие if. 
     Данный генератор обрабатывает только value > 0  """

dict_dif = {kd.title(): vd + 100 for kd, vd in dict_for_iter.items() if vd > 0}
print((dict_dif))



from operator import itemgetter

ps = [(2, 4), (-1, 7), (4, 5), (3, -4), (-1, -5)]
got = itemgetter(0, 2, 3)(ps)

print(got, 'itemgetter, вывод изи списка по индексу')


# Объудинение пар в общий список

list_pair = [i if r == 0 else k for i, k in ps for r in range(2)]
print(list_pair, " Объудинение пар в общий список")

# Операции между LIST и LIST[LIST], умножить ОБ из b  на ОБ из LIST[LIST] поиндексно

x = [[10, 20, 30, 40], [50, 60, 70, 80]] # вложенные LIST[LIST]
b = [2, 2, 2, 2]

j = map(lambda k: [[j*k for j in  i] for i in x ], b)  # lambda вытаскивает  из вложенных LIST поиндексно все ОБ
print(next(j), " next(j) выводит одну итерацию")


# срезом [0:len(x)], берём 1-ю итерацию
print([ [j*v  for j in  i] for v in b for i in x][0:len(x)], " срезом [0:len(x)], берём 1-ю итерацию ")
import operator


# itemgetter позволяет вам одновременно получить доступ к нескольким элементам из списка
# извлекаем элементы по индексу
templist = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]
f = operator.itemgetter(0,3,6,15,18,19)
sublist = list(f(templist[0]))
print(sublist, " operator.itemgetter извлекает элементы по индексу", "\n")

ps = [(2, 4), (-1, 7), (4, 5), (3, -4), (-1, -5)]
got = operator.itemgetter(0, 2, 3)(ps)
print(got, " доступ к нескольким элементам из списка")


def dist(x):
    return (x[0] ** 2 + x[1] ** 2) ** 0.5

ps = [(2, 4), (-1, 7), (4, 5), (3, -4), (-1, -5)]
filtered = list(filter(lambda x: dist(x) > 6.0, ps))
print(filtered)
seq = ['s', 'j', 'p', 'r', 'q']  # присваиваем ОБ списка № или индекс, start=0 - стартовое число №

for i, val in enumerate(seq, start=0):
  print(f'№ {i} => {val}')



seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))

# можно указать с какой цифры начинать считать
print(list(enumerate(seasons, start=1)))

#  функция enumerate() с указанием начального индекса
names = ["John", "Jane", "Doe"]
enumNames = enumerate(names, 10)
print(list(enumNames), " enumerate() с указанием начального индекса")

names = ["Piter", "Roy", "Clara"]
enumNames = enumerate(names, 1)
for item in enumNames:
    print(item, " item")




# initialize list
test_list = [["g", "f", "g"], ["i", "s"], ["b", "e", "s"]]

# printing original list
print("The original list : " + str(test_list))

res = set() # в примере тут был res = [] но я заменил на set() тк нужно было множество
for sublist in test_list:
    # print(sublist)
    res.add(''.join(sublist))
    print(str(res))
# printing result
print("The String of list is : " + str(res), " преобразование списка списков со строчными ОБ в множество строчных ОБ")
#This code is contributed by Vinay Pinjala.

# Поиндексные действия со списками

a = [100, 200, 300]
b = [10, 20, 30]

print([ a[ind] - b[ind] for ind, _ in enumerate(a)], " Поиндексные действия со списками ")


# INDEX OUT RANGE избегаем выхода индекса за пределы списка, ограничиваем генерацию enumerate

s = [[1000, 1], [5, 80], [1, 200], [200, 1], [65, 21], [11, 73], [13, 72]]
print([s[k] if sum(s[k]) < sum(s[k + 1]) else None for k, _ in enumerate(s[:-1])], " ограничиваем генерацию enumerate "
                                                                                   "игнорируя последнее значение "
                                                                                   "enumerate(s[:-1])")

# Операции между LIST и LIST[LIST], умножить ОБ из y_  на ОБ из LIST[LIST] поиндексно

x_ = [[1, 49, 4, 0], [1, 41, 6, 1], [1, 40, 2, 0]]
y_ = [0.5, 0.5, 0.5, 0.5]
print(list(map(lambda enum_and_y, data: [d * y_[enum_and_y[0]] for d in data], enumerate(y_), x_)),
       " Разный LEN() у LIST и LIST[LIST] и Операции между LIST и LIST[LIST] с разным LEN()")


# TODO Разбить два списка разной длины с последующим их совмещением
step = 6
a = list('AB')
b = [_ for _ in range(12)]

for n, row in enumerate(range(0, len(b), step)):  # row - индекс начала каждого нового отрезка
    print(a[n], b[row: row + step])
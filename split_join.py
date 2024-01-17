
# split() - преобразует строку в список разделённую на отд., слова (sep= ) или список где целиком строка

s = 'Welcome, to, the, python, world' # строка с запятыми и с пробелами
name = s[10:]
print(name)
A1 = s.split()
print(A1)

# split() - делит по умолчанию по пробелам если их нет то по запятым
print(s.split())



d = 'Welcome,to,the,python,world' # строка с запятыми и без пробелов

print(d.split(), 'split() - делит по умолчанию по пробелам если их нет,то в списке будет целиком строка,одно значение')

print(d.split(sep=','), '  sep="," - доп параметр который указывает по какому символу делить строку ')



b = 'Welcome to the python world' # строка  с пробелами без запятых

print(b.split(sep=','), ' если sep="," по запятой а в строке её нет то в списке будет целиком строка')


# maxsplit=1 указывает сколько раз будет разделена строка
print(d.split(sep=',', maxsplit=1), ' maxsplit=1 указывает сколько раз будет разделена строка')

# Объединение списка
names = ['Java', 'Python', ' delimiterrrrr']
delimiter = ','
single_str = delimiter.join(names)
print(single_str, " Объединение списка delimiter.join(names)")


# преобразование списка из 1й строки в список строчных объектов по указанному разделителю
# по умолчанию по запятой.
c = ['asdf, poiu, poiu, dfghrtyu, rtyu, asdfpoiu, asdf, asdf, qwert, rewq, asdf, asdddd']

print("".join(c).split(), " преобразование списка из 1й строки в список строчных объектов ")


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

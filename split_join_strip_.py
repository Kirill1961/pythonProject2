
# split() - преобразует строку в список разделённую на отд., слова (sep= ) или список где целиком строка

s = 'Welcome, to, the, python, world' # строка с запятыми и с пробелами
name = s[5:]
print(name, " -  вывод строки по индексу")
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
print(single_str, " Объединение списка delimiter.join(names)", "\n")


# преобразование списка из 1й строки в список строчных объектов по указанному разделителю
# по умолчанию по запятой.
c = ['asdf, poiu, poiu, dfghrtyu, rtyu, asdfpoiu, asdf, asdf, qwert, rewq, asdf, asdddd']

print("".join(c).split(), " преобразование списка из 1й строки в список строчных объектов ", "\n")


# initialize list
test_list = [["g", "f", "g"], ["i", "s"], ["b", "e", "s"]]

# printing original list
print("The original list : " + str(test_list), "\n")

res = set() # в примере тут был res = [] но я заменил на set() тк нужно было множество
for sublist in test_list:
    # print(sublist)
    res.add(''.join(sublist))
    print(str(res), "Преобразование list[list[str]] в set[str]","\n")
# printing result
print("The String of list is : " + str(res), " преобразование списка списков со строчными ОБ в множество строчных ОБ", "\n")
# This code is contributed by Vinay Pinjala.

# strip - удаляет при выводе 1-й и последний символ, если в арг не указать ничего
a = "\n, asdf, poiu, poiu, dfghrtyu, rtyu, asdfpoiu, \n, 1"
print(a.strip(", \n 1 "), "- strip  удаляет при выводе 1-й и последний символ, если в арг не указать ничего", "\n")


# Замена скобок на кавычки Преобразование list[list[str]] в list[str]
p = [['Storm', 'Java', 'pandas', 'MongoDB', 'data science'], ['HBase', 'Storm', 'Java', 'pandas']]
print([",".join(i) for i in p], "Преобразование list[list[str]] в list[str]", "\n")



# replace - замена подстроки в строке на другую побстроку
text = "JavaScript is awesome and JavaScript is easy to learn"
new_text = text.replace("JavaScript", "Python",  2) # 1й арг - что меняем, 2й арг - на что меняем, 2 - кол-во замен
print(new_text, "replace - замена подстроки в строке на другую побстроку", "\n")


# Просто разбить строку на буквы с помощью List
a = "asdfpoiupoiudfg"
print(list(a), "Просто разбить строку на буквы с помощью  List", "\n")


# Таблица в Питоне
st = "asdf" + "\n" + "\n".join("1") + "\n".join("2") + "\n".join("3") + "\n".join("4")
sd = "asdf" + "\n" + "\n".join("1234")
print(st,  "Таблица в Питоне", "\n")
print(sd,  "Таблица в Питоне", "\n")

print("qwer", "asdf", "zxcv", "Используем sep=", sep="\n")
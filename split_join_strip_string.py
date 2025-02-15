import glob
from itertools import permutations as prm
from collections import Counter

# split() - преобразует строку в список разделённую на отд., слова (sep= ) или список где целиком строка

s = 'Welcome, to, the, python, world' # строка с запятыми и с пробелами
name = s[5:]
print(name, " -  вывод строки по индексу")
A1 = s.split("\n")
print(A1, "...................")

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

a_ = 'i  qwer   x'
print(a_.strip("x i"), " -> Что бы удалить буквы и пробелы указываем их в аргументе в ЛЮБОЙ последовательности", "\n")

# Замена скобок на кавычки Преобразование list[list[str]] в list[str]
p = [['Storm', 'Java', 'pandas', 'MongoDB', 'data science'], ['HBase', 'Storm', 'Java', 'pandas']]
print([",".join(i) for i in p], "Преобразование list[list[str]] в list[str]", "\n")



# replace - замена подстроки в строке на другую побстроку
text = "JavaScript is awesome and JavaScript is easy to learn"
new_text = text.replace("JavaScript", "Python")  # 1й арг - что меняем, 2й арг - на что меняем, 2 - кол-во замен
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


str = "Name {}, Old {}, weigh {}"
name = "Kirill"
old = "51"
weigh = "80"
res = str.format(name, old, weigh)
print(res, " -> Фу-ция format")
str_ = "Name {0}, Old {1}, weigh {2}"
print(str_.format(name, old, weigh), " -> Тоже самое с индексами")

# варианты использования формат
print(" Это число : {0:.2f}".format(2.7418241824), "варианты использования формат")
print(" Это число : {1:.2f}".format(2.7418241824, 3.1487962), "варианты использования формат", "\n")


# Преобразование строки - Заглавные, все большие, все маленькие
str = "QWerty, Asdfg, ZXCV"
print(str.capitalize(), " -> Преобразование строки - Заглавные")
print(str.upper(), " -> Преобразование строки - все большие")
print(str.lower(), " -> Преобразование строки - все маленькие", "\n")


# islower() / isupper() - Прверка регистра
str = "QWER, ASDF ,ZXCV"
print(str.isupper(), " - > islower() / isupper() - Прверка регистра")
print(str.islower(), " - > islower() / isupper() - Прверка регистра", "\n")

# endswith / startswith - Проверка символов начала и конца предлжения
s1 = "Qwer, asdf, zxcv ?"
s2 = "!qwer, asdf, zxcv"
print(s1.endswith("?"), " ->  endswith  - Проверка символов конца предлжения")
print(s2.endswith("?"), " ->  endswith  - Проверка символов конца предлжения")
print(s2.startswith("!"),  " -> startswith - Проверка символов начала предлжения", "\n")


# find - Наличие подстроки
s3 = "В некотором царстве в некотором государстве"
print(s3.find("царстве"), " -> find - Наличие подстроки - 'царстве'", "\n")
print(s3[5:10], " -> вытаскиваем по индексу с 5 по 10 символ ", "\n")


# replace - Замена подстроки старое на новое
s4 = "В некотором,  царстве в некотором, государстве"
print(s4.replace(",", "."), " - > Замена подстроки старое ',' на новое '.'")
print(s4.replace("В некотором, ", "В тридевятом, ", 2), " - > Замена подстроки старое 'В некотором,' "
                                                     "на новое 'В тридевятом,.'", "\n")


# Таблица умножения
for i in range(1, 11):    # отвечает за строки
    for j in range(1, 11):  # отвечает за результат умножения в столбах
        print(f"{i * j:3}", end=" ")  # j:3 - "3" это расстояние меж столбами
    print()               # перенос строки "i" по окончании итерации от 1 до 10


# Таблица умножения с нумерацией
print(" ", end="")     # начало нумерации колонок
for k in range(1, 11):  # нумерация колонок
    print(f"{k:>4}", end="") # форматирует номер столбца с выравниванием вправо на 4 символа.
print()                  # перенос строки нум колонок
for i in range(1, 11):
    print(i, end="")     # нумерация строк
    for j in range(1, 11):
        print(f"{i * j:>4}", end="")  # res умножения, j:>4 выводит значение таблицы с выравниванием вправо на 4 символа.
    print("")               # перенос строк res умножения

# Удаляем крайние символы и пустые строки
lst = [
    '\n',
    'THE FREE BONUSES ALONE ARE WORTH ACTING NOW! \n ',
    'THE CABLE DESCRAMBLER KIT COMES WITH A THIRTY DAY \n',
    'MONEY BACK GUARANTEE! IF YOUR NOT COMPLETELY SATISFIED,\n',
    'SEND THE CABLE DESCRAMBLER KIT BACK AND YOU KEEP \n',
    'THE BONUSES FOR FREE. YOU HAVE NOTHING TO LOSE!! \n',
    '\n',
    '\n',
    '\n',
]
# Крутим строки из rows, strip() удаляет по умолчанию крайние символы, if row != '\n' - фильтрует пустые строки
cleaned_lst = [s.strip() for s in lst if s != '\n']
print(cleaned_lst, "удаляем мусор")
# Крутим строки из rows, strip() удаляет по умолчанию крайние символы, if s.strip() удаляет '\n' тк всё край-ие исмво-лы
cleaned_lst1 = [s.strip() for s in lst if s.strip()]
print(cleaned_lst1, "удаляем мусор", "\n")

# Чтение и запись файла в одном блоке кода
inpfr = glob.glob(rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\13.txt")[0]
inpfw = glob.glob(rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\23.txt")[0]
with open(inpfr, "r", encoding="cp1251") as fr:
    rows = fr.readlines()
    rows_fr = [
        f"{enum} : " + row for enum, row in enumerate(rows, start=1)  # добавка к строке нумерации при чтении
    ]
    print(rows_fr)
    with open(inpfw, "w", encoding="cp1251") as fw:
        [fw.write(f" № {row.strip()}") for row in rows_fr]  # добавка к строке нумерации при записи
    with open(inpfw, "r", encoding="cp1251") as wr:
        write = wr.readlines()
        print(write)


# Удаление части строки с  split()

s = "qwerty"
index = s.find('qw')
if index != -1:
    result = s[:index]
else:
    result = s
print(result)  # Output:


s = "qwerty"
result = s.split('qw')[0] + 'qw'
print(result)  # Output: qw


# splitlines()  разделениет строки на список строк, по символам новой строки (например, \n, \r\n и т. д.).
text = """Hello, world!
This is a test.
Python is awesome!"""

lines = text.splitlines()
print(lines)

#  использование методов is....... (isalpha, isnumeric, isalnum и тд)
n = "Kirill1971Sh"
print("".join(list(filter(lambda x: x.isnumeric(), n))), '\n')


#  Все варианты перестановок символов строки
string = 'abcd'

# Вывод групп с комбинациями равных размеру строки
string_perm = list(prm(string))


# Длина слов после очистки
res_len = [len(i.strip('. , ')) for i in s.split()]
print(res_len, 'Длина слов после очистки')

# Вывод групп с комбинациями ограниченного размера len(string_perm_limit)=2
string_perm_limit = list(prm(string, r=2))


print([''.join(row) for row in string_perm], '\n')

print([''.join(row) for row in string_perm_limit])

# Субстрока заданной длинны
def longest_substring_vs_k_limit(s):
    start = 0
    for i, j in enumerate(s):
        sub_string = s[start: i + 1]
        print(len(sub_string), dict(Counter(sub_string)))
        if len(sub_string) >= 3:
            start += 1

    return len(sub_string), dict(Counter(sub_string))

longest_substring_vs_k_limit('aacidfgrrty')


# Убираем запятые пробелы точки, оставляем одни слова

s = 'Hi all, my... name.'

res = [(i.strip('. , ')) for i in s.split()]
print(res,  'Убираем запятые пробелы точки, оставляем одни слова')


# Для заданного предложения вернуть среднюю длину слова
__doc__ = '''MY'''

s1 = "Hi all, my name is Tom...I am originally from Australia."
s2 = "I need to work very hard to learn more about algorithms in Python!"
s = 'Hi all, my... name.'

def avereg_lenght_word(str):
    clean_word = [i.strip("!?',;.") for i in str.split()]
    lenght_words = map(len, clean_word)
    lenght_list = len(list(lenght_words))
    lenght_total = sum(map(len, clean_word))
    avereg_lenght = lenght_total / lenght_list
    print(clean_word)
    print(lenght_list)
    print(lenght_total)
    return avereg_lenght
print(avereg_lenght_word(s))


__doc__ = '''Eduson'''

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def solution(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')

    words = sentence.split()
    print(words)
    print([len(word) for word in words])
    print(sum([len(word) for word in words]),len(words))
    return round(sum(len(word) for word in words)/len(words),2)

solution(sentence1)

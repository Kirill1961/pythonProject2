""" sorted() возвращает новый отсортированный список итерируемого объекта
(списка, словаря, кортежа). По умолчанию она сортирует его по возрастанию."""

"""   Возвращаемое значение — List (список).
    Синтаксис: sorted(iterable,key=None,reverse=False).
    iterable - строка, список, кортеж, множество, словарь
    key - (необязательный параметр): если указать ключ, то сортировка будет выполнена по функции этого ключа.
    reverse - (необязательный параметр): по умолчанию сортировка выполняется по возрастанию.
    Если указать reverse=True, то можно отсортировать по убыванию."""

# Параметр key - объект можно также отсортировать по функции, указанной в параметре key

""" Моя сортировочка"""

# Значения из списка " р " передаются в аргумент " х " ф-ции lambda
p = [-5, 1, 3, 10]
p_sorted = sorted(p, key=lambda x: x * -2)  # Если задана ключевая функция
# , примените ее один раз к каждому элементу списка и отсортируйте их,

print(p_sorted, ' список " р " сортируется с учётом умножения на -2')
# То же самое + реверс
p_sorted = sorted(p, key=lambda x: x * -2, reverse=True)
print(p_sorted, " То же самое + реверс")


# Сортировка словаря на основе функции len
l1 = {"carrot": "vegetable", "red": "color", "apple": "fruit"}
# Возвращает список ключей, отсортированных по функции len
print(sorted(l1, key=len), "по функции len 1")


# Возвращает список значений, отсортированных на основе функции len
print(sorted(l1.values(), key=len), "по функции len 2")


# Сортировка списка на основе функции len
l1 = ["blue", "green", "red", "orange"]
print(sorted(l1, key=len), "по функции len 3")


# Сортировка списка по абсолютному значению
l1 = [1, -4, 5, -7, 9, 2]
print(sorted(l1, key=abs), "по абсолютному значению")


s1 = "Hello How are you"

# Разбивает строку и сортирует по словам
print(sorted(s1.split()), "сортирует по словам")


# Разбивает строку и сортирует после применения str.lower ко всем элементам
print(sorted(s1.split(), key=str.upper), "str.upper  - безучёта регистра")


d1 = {"apple": 1, "Banana": 2, "Pears": 3}
# Возвращает список ключей, отсортированный по значениям
print(sorted(d1), "список ключей 1")

# Возвращает список ключей, отсортированный после применения str.lower ко всем элементам
print(sorted(d1, key=str.lower), "список ключей , str.lower - безучёта регистра")


# напишем функцию для получения второго элемента
def sort_key(e):
    return e[1]


l1 = [(1, 2, 3), (2, 1, 3), (11, 4, 2), (9, 1, 3)]
# По умолчанию сортировка выполняется по первому элементу
print(sorted(l1), " сортировка по 1му элементу")


# Сортировка по второму элементу с помощью функции sort_key
print(sorted(l1, key=sort_key), " сортировка по 2му элементу")


# sort списка кортежей по вторым элементам кортежей
tup = [(2, 2), (17, 89), (142, 17), (51, 14), (-1, 51), (14, -1), (89, 142)]
tup.sort(key=lambda row: row[1])
print(tup, " sort списка кортежей по вторым элементам кортежей")


# sort() - Сортировка по определенному полю в словарях
# sort() - возвращает изменёную исходную структуру
students = [
    {'name': 'Alice', 'grade': 90},
    {'name': 'Bob', 'grade': 82},
    {'name': 'Charlie', 'grade': 95}
]
students.sort(key=lambda x: x['grade'])
print(students, "sort() - Сортировка по определенному полю в словарях")

# sorted() - Сортировка по  полю
# sorted() - возвращает новую структуру
students = [
    {'name': 'Alice', 'grade': 90},
    {'name': 'Bob', 'grade': 82},
    {'name': 'Charlie', 'grade': 95}
]
sort_stud = sorted(students, key=lambda x: x['grade'])
print(sort_stud, "sorted() - Сортировка по определенному полю в словарях")

# Определение самого длинного слово с выводом max len и слов с max len
doc = ("That's an important role in everything from traditional computer science it comes"
       " close to providing one stop shopping for most statistical work ")
doc_fram = doc.strip(" ").split(" ")
doc_fram_sort = sorted(doc_fram, key=len)
max_len = len(doc_fram_sort[-1])
print(f"max len = {max_len}")
for word in doc_fram:
  if len(word) == max_len:
    print(f"word have max lenght : {word}")


alphabet = [chr(i) for i in range(97, 123)]
print(alphabet)
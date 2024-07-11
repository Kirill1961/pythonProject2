"""  __________________WHILE_________________________"""

""" Вариант остановки цикла с помощью условия прописанного в цикле while"""

a = 1
while a < 4:
    print('Цикл выполнился', a, 'раз(а)')
    a = a + 1
print('Цикл окончен')

index = 0
while index < 5:
    print(index, 'index принт в теле цикла')
    index += 1
print(index, 'index принт в конце цикла')

""" Вариант остановки цикла по условию с помощью return"""

a = [1, 2, 3, 4, 5]


def w():
    while a:
        if len(a) > 3:
            print('ok')
        return a


print(w(), '**************')

"""  ___________Else в цикле while______________
    В этом случае блок в else исполняется, когда условие цикла становится ложным."""
b = 1

while b < 5:
    print('условие верно')
    b = b + 1
    print(b)
else:
    print('условие неверно')

""" ______________Прерывания цикла while с помощью Break _________________
    Break — ключевое слово break прерывает цикл и передает управление в конец цикла"""

a = 1
while a < 5:
    a += 1
    if a == 3:
        break
    print('break')  # 2

""" ______________Прерывания цикла while с помощью Continue _________________
    Continue — ключевое слово continue прерывает текущую итерацию и передает 
    управление в начало цикла, после чего условие снова проверяется. 
    Если оно истинно, исполняется следующая итерация."""

a = 1

while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)  # вывод 2, 4, 5
""" ________________Вариации с " is not  None "__________________"""

l = [0, 1, 2, 3, 4]
l1 = []


def whle():
    while l is not None:
        l1.append(l.pop())
        if len(l1) == 3:
            return l1


print(whle())

l = [0, 1, 2, 3, 4]
l1 = []


def whle():
    while l is not None:
        l1.append(l.pop())
        if len(l1) == 4:
            break
    print(l1)


whle()

""" более сложные, составные условия. Они могут быть сколь угодно длинными, 
    а в их записи используются логические операторы (not, and, or):"""
dayoff = False
sunrise = 6
sunset = 18

worktime = 12

# пример составного условия
while not dayoff and sunrise <= worktime <= sunset:
    if sunset == worktime:
        print("Finally it's over!")
    else:
        print('You have ', sunset - worktime, ' hours to work')
    worktime += 1

list = [10, 20, 30]


# def defineAList():
#     list = ['1','2','3']
#     print ("For checking purposes: in defineAList, list is",list)
#     return list

def useTheList(*args, **kwargs):
    print("For checking purposes: in useTheList, list is", *args, **kwargs)


# def main():
#     # defineAList()
#     useTheList(list)
#
# main()
useTheList(list)


def laz(n):
    i = 0
    while i < n:
        yield i
        i += 1


fg = [k for k in laz(100)]
print(fg)


# Цикл в Цикле

def out():
    m = 0
    while m < 2:  # число повторов  while n < 10
        m += 1
        n = 0
        while n < 10:
            n += 1
            print(n, " Цикл в Цикле ")


out()

"""while True: -  бесконечный цикл
   while False: или пустой  list()  или  пустая  str() - цикл ни когда неначнётся"""

# Если поместить условие бесконечного цикла True в переменную, а затем изменить её на False, то цикл остановится
condition = True
x = 0
while condition:  # Цикл идёт пока condition = True
    print(x)
    x += 1
    if x == 3:
        condition = False
        print(x, "condition = True, при х = 3 condition = False")

# Пока список b непустой цикл работает
b = [[1, 2], [3, 4], [5, 6]]
while b:
    b.pop()
    print(b, "Пока список b непустой цикл работает")

x = 0
while True:  # True - бесконечный цикл
    print(x)
    x += 1
    if x == 3:
        break

    print(x, "True в условии, останов по break")


# while - коллекции или строки, останов по длинне коллекции
s = "qwert"
index = 0
length = len(s)

while index < length:
    print(s[index])
    index += 1

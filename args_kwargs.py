*a, b, c = [2, 34, 'ok', 45]
print(a, b, c)

print(set(range(1, 5)), ' set(range(1, 5)')

d = (10, 20)
print(set(range(*d)), '  *d*d*d*d*d')  # распаковываем аргументы для range


def star(a, b, c, d):
    p = [a, b, c, d]
    return p


ar = ['tro lo lo ', 12, True, [7, 8, 9]]
print(star(*ar))  # распаковывем список ar для передачи в ф-цию star, ко-во аргументов должно совпадать

""" _________Вариант без переменных только ar___________"""


def star(*ar):
    p = [ar]
    return p


ar = ['tro lo lo ', 12, True, [7, 8, 9]]
print(star(*ar))  # распаковывем список ar для передачи в ф-цию star, ко-во аргументов должно совпадать


def star1(*args):
    print(args, type(args))


star1(44, 55, 77, 99)

"""_________________Намудрил передачу аргументов со звездой______________"""


def count_out1(start=0):  # Переменная start  в глобальной обл видимости и не стирается при повторных вызовах cl и cl2
    def count_inner1(*args):
        nonlocal start  # nonlocal для того что бы не создавать в локальной обл. а пользоваться перемен из глобальн.обл
        start += 1
        f = sum(args) + start
        return f

    return count_inner1


j = [3, 4, 5, 9, 68, 1003]
cl = count_out1(5)
cl2 = count_out1()
print(cl(*j), cl2(*j))  # Распаковали список j, и -> в count_inner1() через *args -> в sum(args) -> вернули f = sum()


# когда две ф -ции работают в связке с разным кол-вом аргументов
# , то  для ф-ции с меньшим кол-вом арг используем *args

a, b, x, y = 5, 2, 10, 50


def pred(*args):
    print(*args, " аргументы из *args")
    return a * x + b

def devi(x, y, a, b):
    return y - pred(x, y, a, b)


print(devi(10, 50, 5, 2), " две ф -ции работают в связке с разным кол-вом аргументов")
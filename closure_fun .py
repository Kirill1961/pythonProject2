# Просто вложенная ф-ция inner()
def outer(name):
    def inner():
        print('good pogrammerrrrr  -  ' + name)

    inner()


outer('Kirill')

""" Замыкание ф-ции происходит так :
    переменная (name) находится в глобальной области  ф-ции outer и не стирается после выполнения ф-ции inner
    глоб переменная close -> вызывает ф-ю outer(name) -> ссылается на влож ф-ю inner(nname) -> return inner возвращает
    в close(' and Kirill') -> print, таким обр ф-я  inner(f) использовала переменную name не объявленную в её теле"""


def outer(name):
    def inner(f):
        print('good pppppogrammer  -  ' + name + f, " >>>>>>>>>>>>>>>>>>>")

    return inner


close = outer('Kirill')
close(' and Kirill')  # Переменная close вызывает ф-ю inner() через outer(name) и по факту является ф-й inner()

""" Независимые счётчики res(20) и res(1000)"""


def count_out(n):
    def count_in(b):
        b += 1
        # print(b+n)
        return b + n

    return count_in


res = count_out(5)
print(res(20), '  res(20)')  # фактически это ф-ция count_in(b)
print(res(1000), '  res(1000)')  # и это фактически ф-ция count_in(b) но с др аргументом

""" Замыкани и список"""


def avarege():
    list = []

    def inner(val):
        list.append(val)
        res = sum(list) / len(list)
        return res

    return inner


s = avarege()
print(s(8), s(6), s(4))

""" _________________Счётчики__________________  """


def count_out1(start=0):  # Переменная start  в глобальной обл видимости и не стирается при повторных вызовах cl и cl2
    def count_inner1(n):
        nonlocal start  # nonlocal для того что бы не создавать в локалььной обл а пользоваться перемен из глобальной О
        start += 1

        return start ** n

    return count_inner1


cl = count_out1(1)
cl2 = count_out1()
print(cl(2), cl2(2))
print(cl(2), cl2(2))
print(cl(2), cl2(0))

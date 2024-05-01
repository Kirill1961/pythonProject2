from functools import wraps


def g(f):  # g(f) - сюда передали адрес ячейки ф-ции р(с)
    def l(x):  # сюда передали адрес ячейки аргумента ф-ции р(с)
        print(x ** 2, "before")
        f(x)  # обратились к ячейкам ф-ции и аргумента
        print(x ** 2, "after")
        return x ** 3  # возвращаем res ф-ции l(x)

    return l  # возвращаем ячейку ф-ции l


@g  # этот декоратор передаёт ф-цию р(с) в аргумент ф-ции g(f)
def p(c):  # Вызов p(c) активизирует декоратор @g который передаёт адреса ячеек ф-ции p() и её аргумента c в g(f) и l(x)
    print(c ** 2)


print(p(2), " печать вызова", "\n")

print(" Структура декоратора c @", "\n")


def a(x):
    def c(y):
        print("a")
        x(y)
        return x

    return c


@a
def b(z):
    print(z)
    return z


b("NN")  # Вызов b(z) активизирует декоратор @a который передаёт адреса ячеек ф-ции b() и её аргумента z в a(x) и в c(y)

print(" Структура декоратора с декорированием через переменную", "\n")


def a(u):
    def c(y):
        print("a")
        u(y)
        return u

    return c


af = a(b)  # af = a(b) Играет роль декоратора
af("MM")    # передача аргумента декорируемой ф-ции b(z)


def b(z):
    print(z)

print(" Структура декоратора c переменной", "\n")

# print(g(p(2)))


def f_d(fun):
    def wr(x):
        print('befor')
        fun(x)  # тело ф-ции s_f(x)
        print(x, " xxxxxx")
        print('after', "\n")
        # return x

    return wr  # возврат результ ф-ции wr


@f_d
def s_f(x):
    print(f'{x}', " 1-й заброс в декоратор'")


f_d(s_f(" OK NO OK NO"))
# f = f_d(s_f)
# f('ok / no')
# print(f('ok / no'),   ">>>>>>>>>>>>", "\n")

# def aa(ff):

#     def bb():
#         ff()
#         x = 1
#         print(x + 1)

#     return bb


# def cc():
#     print('jj')


# fuf = aa(cc)
# fuf()

#
# def dr(fr):
#     def de(r, g):
#         print('OK')
#         return fr(r, g)
#
#     return de
#
#
# def mn(r, g):
#     return r + g
#
#
# f = dr(mn)
# print(type(f))
# print(f(3, 6))
#
#
# # """ Функция как аргумент другой функции"""
#
# def m_n(nm):
#     return f'hi,{nm}'
#
#
# def m_p(nm):
#     return f'good,{nm},togethe'
#
#
# def m_l(gf):
#     # gf ='john'
#     return gf('john')


# print(m_l(m_n), m_l(m_p))

# """ Встроенные функции """

# def m_ll():
#     print('m_ll')


#     def m_pp():
#         print('m_pp')


#     def m_nn():
#         print('m_nn')
#     m_pp(),m_nn()
# m_ll()


# def ff(x,y):
#     return x / y
# a = 3
# b = 5
# print(ff(b,a))

# def apl (func, val):
#     return func(val)
# print(apl)

""" @wraps  сохраняет документацию и имя декорируемой ф-ции
тк при передаче декорируемой ф-ции в качестве аргумента имя декорируемой 
ф-ции меняется на имя вложенной ф-ции inner, что бы того не произошло 
используем @wraps из класса functools для сохранения имени и документации  """


def outer(fu_nc):
    """ decorator """

    @wraps(fu_nc)
    def inner(*args, **kwargs):
        print('six/' * 3)
        return fu_nc(*args, **kwargs)

    return inner


def outer_2(func):
    @wraps(func)
    def inner_1(*args, **kwargs):
        print('V' * 10)
        return func(*args, **kwargs)

    return inner_1


def my_func(a, c):
    return a * c


my_fu = outer(my_func)

print(my_fu(2, 3))


def oter(func):
    def inr(*x):
        for y in x:
            func()
            print(f'{y}')

        return x

    return inr


def work():
    print('num = ', end='')


f = oter(work)
print('nums = ', f(10, 100, 1000))


def oter(func):
    def inr(*x):  # ф-ция inr(*x) - через декоратор @oter становится ф-цией work(v)
        s = [func(x)]
        for i in s:
            print(i, ":-( кортеж;")
        for y in x:
            # func(x)
            print(y * 7)
            # print(f'{y}')

        return x

    return inr


@oter  # принадлежность к аргументу функции @oter
def work(v):  # ф-ция work(v) аргумент ф-ции oter(func)
    # v = 'nums or '
    # print(v + 'num = ', " >>>>>>>>>> @oter ", end='')
    value = [v]  # v - аргумент ф-ции work(v)


f = oter(work)  # ф-ция work(v) аргумент ф-ции oter(func)
wf = work
# wf(50, 500, 5000)
f(10, 100, 1000)  # все эти аргументы передаются в inr(*x)
wf(50, 500, 5000, "Y")  # все эти аргументы передаются в inr(*x)

# df = print(work(10, 100, 1000, ' 2й вариант с @oter'))  # все эти аргументы передаются в inr(*x)
# print(df)

""" _______________Алгоритм Эвклида_____________"""
import time


def oter(func):
    def inr(*args):
        ds = time.time()
        # time.sleep(2)
        nod = func(*args)
        df = time.time()
        dw = df - ds
        print('Time work code  ', dw)
        return nod

    return inr


def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


f = oter(get_nod)
print(f(70, 84), 'наибольший ОД')


# ф-цию degree(k) через переменную function_from_list закидываем в список res для действий с генерируемой " k "
def degree(k):
    return k ** 2


def make(a, function_from_list):
    res = [function_from_list(k) for k in range(a)]  # каждый цикл res вызывает degree(k), return k**2 возвращает в res
    print(res, ' res res res')


make(5, degree)

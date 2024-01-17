from functools import wraps

def f_d(fun):
    def wr(x):
        print('befor')
        fun(x)
        print(x, " xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print('after')
    return wr
def s_f(x):

    print(f'{x}', " (f'{x}'")
f = f_d(s_f)

f('ok / no')


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
from functools import wraps


def outer(fu_nc):
    """ decorator """

    @wraps(fu_nc)
    def inner(*args, **kwargs):
        print('six/' * 3)
        return fu_nc(*args, **kwargs)

    return inner


def outer_1(func):
    @wraps(func)
    def inner_1(*args, **kwargs):
        print('*' * 10)
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
    def inr(*x):
        for y in x:
            func(x)
            print(f'{y}')

        return x

    return inr


@oter # принадлежность декоратору
def work(v):
    v = 'nums or '
    print(v + 'num = ', " >>>>>>>>>> @oter ", end='')


# f = oter(work)
# print( f(10, 100, 1000))

df = print(work(10, 100, 1000, ' 2й вариант с @oter'))
print(df)



""" _______________Алгоритм Эвклида_____________"""
import time
def oter(func):
    def inr(*args):

        ds = time.time()
        # time.sleep(2)
        nod = func(*args)
        df = time.time()
        dw = df - ds
        print('Time work code  ',  dw)
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

def make(a, function_from_list):
    res = [function_from_list(k) for k in range(a)] # каждый цикл res вызывает degree(k), return k**2 возвращает в res
    print(res, ' res res res')
def degree(k):
    return k**2
make(5, degree)
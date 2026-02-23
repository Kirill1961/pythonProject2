from functools import wraps

def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print(' - have use args ')
    else:
        print('args have not')
myfunc(1,2,3,4,1,'oj')





from decor_func import *   # Импортироуем из decor_func нужные ф-ции через декор




@outer       # принадлежность к ф-ции outer
@outer_2     # принадлежность к ф-ции outer_2
@outer
def my_func(a,c):
    return print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
# @outer_1
# def try_():
#     return '- this is six'
# my_func= outer(my_func)
print(my_func(2,3))



# Lexer GPT / MY
"""
Декоратор @...  делает так:
sql("import qwer comment include delete -- asdf") == func_wrapper(code)
если декоратор навешан то при вызове sql тело sql заменяется на тело обёртки, и аргумент переходит в переменную обёртки
"""
def func_decor(func):  # язык в аргументе внешней ф-ции
    def func_wrapper(code):  # код в аргументе внутренней ф-ции

        deleter = func()
        if isinstance(deleter, tuple):

            for command in deleter:
                code = code.replace(command, "")

            return f" {func.__name__} : {code}"

        else:
            if deleter in code:
                code = code.replace(deleter, "")
            return f" {func.__name__} : {code}"

    return func_wrapper  # декоратор возвращает обновлённую ф-цию, дальше можно обращаться к ней

@func_decor
def python():
    return "import", "delete"


@func_decor
def sql():
    return "--", "comment"


@func_decor
def c_plus_plus():
    return "include"


# запуск декоратора через вызов декорируемой ф-ции с навешенным @func_decor
print(python("import qwer comment include delete -- asdf"))
print(sql("import qwer comment include delete -- asdf"))
print(c_plus_plus("import qwer comment include delete -- asdf"))



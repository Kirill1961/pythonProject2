# def myfunc(*args):
#     for a in args:
#         print(a, end=' ')
#     if args:
#         print(' - have use args ')
#     else:
#         print('args have not')
# myfunc(1,2,3,4,1,'oj')
from decor_func import *

@outer
@outer_1
@outer
def my_func(a,c):
    return a * c
# @outer_1
# def try_():
#     return '- this is six'
# my_func= outer(my_func)
print(my_func(2,3))
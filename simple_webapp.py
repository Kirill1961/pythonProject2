import string
from typing import Type

from _ctypes_test import func
from flask import Flask, session
# from checker import check_logged_in, good_programmer
from checker import *
from functools import wraps

app = Flask(__name__)


# def good_programmer(fun):
#     @wraps(fun)
#     def wrapper_good_programmer(*args, **kwargs) -> object:
#         return 'good_programmer'
#
#     return wrapper_good_programmer
#
#

#
#
# def check_logged_in(fun):
#     @wraps(fun)
#     def wrapper(*args, **kwargs):
#         return 'check_logged_in'
#
#     return wrapper


#
# def merge_decor(fun):
#     return ch(gd(ch))


# def out(fun: object) -> object:
#     def wra(*args, **kwargs):
#         print('*' * 10)
#         return fun(*args, **kwargs)
#
#     return wra


# @good_programmer
# @check_logged_in
# def pro_decor(x):
#     return x ** 2
#
#
# print(pro_decor(10))

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'


@app.route('/page1')
# @good_programmer
@check_logged_in
@good_programmer
# @merge_decor
def page1(x) -> Type[str]:
    # def wrap_pag():
    #     return 'Page 2'

    return x,y


# @app.route('/page2')
# @check_logged_in
# def page2() -> str:
#     return 'This page2'
#
#
# @app.route('/page3')
# @check_logged_in
# def page3() -> str:
#     return 'This page3'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


#
#
@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


app.secret_key = 'YoNi'

if __name__ == '__main__':
    app.run(debug=True)

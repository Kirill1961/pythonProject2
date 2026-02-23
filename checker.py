from flask import Flask, session
from functools import wraps

""" @wraps  сохраняет документацию и имя декорируемой ф-ции
тк при передаче декорируемой ф-ции в качестве аргумента имя декорируемой 
ф-ции меняется на имя вложенной ф-ции inner, что бы того не произошло 
используем @wraps из класса functools для сохранения имени и документации  """
# app = Flask(__name__)


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args):
        print('check_logged_in')
        # if 'logged_in' in session:
        return func('check')
        # return 'You are not logged in'

    return wrapper


def good_programmer(func):
    @wraps(func)
    def wrapper_good_programmer(*args):
        print('wrapper_good_programmer')
        return func('wrapper_good_programmer''ok')

    return wrapper_good_programmer


def merge_decor(func):

    return check_logged_in (good_programmer(func))

# if 'logged_in' in session:
#     return func(*args, **kwargs)

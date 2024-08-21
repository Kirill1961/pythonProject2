"""
eval() подходит для выполнения простых выражений и возвращает результат.
exec() подходит для выполнения сложных блоков кода, не возвращая результат напрямую.
"""
import random
x = 10
result = eval('x + 5')
print(result)  # Выведет 15


code = '''
def greet(name):
    return f"Hello, {name}!"
result = greet('Alice')
print(result)
'''

exec(code)  # Выведет "Hello, Alice!"


code = ("""
p = [random.randrange(1, 20, 3) for _ in range(5)]
print(p)
""")

exec(code)

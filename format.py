num = 42
str_num = ("{}".format(num), ' def')
print(str_num)
print(type(str_num))

""" _______________________________f - строка"""
num = 77
string_num = (f"{num}" + 'abc')
print(string_num)
print(type(string_num))

set = {i for i in range(10)}
print(set)

""" _____________________________f - строка"""
set2 = {(f'{k}', 'FormaT' ) for k in set}
print(set2)

price = 46.99
tag = 'is a real bargain'

""" ___________________Кокотенация, с помощью " + " соединяем строчные символы"""

mag = 'AT' + str(price) + ',' +  tag + '-' + 'good programmer'
print(mag)



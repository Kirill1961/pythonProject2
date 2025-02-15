import math as mt
a = [1, 2, 3, 0.5]
b = [0, 2, 7]

# параметр key=  -  для ф-ции  min / max указывает по какому признаку определять min / max
print(min(a, b, key=sum), ' выбор из 2x списков наименьшей суммы', "\n")  #
print(max(a, b, key=sum), ' выбор из 2x списков наибольшей суммы', "\n")  #
print(min(a, key=None),"min значение в списке ", "\n")
print(max(a, b, key=len),"список с мах длинной", "\n")  # определяет max по длинне списка

# min значение в списке
a = [1, 2, 3, 0.5]
print(min(range(len(a)), key=lambda i: a[i]), "min значение в списке, проверка поиндексно", "\n")

#  max определяет МАКС value словаря, но выводит ключи
dict = {1: {"a": 20, "b": 1, "c": 1000, "d": -5},
2: {"a": 555, "b": 10, "c": -33, "d": 77},
3: {"a": 0.01, "b": 17, "c": 0, "d": 840}}

res = [max(x, key=x.get) for x in dict.values()]
print(res, "max определяет МАКС value словаря, но выводит ключи")

# max с аргументом default
# если не найдено число меньше limit то возвращается -1,
nums = [10, 20, 30]
limit = 5
result = max([num for num in nums if num < limit], default=-1)
# Output: -1, потому что все числа в `nums` больше или равны `limit`
print(f"если не найдено число меньше limit то возвращается число {result}")


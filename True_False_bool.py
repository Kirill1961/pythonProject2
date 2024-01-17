a = [2, 51, 14, 142, 17, 89, -1]

print([i for i in a if True], " if True  разрешает итерацию списка")

print([i for i in a if False], " if False  неразрешает итерацию списка")

print([0 if True else 1], " if True в тернарном операторе возвращает 1-е значение ")

print([0 if False else 1], " if False в тернарном операторе возвращает 2-е значение ")

# lambda  определяет заданное число совпадений ОБ

a = 5
b = 5
bo_ol = [a == b for _ in range(5)]
print((bo_ol, " Список из одних True"))
print([i for i in filter(lambda r: not r is False, bo_ol)], " ?? not is False - отрицание наличия False")
print([i for i in filter(lambda r: not r, bo_ol)], " ?? not  - отрицание отсутствия True")
if [i for i in filter(lambda r: not r, bo_ol)] is True:
    print("ok")
else:
    print("no")

# Определяем наличие True / False в словаре оператором IN
# filter передаёт в lambda список bo_ol.
print(True in [r for r in filter(lambda r: r is True, bo_ol)], " фильтруем из списка bo_ol только True")
print(False in [r for r in filter(lambda r: r is True, bo_ol)], " фильтруем из списка bo_ol только False")

# определяем пустой или заполненный список с BOOL
print(bool([i for i in filter(lambda x: x is False, bo_ol)]), " проверка присутствия  False - отсутствует")
print(bool([i for i in filter(lambda x: x is True, bo_ol)]), " проверка присутствия  True - присутствует")


# фильтрация списка содержащего только True по РЕР-8 и мой самопис
quotient = [True, True, True]
if not bool([_ for _ in filter(lambda row: row is False, quotient)]):
    print(" True, по РЕР-8 фильтрация списка содержащего только True")
else:
    print("False, по РЕР-8 фильтрация списка содержащего только True")

if bool([_ for _ in filter(lambda row: row is False, quotient)]) == False:
    print(" True, фильтрация списка содержащего только True, мой самопис")
else:
    print("False, фильтрация списка содержащего только True, мой самопис")




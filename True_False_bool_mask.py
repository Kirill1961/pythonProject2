import numpy as np

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


# Среднее для списка bool, учтём что False=0, True=1
x = [False, False, True, True, True]
mean = sum(x) / len(x)
print(mean, "Среднее для списка bool, учтём что False=0, True=1"
            "")

# Одномерный Массив
arr = np.arange(5, 30, 5)

# Задать маску
mask = [True, False, True, True, False]

print(f"Задать маску {arr}")

# Применение маски к массиву
print(f"Применение маски к массиву {arr[mask]}")

# Применение логического условия к массиву, выбрать элементы больше 10
print(f"Применение логического условия к массиву, выбрать элементы больше 10 {arr[arr>10]}")

# Применение логического условия к массиву
print(f"Применение логического условия к массиву {arr % 2 == 0}")

# Булевская маска на основе условия (элементы больше 2)
print(mask_condition := arr < 20, "Булевская маска на основе условия (элементы больше 2)")

# Увеличить все элементы меньше 15 на 100
arr[arr < 15] += 100
print(f"Увеличить все элементы меньше 15 на 100 {arr}")

# Комплексный фильтр выбрать элементы, которые больше 10 и меньше 25
print(filtered := arr[(arr > 10) & (arr < 25)], "Комплексный фильтр выбрать элементы, которые больше 10 и меньше 25")

# Заменить все отрицательные значения на 0
a = np.array([-1, 2, -3, 4, 5])
a[a < 0] = 0
print(f"Заменить все отрицательные значения на 0 {a}")

# Создать новый массив только с положительными элементами
a = np.array([-5, -3, 0, 2, 4, 5])
positive_a = a[a > 0]
print(f"Создать новый массив только с положительными элементами {positive_a}")

#  Многомерный массив
import numpy as np
b = np.arange(0, 12).reshape(3, 4)

print(b, "\n")

# Маска всего массива однообразная
msk = b >= 0
print(msk, "\n")

# Маска  массива по условию
msk = b > 2
print(msk, "\n")

# Уменьшим на 10 все элементы, которые больше 5
b[b > 5] -= 10
print(b, "\n")
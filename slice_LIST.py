list_slise = [1, 2, 3, 4, 5, 6, 7, 8]

print(list_slise[-2:], " два последних значения")  # два последних значения
print(list_slise[-2], " второе значение с конца")  # второе значение с конца
print(list_slise[:-2], " все кроме 2x последних")  # все кроме 2x последних
print(list_slise[1:-1], " все кроме 1го и  последнего")  # все кроме 1го и  последнего


# СРЕЗЫ
f = [(2, 3, 21), (-14, 10, 2), (1, -5, 17), (-67, 0, 12), (15, 1, 33), (0.5, -9, 77)]
print([i for i in filter(lambda  row:  row, f)][-1:], " СРЕЗЫ последняя кроме всех")
print([i for i in filter(lambda  row:  row, f)][:-1], " СРЕЗЫ все кроме последней")
print([i for i in filter(lambda  row:  row, f)][-4:], " СРЕЗЫ последние 4 значения")
print([i for i in filter(lambda  row:  row, f)][:-2], " СРЕЗЫ все кроме 2x последних")
print([i for i in filter(lambda  row:  row, f)][4:], " СРЕЗЫ все начиная с 5 го индекса")
print([i for i in filter(lambda  row:  row, f)][:2], " СРЕЗЫ все до 2 го индекса включительно")

# вытащить из списка элементы и присвоить их переменным

ls = [10, 20 , 30]
a, b, c = ls[0], ls[1], ls[2]
print(a, b, c, " вытащить из списка элементы и присвоить их переменным")

l = [i for i in ls]
g, h = l[0], l[2]
print(g, h, " вытащить из listcomprehension и присвоить их переменным")

print([i for i in ls][1], " вытащить из listcomprehension с индексом")



# Операции между LIST и LIST[LIST], умножить ОБ из b  на ОБ из LIST[LIST] поиндексно

x = [[10, 20, 30, 40], [50, 60, 70, 80]]  # вложенные LIST[LIST]
b = [2, 2, 2, 2]

j = map(lambda k: [[j * k for j in i] for i in x], b)  # lambda вытаскивает  из вложенных LIST поиндексно все ОБ
print(next(j), " next(j) выводит одну итерацию")


# Поиндексное действие П Р О С Т О
w = [10, 20, 30, 40]
d = [2, 2, 2, 2]
print(list(map(lambda x, y: x + y, w, d)), " Поиндексное действие П Р О С Т О")

# Нахождение в LIST[LIST] списка с min суммой значений
c = [[1000, 1], [5, 80], [1, 200], [200, 1], [65, 21], [20, 73], [13, 72]]
sum_of_lists = [sum(i) for i in c]
print(c[sum_of_lists.index(min(sum_of_lists))], " Нахождение в LIST[LIST] списка с min суммой значений")
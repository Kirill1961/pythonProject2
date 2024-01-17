
""" перевод числа в строку,2й аргумент это
основание системы счисления, 16 это :
0123456789abcdef, """

print(int('4aa', 16))

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ]

result = [elem for elem in a if elem in b]

resultt = set(a).intersection(set(b))

resulttt = list(set(a) & set(b))

print(result, resultt, resulttt)

c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ress = [item for item in c if item < 5]
print(ress)





l = [1, 2, 3, 4, 5, 6]

mid = len(l) // 2 #  Делим длинну списка на 2 части и выводим срезы lef и rht
lef = l[:mid]
rht = l[mid:]
print(lef, rht)

str_list = ['a', 'b', 'c', 'd', 'e', 'f'] # срезом с шагом выделяем нужные куски из списка
step = 3
res_lis = [str_list[i:i + step] for i in range(0, len(str_list), step)]

print(res_lis)




b = ['a', 'b', 'c', 'd', 'e', 'f']  # срезом с шагом выделяем нужные куски из списка
step = 3
div = [b[ind:ind + step] for ind in range(0, len(b), step)]

print(div)

for i in [b[ind:ind + step] for ind in range(0, len(b), step)]:
    print({''.join(i)})


""" Список списков с строчн ОБ изменяем в список соединёных строчных ОБ"""
# initialize list
test_list = [["g", "f", "g"], ["i", "s"], ["b", "e", "s", "t"]]

# printing original list
print("The original list : " + str(test_list))

res = []
for sublist in test_list:
    print(sublist)
    res.append(''.join(sublist))

# printing result
print("The String of list is : " + str(res))
#This code is contributed by Vinay Pinjala.

import math

print(math.factorial(3))

print(math.comb(4, 2), '  число сочетаний ')  # число сочетаний n! / (k! * (n - k)!)
print(math.fmod(5, 2))
print(math.frexp(5))
print(math.isqrt(5), '  целочисленный квадратный корень')
print(math.nextafter(8, 4))
print(math.perm(3, 2), '  количество способов выбора k элементов из n, n! / (n - k)! when k <= n')

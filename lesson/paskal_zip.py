m_list = [1]
print(m_list)


def f_p_l():
    while len(m_list) != 10:  # ЧИСЛО СТРОК
        sec_l = [1]
        for a in range(len(m_list)):
            sec_l.append(sum(m_list[0:2]))
            m_list.pop(0)
        yield sec_l


for i_p_l in f_p_l():
    m_list.extend(i_p_l)
    print(i_p_l)

""" ф-ция zip принимает любое кол-во аргументов, в данном случае
сумму списков:
 [0] + row и row + [0], затем объединяет соответствующие их
 значения,  т.е. все первые значения затем все вторые и тд,
 возвращает кортеж """


# первая итерация : [0,1]
#                   [1,0]
# zip объединил в кортежи первые значения списков затем вторые (0,1) и (1,0)
# sum складывает item в кортежах, тк конструкция в [ ],
# то row получает список [1,1]
# вторая итерация [0,1,1]
#                 [1,1,0] ---> кортежи (0,1) (1,1) (1,0)
# сработала sum и [ ] и row = [1,2,1]
def PrintPasTriangle(rows):
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip(row + [0], [0] + row)]


PrintPasTriangle(5)


""" _________________ Add Two Numbers_______________________"""
l3 = [4, 4,  5]
l4 = [6, 5,  4, 2, 9]
l_min = l3 if len(l3) - len(l4) < 0 else l4
for i in range(abs(len(l4) - len(l3)) if len(l3) - len(l4) != 0 else 0): # количество добавленных нулей
    l_min.append(0)
list_one = [sum(l_o) for l_o in zip(l3, l4)]
last_ind = len(list_one) - 1
for ind  in range(len(list_one[0:-1])):
    if list_one[ind] >= 10:
        list_one[ind] = list_one[ind] - 10
        list_one[ind + 1] = list_one[ind + 1] + 1
    if list_one[last_ind] >=10:
        val_last = list_one[last_ind] - 10
        list_one[last_ind] = val_last
        list_one.append(1)






print(list_one,'one')
print('last index-', last_ind, 'last value-', list_one[last_ind])
print(list_one)

c = [10, 20, 30, 40]
b = [2, 2, 2, 2]
print(list(map(lambda x_f, e_r_f:  e_r_f * x_f, c, b)), " Поиндексное действие П Р О С Т О")
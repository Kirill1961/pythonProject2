from functools import wraps
from _datetime import datetime
from threading import Thread
from time import sleep
from typing import List

import requests
#
#
# def outer(fu_nc):
#     """ decorator """
#
#     @wraps(fu_nc)
#     def inner(*args, **kwargs):
#         print('six/' * 3)
#         fu_nc(*args, **kwargs)
#
#     return inner
#     inner.__name__ = fu_nc.__name__
#     inner.__dock__ = fu_nc.__dock_

# m_list = [1]
# print(m_list)
#
#
# def f_p_l():
#     while len(m_list) != 10:  # ЧИСЛО СТРОК
#         sec_l = [1]
#         for a in range(len(m_list)):
#             sec_l.append(sum(m_list[0:2]))
#             m_list.pop(0)
#         yield sec_l
#     # try:
#         raise Exception('okokokok') # принудительный вызов исключения
#     # finally:
# try:
#     for i_p_l in f_p_l():
#         m_list.extend(i_p_l)
#         print(i_p_l)
# except Exception as eer:
#     print(eer)
import csv

#
# data_users = [
#     (' name users', ' addresses users', 'N'),
#     ['user1', 'address1', '1'],
#     ['user2', 'address2', '2'],
#     ['user3', 'address3', '3'],
# ]
#
# # with open('c_from_data.csv', 'w', newline='') as file:
# #     writer = csv.writer(file, delimiter=';')  # создаём ОБ писатель with name writer
# #     writer.writerows(data_users)
#
# with open('c_from_data.csv') as file:
#     red = csv.reader(file)
#     for i in red:
#         print(i)
#
# with open('c_from_data.csv', newline='') as file:
#     writer = csv.DictReader(file, delimiter=';')  # создаём ОБ писатель with name writer
#     for i in writer:
#         print(i)
#
# data_app = [['user4', 'address4', '4'],
#             ['user5', 'address5', '5']
#             ]
#
# with open('c_from_data.csv', 'a', newline='') as file:
#     writer = csv.writer(file, delimiter=';')  # создаём ОБ писатель with name writer
#     writer.writerows(data_app)
#
# my_dict = [
#
#     ['user1', 'address1', '1'],
#     ['user2', 'address2', '2'],
#     ['user3', 'address3', '3'],
# ]

# with open('c_from_data.csv', 'r') as da_ta:
#     reader = csv.DictReader(da_ta)
#
#     with open('c_in_data.csv', 'w') as da_ta:
#         header = ['name users', 'addresses users', 'N']
#         writer = csv.DictWriter(da_ta, fieldnames=header)  # создаём ОБ писатель with name writer
#
#         writer.writeheader()  # запись имён полей
#
# try:
#     for i_dict in reader:
#         # print(i_dict)
#         writer.writerow(i_dict)
# except ValueError as err:
#     print(err)

# with open('c_from_data.csv', 'r') as da_ta:
#     # header = ['name users ', 'addresses users', 'Phone']
#     reader = csv.DictReader(da_ta, fieldnames=['name users /', 'addresses users /', 'Phone'], )
#     with open('c_in_data.csv', 'w', newline='') as fi_le:
#         writer = csv.DictWriter(fi_le, fieldnames=['name users /', 'addresses users /', 'Phone'])
#         writer.writeheader()  #  заголовков
#         for i_dict in reader:
#             # print(i_dict)
#             # del i_dict ['addresses users /']
#             writer.writerow(i_dict)
#             print(i_dict)


""" Задан массив целых чисел nums и целое число - target?
вернуть индексы двух чисел таким образом, что бы они складывались в число равное target."""
nums = [4, -2, 5, 0, 6, 3, 2, 7]


class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        print(len(nums))

    def twoSum(self, nums: List[int], target: int) -> List:
        self.nums = nums
        self.target = target
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


ans = Solution(nums, 5)
print(ans.twoSum(nums, 1), 'qqqqqqqqqqqqqq')


""" даны два непустого списка, представляющих два неотрицательных целых числа,
в данном случае это цифры 445 и 65429
Цифры хранятся в обратном порядке, и каждый из их узлов содержит одну цифру.
 Надо сложить эти два числа и вывести число ответа в обратном порядке"""


l3 = [4, 4, 5]
l4 = [6, 5, 4, 2, 9]

# d = len(l4) - len(l3)

# num_el = abs(d) if d != 0 else 0
# print(num_el, '++')
l_min = l3 if len(l3) - len(l4) < 0 else l4
print((abs(len(l4) - len(l3)) if len(l3) - len(l4) != 0 else 0), 'null')

X = [l_min.append(0) for i in range(abs(len(l4) - len(l3)) if len(l3) - len(l4) != 0 else 0)]

list_one = [sum(l_o) for l_o in zip(l3, l4)]
last_ind = len(list_one) - 1
for ind in range(len(list_one[0:-1])):

    if list_one[ind] >= 10:
        list_one[ind] = list_one[ind] - 10
        list_one[ind + 1] = list_one[ind + 1] + 1
    if list_one[last_ind] >= 10:
        val_last = list_one[last_ind] - 10
        list_one[last_ind] = val_last
        list_one.append(1)
print(list_one)


class two_Numbers():
    def __init__(self, nums=[5, 6, 4, 2, 9], target=4):
        # self.l3 = l3
        # self.l4 = l4
        self.nums = nums
        self.target = target

    # def __init__(self):
    #     self.target = None
    #     self.l4 = None
    #     self.l3 = None
    #     self.nums = None

    # def add_Two_Numbers(self, l3, l4):
    #     # self.l3 = l3
    #     # self.l4 = l4
    #     l_min = l3 if len(l3) - len(l4) < 0 else l4
    #     for i in range(abs(len(l4) - len(l3)) if len(l3) - len(l4) != 0 else 0):
    #         l_min.append(0)
    #     list_one = [sum(l_o) for l_o in zip(l3, l4)]
    #     last_ind = len(list_one) - 1
    #     for ind in range(len(list_one[0:-1])):
    #         if list_one[ind] >= 10:
    #             list_one[ind] = list_one[ind] - 10
    #             list_one[ind + 1] = list_one[ind + 1] + 1
    #         if list_one[last_ind] >= 10:
    #             val_last = list_one[last_ind] - 10
    #             list_one[last_ind] = val_last
    #             list_one.append(1)
    #     return list_one

    def nums_targ(self, nums, target):
        self.nums = nums
        self.target = target
        for i in [(nums.index(n), nums.index(m)) for n in nums for m in nums[0:] if target == n - m or target == m + n]:
            if len(i) == 2:
                return list(i)


t_m = two_Numbers(nums, 1)
t_n = two_Numbers(nums, 1)
print((t_n.nums_targ([5, 5, 4, 2, 9], 1), 'nums_targ 1'))
# print(t_n.add_Two_Numbers([4, 4, 5], [6, 5, 4, 2, 9]), 'add_Two_Numbers')
print((t_n.nums_targ(nums, target=7), 'nums_targ 2'))
print((t_m.nums_targ([6, 5, 4, 2, 9], target=3), 'nums_targ 3'))


class dog:
    def __init__(self, name='dog', age=1, breed=' dnt know'):
        self.name = name
        self.age = age
        self.breed = breed

    def larges_age(self, dan_age, sandy_age):
        # self.dan_age = dan_age
        # self.sandy_age = sandy_age
        hwo_older = 'Dan' if dan_age - sandy_age > 0 else 'Sandy'
        return hwo_older


Sandy = dog('Sandy', 14)
Dan = dog(age=8)
print(Sandy.__dict__)
print(Dan.__dict__)
print(Sandy.breed, Dan.age, Sandy.age)
print(Dan.larges_age(8, 10))


class Shark:
    animal_type = "fish"


new_shark = Shark()
print(new_shark.animal_type)

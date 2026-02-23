""" _________________ Add Two Numbers_______________________"""


# l3 = [4, 4,  5]
# l4 = [6, 5,  4, 2, 9]
def add_Two_Numbers(l3, l4):
    l_min = l3 if len(l3) - len(l4) < 0 else l4  # список с наименьшим ко-вом значений
    for i in range(abs(len(l4) - len(l3)) if len(l3) - len(l4) != 0 else 0):  # количество добавленных нулей
        l_min.append(0)  # добавление нулей для выравнивания списков
    list_one = [sum(l_o) for l_o in zip(l3, l4)]  # создание исходного списка из 2х списков
    last_ind = len(list_one) - 1  # индекс последнего ОБ
    for ind in range(len(list_one[0:-1])):  # перебор коллекции ОБ кроме последнего
        if list_one[ind] >= 10:  # фильтр для переноса единицы если все ОБ кроме последнего > или = 10
            list_one[ind] = list_one[ind] - 10
            list_one[ind + 1] = list_one[ind + 1] + 1
        if list_one[last_ind] >= 10:  # фильтр для переноса единицы последнего ОБ если он > или = 10
            val_last = list_one[last_ind] - 10
            list_one[last_ind] = val_last
            list_one.append(1)  # добавление единицы если последний ОБ > или = 10
    return list_one


print(add_Two_Numbers([4, 4, 5], [6, 5, 4, 2, 9]))


""" _________________two summ___________________________"""

""" Проверка является ли переменная целым числом с помощью isinstance(x, int) и int()
    isInt = isinstance(x, numbers.Integral)
    print(isInt) 
    >>> True  
    isInt = int(x) == x
    print(isInt) 
    >>> True """
nums = [2, 9, 1, 7, 3]
target = 8

""" _____________________Тело ф-ции, основной код"""
print([(nums.index(n), nums.index(m)) for n in nums for m in nums[0:] if target == n - m or target == m + n])

""" ____________________ Функция___________________________"""


def nums_targ(nums, target):
    for i in [(nums.index(n), nums.index(m)) for n in nums for m in nums[0:] if target == n - m or target == m + n]:
        if len(i) == 2:
            return list(i)


print(nums_targ(nums, target=8))

""" __________________________MY FIRST CLASS ________________________________"""

class two_Numbers():
    # def __init__(self, l3, l4, nums, target):
    #     self.l3 = l3
    #     self.l4 = l4
    #     self.nums = nums
    #     self.target = target

    def __init__(self):
        self.target = None
        self.l4 = None
        self.l3 = None
        self.nums = None

    def add_Two_Numbers(self, l3, l4):
        self.l3 = l3
        self.l4 = l4
        l_min = l3 if len(l3) - len(l4) < 0 else l4
        for i in range(abs(len(l4) - len(l3)) if len(l3) - len(l4) != 0 else 0):
            l_min.append(0)
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
        return list_one

    def nums_targ(self, nums, target):
        self.nums = nums
        self.target = target
        for i in [(nums.index(n), nums.index(m)) for n in nums for m in nums[0:] if target == n - m or target == m + n]:
            if len(i) == 2:
                return list(i)


t_n = two_Numbers()
print((t_n.nums_targ([6, 5, 4, 2, 9], 1)), 'nums_targ')
print(t_n.add_Two_Numbers([4, 4, 5], [6, 5, 4, 2, 9]), 'add_Two_Numbers')
print(t_n.__dict__)
print(two_Numbers.__dict__)





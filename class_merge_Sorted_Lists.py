""" Задание из LEET CODE --- Merge k Sorted Lists, Вам дается массив к списков,
каждый связанный список сортируется в порядке возрастания.Объединить все связанные списки в один
отсортированный связанный список и вернуть его."""

# 1й вариант простой список
print('        ВАРИАНТ 1')
lists = [[1, 4, 3], [2, 5, 11], [3, 7, 6, 24, 0]]


class Internal_lists:
    def __init__(self, items_list, next):
        self.items_list = items_list
        self.next = next


class Linked_list:
    def __init__(self, head):
        self.head = head

    def merge(self, all_lists):
        self.head = all_lists
        index = 0
        merge_list = []
        while all_lists is not len(all_lists) != index:
            separate_list = all_lists[index]
            merge_list.extend(separate_list)
            index += 1
        return sorted(merge_list)


merge_lists = Linked_list(lists)
print(merge_lists.head)
print(merge_lists.merge(lists))

# from typing import List

# 2й вариант задаём список списков -> трансформируем в связанный -> сортируем -> и выводим связ список
print('         ВАРИАНТ 2')
list = [[1, 4, 3], [2, 5,  11], [3, 7, 6, 24, 0]]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def __call__(self, g="Kirill", *args, **kwargs):
    #     print('Hellow', g)

    def mergeKLists(self, lists,*args, **kwargs):

        sorted_list = []
        index = 0
        while index < len(list):
            index += 1
            next = ListNode(list[index - 1])
            if lists is None:
                lists = next
            nextlists = next
            # print(nextlists.val,nextlists, '      Связали исходный список списков list')
            while nextlists.val :
                nextval = ListNode(nextlists.val.pop(0))
                print('\t'*2,nextval.val,'  ->  Изъяли из связанных списков отдельные значения ;     ',  nextval, '   и связали эти значения ')
                sorted_list.insert(0, nextval.val)
        linkedsort = sorted(sorted_list)
        print(linkedsort, '  sorted linked list')


obj1 = Solution()
obj1.mergeKLists(list)
obj1()  # для вызова __call__

""" _____________________________1 -е  задание """
from typing import Optional

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


print(nums_targ(nums, target=8),'****')


l1 = [2, 4, 3]
l2 = [5, 6, 4]




class MyHashSet:

    def __init__(self):
        self.arry = [[] for _ in range(10)]

    def add(self, key: int) -> None:
        subkey = key % 1000
        if not self.contains(key):
            self.arry[subkey].append(key)
            print(subkey,'|||')
            print(self.arry)
    def remove(self, key: int) -> None:
        subkey = key % 1000
        if self.contains(key):
            self.arry[subkey].remove(key)
            print(self.arry,'&&&')
    def contains(self, key: int) -> bool:
        subkey = key % 1000
        print(key,' === ')
        return key in self.arry[subkey]

sk = MyHashSet()
sk.add(1003)

sk.remove(1003)
sk.contains(1009)

# Definition for singly-linked list,
# Определение для односвязного списка.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int) :
        nodes = []
        cnt = 0
        cpy = head
        while head:
            nodes.append(head)
            head = head.next
            cnt += 1
            if cnt == k:
                cnt = 0
                m,n = 0,k-1
                while m<n:
                    nodes[m].val,nodes[n].val = nodes[n].val,nodes[m].val
                    m,n = m+1,n-1
                nodes = []
        return cpy

rk = Solution()
Solution.reverseKGroup(rk, 5, 2)
# rk.reverseKGroup([1,2,3,4,5], 2)
print(rk.__dict__)
rn = ListNode()
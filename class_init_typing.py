class Cat:
    """ внутри метода __init__ через self можно задать начальные значения 
    атрибутов экземпляра. Аргументам метода __init__ можно присваивать  сразу значения ,
    если не присвоено как "nm" , то надо указывать значения в виде аргументов
      при создании объекта, метод __init__ производит инициализацию те заполнение
      наших объектов какими либо значениями тк значения аргументов хранятся в __init__"""

    #     def __init__(self, nm,  ag, cl ): #| <--- способ создания объекта, имя класса Cat со
    #         print('Ok',self, nm,  ag, cl) #| значениями для метода __init__, сам объект сохраняется
    # Cat('Joe', 10, 'Wite')                #|в переменной self знач подставляются и выводится ОБ + значения:
    #                                       #| Ok <__main__.Cat object at 0x00000145B6328810> Joe 10 Wite

    def __init__(self, nm, ag=80, cl='Bl'):
        self.name = nm
        self.age = ag
        self.color = cl

    def s_v(self, nm, ag=10, cl='black'):
        self.name = nm
        self.age = ag
        self.color = cl


bob = Cat('Bobik')  # экземпляр(объект) bob
bob.s_v('Bob')  # объекту bob добавили сво-ва из метода s_v
# Cat()         
Tom = Cat('Tom', ag=50)

bim = Cat('Lisa')

""" метод __dict__ показывет содержание объекта"""

print(bob.__dict__)
print(Tom.__dict__)
print(bim.__dict__)


# class Gr:
#     def f_c(self, p = 100, t = 'rim'):
#         self.pol = p
#         self.tol = t
#         return  p, t
# sok = Gr()
# kos = Gr()
# print(sok.f_c())
# print(sok.f_c(10,'xpen'))
# print(sok.__dict__)
# print(kos.f_c(),(kos.__dict__))

# class CoFr:
#     def __init__(self, i, v, z) -> None:
#         self.incr = i
#         self.vincr = v
#         self.zic = z
#     def increase(self):

#         self.zic =  self.zic * 2
#         self.incr = self.incr * 2 
#         self.vincr = self.vincr * 2  
#         print(self.vincr, self.incr, self.zic )
# a = CoFr(100,33,2)  
# b = CoFr(2,5,100)  
# b.increase()
# a.increase()


# class ProbClass:
#     # xx = 0 
#     def __init__(self, incr : int = 0, arg_object : int = 1, step = 0) :
#         self.incr = incr 
#         self.arg_object = arg_object
#         self.step = step      
#     def increase(self):       
#         if self.step == 0:    
#             self.incr += 1 + self.arg_object  + self.step  - 1 
#         else:
#             self.incr += 1 + self.step  - 1
#         print (self.incr)
#     def __repr__(self) -> str:
#         return(f'{self.incr}')    
#         # ProbClass.xx += 1 
#         # print('\t'*2,ProbClass.xx)


# object_c = ProbClass()
# object_d = ProbClass(100)
# object_e = ProbClass(100,20)
# object_f = ProbClass(step=15)

# print(object_d)
# object_c.increase()
# object_c.increase()


# object_d.increase()
# object_d.increase()


# for i in range(3):
#     object_e.increase()

# for i in range(3):
#     object_f.increase()


# class Cf:
#     def __init__(self, vv: int = 0, ii: int = 1) -> None:
#         self.vv = vv
#         self.ii = ii
#     def innc(self ):
#         self.vv += self.ii 
#         # print(self.vv)
#     def __repr__(self) -> str:
#         return str(self.vv)
# avv = Cf(100,10)
# print(avv)    
# print(avv)
# print(avv)   
# for k in range(3):
#     print(avv)

# print(13%2)
class try_self:
    def __init__(self, a, b, c):
        self.aa = a
        self.bb = b
        self.cc = c

    def met_self(self):
        return self.aa + self.bb / self.cc


obj1 = try_self(2, 5, 9)
print(obj1.cc)
print(obj1.met_self())
obj2 = try_self(100, 200, 300)
print(obj2.met_self())


class Sol:
    def __init__(self, f, g):
        self.f = f
        self.g = g
        print(f, g, )

    def twoS(self, f, g):
        self.f = f
        self.g = g
        return self.f + self.g


ans = Sol(10, 34)
print(ans.twoS(1, 1))

""" Python — это язык с сильной динамической типизацией.
    до Python 3.9 : from typing import List, Tuple, Dict, Set , 
    после 3.9:
    тип всех элементов списка - primes: list[int],
    тип каждого элемента кортежа - person_info: tuple[str, int, float, float],
    тип ключей, тип значений - stock_prices: dict[str, float],
    тип всех элементов множества - valid_answers: set[str]"""

from typing import List

nums = [4, -2, 5, 0, 6, 3, 2, 7]


class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        print(len(nums))

    def twoSum(self, nums: list[int], target: int) -> list:
        self.nums = nums
        self.target = target
        for i in range(len(nums)):
            for j in range(i + 1):
                if nums[j] == target - nums[i]:
                    return [i, j]


ans = Solution(nums, 9)
print(ans.twoSum(nums, 3))

""" В этом классе аргумент age один на два ОБ: self.dan_age = age и self.sandy_age = age,
    но по хорошему надо писать именные аргументы self.dan_age = dan_age и self.sandy_age = sandy_age,
    в __init__ по порядку идут типы аргументов 1й - str, 2й - int, 3й - int, 4й - str ,
    В таком же порядке должны присваиваться аргументы по типам при создании ОБ этого класса: str, int, int, str"""


class dog:
    spiteful = 'spiteful '
    kind =' kind'
    def __init__(self, name='dog', sandy_age=None, dan_age=1, breed=' dnt know'):
        self.name = name
        # self.age = age
        self.breed = breed
        self.dan_age = dan_age
        self.sandy_age = sandy_age

    def larges_age(self, dan_age, sandy_age):
        # self.dan_age = dan_age
        # self.sandy_age = sandy_age
        print(Sandy.sandy_age, '>>>>>>>>>>>>>>>>>>>>>>>>>>')
        hwo_older = 'Dan' if dan_age - sandy_age > 0 else 'Sandy'
        return hwo_older


""" В ОБ именованные аргументы если их поменять местами то в __init__ то же надо менять местами арг, иначе 
    может не совпасть тип аргументов str или int"""

Sandy = dog('Sandy', 5)
Dan = dog('Dan', dan_age=8)
print(Sandy.__dict__, 'Sandy.__dict__')
print(Dan.__dict__)
print(dog.__dict__)
print(Sandy.sandy_age, Dan.dan_age, 'age age age')
print(Dan.larges_age(Dan.dan_age, Sandy.sandy_age))
print(Sandy.spiteful)
""" Вариант записи экземпляра с аргументами через метод и класс - dog.larges_age(Dan, dan_age=10, sandy_age=5)  """
print(dog.larges_age(Dan, dan_age=10, sandy_age=5))
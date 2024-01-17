
class N:
    enimal = "dog"   # атрибуты(свойства) класса
    flower = "rose"

# Созд экземпляров
d = N()
w = N()

# созд атрибутов экземпляров
w.plant = "wood", 100
d.enimal = " hippopotam"
d.flower = "tulip"
print(w.__dict__, d.__dict__, " w,d.__dict__")

print(" ")

# динамически добавляем атрибут в класс
N.flower = "iris"

# с помощью SETATTR динамически добавляем атрибут в класс
setattr(N, "peopl", " John") # в классе
setattr(w, "plant", "birch")

# Присваиваем переменной атрибут класса
res = N.flower, N.peopl

# с помощью SETATTR Изменяем значение атрибута peopl
setattr(N, "peopl", "Bob")

# проверить существование атрибутов  с помощью hasattr
print(hasattr(N, "flower"), hasattr(d, "enimal", ), " - проверить существование атрибутов и экземпляров hasattr(N, flower})")

print(" ")

# Удаление атрибутов
del d.enimal




# Параметр self, формальные параметры



class A:
    def __init__(self, x=100, y=500):
        print(" вызывается  __init__ ")
        self.x = x
        self.y = y

    def mult(self, x, y):
        return x * y

o = A() # если формальные параметры, то в ЭКЗ можно не указывать параметры


# Параметры при создании ЭКЗ
class G:
    def __init__(self, x, y):
        print(" вызывается  __init__ ")
        self.x = x
        self.y = y

    def mult(self, x, y):
        return x * y

l = G(44, 55) # Параметры при создании ЭКЗ



""" Вызов метода из класса + добавка атрибута в ЭКЗ"""


class R:
    def __init__(self, x, y):
        print(" вызывается  __init__")
        self.x = x
        self.y = y

    def mult(self):
        print(self.x, self.y)
        return self.x * self.y
    def divid(self, n):
        return (self.x * self.y) ** n
ob = R(5, 2)
b = ob.mult()
ob.new_value = 2 # добавка атрибута в ЭКЗ

print(ob.divid(ob.new_value), " использование добавленного  атрибута экземпляра в методе divid")
print(ob.__dict__, " добавка атрибута в ЭКЗ")
print((b),  " Вызов метода из класса")


print(" ")



print(w.__dict__, d.__dict__, " w,d.__dict__ изменили с помощью setattr")
print(" ")
print(N.__dict__, " N.__dict__")
print(" ")
print(res, " res")

print(" ")

print(d.__dict__, " удалили  атрибут enimal" )

print(" ")

print(o.__dict__, "Параметр self, формальные параметры")
print(l.__dict__, "Параметры при создании ЭКЗ")




# SELF
def f(a):
    return pow(a,2)

c = 1000
class K:
    def __init__(self, a):

        self.a = a
        # self.l = []
        # print(self.a, " aaaaa")
        # print(self.l, " lllll")

    def m(self,  b):
        # self.l.append(f(b) * self.a)
        # print(self.l, " 2l2l2l")
        # return self.l
        return f(b) * self.a

e = K(c)
print(e.m(4))
print(" ")
print(e.m(4), print(" e.m(4)"))
print(" ")
print(dir(e), print(" dir(e)"))
# print (K.__dir__(e), print(" K.__dir__(e)"))
# print(" ")
# print(K.__doc__, print(" K.__doc__ "))
# print(e.__dict__, " e.__dict__")

print(" ")

def f_s(b):
    # print((b, " NN b Naive"))
    return pow(b,2)

class Nn:
    def __init__(self, c):
        self.c = c

    def f_t(self, g):
        # w_p = f_s(g) * self.k
        return f_s(g) * self.c
ex = Nn(5)
print(ex.f_t(10), " Nn")
# print(dir(ex))









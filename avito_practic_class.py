import numpy as np
import pandas as pd

'''
1️⃣ Синяя стрелка вверх - Метод переопределяет метод в родительском классе.
* Overrides method in A
    👉 Это значит:
    в A есть метод с таким же именем
    текущий метод перекрывает его

2️⃣ Синяя «развилка» (несколько стрелок) - Метод переопределён в нескольких дочерних классах.
* Is overridden in: B, C
    👉 То есть:
    A.process определён здесь
    но в B и C есть свои версии
    
3️⃣ Красная стрелка в этом значке - Есть несколько путей наследования / неоднозначность
* Чаще всего это:
    множественное наследование
    ромбовидная структура
    PyCharm таким образом намекает:
        «Осторожно, здесь MRO может быть неочевиден»

📌 Click Красная стрелка - перейти к родителю
📌 Click Синяя стрелка - перейти к потомку

'''

class A:
    def method_0(self):
        return "class A"
    def method_2(self):
        return "class A"

class B(A):
    def method_0(self):
        return super().method_0()
    def method_1(self):
        return "class B"

class C(A):
    def method_0(self):
        return "class C"
        # return super().method_2()
    def method_1(self):
        # return "class C"
        return super().method_2()
    def method_2(self):
        return "class C"
        # return super().method_2()
class D(B, C):
    pass

obj = D()
print(obj.method_0(), obj.method_1(), obj.method_2())

print('MRO : \n ', D.mro())


class R:
    def process(self):
        print("Processing in class R")

class F(R):
    def process(self):
        # super().process()  # Вызов метода process() из класса A
        print("Processing in class F")
        super().process()  # Вызов метода process() из класса A

class W(F):
    def process(self):
        super().process()  # Вызов метода process() из класса B
        print("Processing in class W")

w = W()
w.process()

print(W.mro())

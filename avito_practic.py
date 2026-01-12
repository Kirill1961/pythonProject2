import numpy as np
import pandas as pd

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


class A:
    def process(self):
        print("Processing in class A")

class B(A):
    def process(self):
        # super().process()  # Вызов метода process() из класса A
        print("Processing in class B")
        super().process()  # Вызов метода process() из класса A

class C(B):
    def process(self):
        super().process()  # Вызов метода process() из класса B
        print("Processing in class C")

c = C()
c.process()

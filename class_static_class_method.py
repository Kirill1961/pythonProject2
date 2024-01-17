
# @classmethod
class A:
    PAR1 = 0
    PAR2 = 50
    @classmethod     # # classmethod использование только переменных (состояние) класса А
    def class_methd(cls, num):
       return cls.PAR1 < num < cls.PAR2
    def __init__(self, x, y):
        print(" __init__")
        self.x = self.y = 0
        if A.class_methd(x) and A.class_methd(y) is True : # # фильтр пропускает значения соотв условию из class_methd
            self.x = x
            self.y = y
            print(self.x, self.y, " значения соотв условию из class_methd")
    def multi_ply(self):
       return self.y,self.x

o = A(5, 5)
print(A.class_methd(5), " A.class_methd")
print(A.multi_ply(o), " A.multi_ply")
print(o.multi_ply(), " o.multi_ply")


# @classmethod

class D:
    PAR1 = 100
    PAR2 = 50
    @classmethod
    def class_methd(cls, num):
       return (cls.PAR1 + cls.PAR2) ** num # cls - ссылка на класс А
       # return (A.PAR1 + A.PAR2) ** num

    def __init__(self, x=2, y=1):
        print(" __init__")
        self.x = x
        self.y = y

    def multi_ply(self):
       return self.y + self.x

o = D()
print(D.class_methd(2), " D.class_methd")
print(D.class_methd(o.multi_ply()), " D.class_methd в аргументе результат метода o.multi_ply()")
print(D.multi_ply(o), " D.multi_ply(o)")
print(o.multi_ply(), " o.multi_ply()")



#  @staticmethod

class P:
    PAR1 = 10
    PAR2 = 5
    @classmethod
    def class_methd(cls, num):
       return (cls.PAR1 * cls.PAR2) * num

    def __init__(self, x=2, y=1):
        print(" __init__")
        self.x = x
        self.y = y

    @staticmethod           #  @staticmethod
    def static_method(x, y):
        return (x - y) ** 2


    def multi_ply(self):
       return self.y + self.x



s = P()
print(P.class_methd(2), " D.class_methd")
print(P.class_methd(s.multi_ply()), " D.class_methd в аргументе результат метода s.multi_ply()")
print(P.multi_ply(s), " D.multi_ply(s)")
print(s.multi_ply(), " s.multi_ply()")
print(s.static_method(4, 2), " @staticmethod")


# # Упрощённый код naive_Bayes
def mult(x):
    # x = {"w" : [0, 1], "v" : [1, 0]}
    return [(w, k, v) for w, (k, v) in x.items() ]

def spam(m):
    print([i [0] for i in m], " вызов из clasify(self) преобразование ф-цией spam(m)")
    return [[i [0] for i in m]]

y = {"w": [0, 1], "v": [1, 0]}
class NvB:

    def __init__(self, a):
        self.a = a
        self.listt = []

    def train(self, a):
        self.listt = mult(a)
        print(self.listt, "заполненый список кортежей из ф-ции mult(x) ")
    def clasify(self):
        return spam(self.listt)

object = NvB(y)
object.train(y)
print(object.clasify(), "clasify")
w = object.a  # # все переменные можно вызывать через экземпляр
v = object.listt
print(w, 'переменная а ;', v, " переменная self.listt")
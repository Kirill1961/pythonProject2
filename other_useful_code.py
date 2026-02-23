
                        # pow(a,2) self, init
def f(a):
    return pow(a,2)


class k:
    def __init__(self, a=50):
        print(a)
        self.a = a
        self.l = []

    def m(self,  b):
        self.l.append(f(self.a) * b)
        return self.l


e = k(a=500000)
print(e.m(4))



                    # Переопределение переменной Х
print (k.__dir__(e))
def f(x):
    n = 0
    while n < 5:
        n += 1
        print(x, "1")  # Одно значение Х
        x = x * 2
        print(x, "2")  # Другое значение Х


f(2)


                    # Оператор Морж / Warlus

def func(x):
    return x * 100

result = [func(100), func(100)**2, func(100)**3] # func() вызывается три раза

result_warlus = (w := func(100), w ** 2, w ** 3) # func() вызывается один раз и записывается в переменную w

result_lambda = lambda y : y

print(result, " result", "\n" )
print(result_warlus, "   :=  result_warlus,", "\n")

print(result_lambda([v := func(200), v ** 2, v ** 3]), " result_lambda со своим аргументом", "\n")
print(result_lambda(result), " result_lambda с аргументом для func(x): ", "\n")


                    # Списковое включение с  Морж / Warlus
data = [11, 22, 33]

res_func = [func(x) for x in data ]# прокручиваем data через func(x), func() вызывается три раза


res_y_func = [y for x in data if  (y := func(x) )] # func() вызывается один раз и записывается в переменную w

print(res_func, " res_func", "\n")
print(res_y_func, " res_y_func", "\n")


# Накапливание данных
c = 0
data = [5, 4, 3, 2]
print([c := c + x for x in data], " Накапливание данных")


                    # Прокрутка нужного значения определённое ко-во раз
a =  5
print([a for _ in range(5)], " Прокрутка нужного значения определённое ко-во раз")

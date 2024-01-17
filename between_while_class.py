class Class_first:

    def __init__(self, a=None):
        self.a = a

    def aa(self, a):
        print(a)
        while a < 5:
            a += 1
            print('a/c =', a)
            valaa = Class_second()
            valaa.bb(a)
            if a == 5:
                return a


class Class_second:
    def __init__(self, b=None, c=None):
        self.b = b
        self.c = c

    def bb(self, c):
        # valbb = Class_first()
        # valbb.aa(555)
        b = c * 5
        if c == 5:
            return b
        print('     b =', b )


expir_f = Class_first()
valf = expir_f.aa(0)

# expir_s = Class_second()
# vals = expir_s.bb(valf)
# print('     b =', vals)

# print(valf, vals, 'valf vals')

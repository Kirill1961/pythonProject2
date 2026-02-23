a = int (input())
b = int (input())

try:
    ressult = a / b
    if b > 0 : print(ressult)
except ZeroDivisionError:
    ressult = ('OK')
    print(ressult)

try:
    f = int(input())
    if  f == int: 
        print(f)
except ValueError:
    print('no')
else :
    print('all good')
finally:
    print('go 100%')


def cldr():
    try:
        r=float(input())
        h=float(input())
        side=2*3.14*r*h
        crcl=3.14*r**2
        full=side*2*crcl
    except ValueError:
        print('ok')
    else:
        return full
scr=cldr()
print(scr)

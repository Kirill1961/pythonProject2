import os
import sys
# import logg as lg
from glob import glob
import time

a = [0.98, 0.14, 0.44, 0.13, 0.09, 0.19, 0.53, 0.7]


def ou(x):

    def ine(y):
        return x * y

    return ine(5)


print(ou(2), "ok")





def count_vs_while(x):
  if x < 1000:
    print(x)
    return True
  return False
x = 2
while count_vs_while(x):
  x *= 10
count_vs_while(2)


f = open("pass.txt", "w")
f.write("ещё один текст")
f.close()
f = open("pass.txt", "r")
print(f.read())
print(f)

time_carent = time.asctime()
print(f"текущее время :{time_carent}")

def foo(x):
    while True:

        yield x * 10
        x + 5
f = foo(2)
print(next(f))
print(next(f))
print(next(f))
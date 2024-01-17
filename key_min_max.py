a = [1,2,3,0.5]
b = [0,2,7]

# параметр key=  -  для ф-ции  min / max указывает по какому признаку определять min / max
print(min(a,b,key=sum), ' выбор из 2x списков наименьшей суммы') #
print(max(a,b,key=sum), ' выбор из 2x списков наибольшей суммы') #
print(min(a, key=None))
print(max(a,b,key=len))  # определяет max по длинне списка
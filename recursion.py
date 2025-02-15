
def rc(i):
    print(i,'one')  
    if i > 3: # базовый случай
        return i     
    else:      
        print(rc(i+1),'for') # ркурсивный случай
    print(i,'two')
    return i
print(rc(1),'three') # вызывающий код


#def gt2(name):
    #print('h a y',name)
#def bye():
   # print('ok')
#def gt(name):
    #print('hel',name)
    #gt2(name)
    #print('getting bye')
    #bye()
#gt('mag')

""" Сумма с РОР"""
def sum(ar): 
    if len(ar)<=1:
        x=ar.pop(0)
        return x                 
    else:    
        x=ar.pop(0) 
        y=(sum(ar))         
    return x+y   
print(sum([2,4,7,1]))

""" Сумма с  list """
def sum(ls):
    if ls==[]:              
        return 0
    else:
        x=sum(ls[1:])+ls[0]       
    return x
print(sum([2,4,7,1]),'...') 

""" Сумма с  list в одну строку """
def sum(ls):
    if ls==[]:              
        return 0         
    return sum(ls[1:])+ls[0]
print(sum([2,4,7,1])) 

""" Счётчик с list """
def count(ls):
    print(ls,'.')
    if ls==[]:
        print(ls,'..')
        return 0
    else:
        x=count(ls[1:])+1
        print('\t'*1,x)
        print('\t'*2,ls[1:],'...',ls[0])
        #print(x,'/')
        return x
print(count([2,7,1]))

""" Счётчик с list в одну строку """
def count(ls):
    if ls==[]:             
        return 0       
    return count(ls[1:])+1 
print(count([2,7,1])) 


""" Максимальное значение с РОР"""
def max(ar):
    if len(ar)==2:
        return ar[0] if ar[0]>ar[1] else ar[1]
    else:
        x=ar.pop(0)
        y=ar[0]
        m=(max(ar))
        if m>x:
            return m
        if x>y:
            return x
print(max([6,62,31,14]))

""" Максимальное значение с РОР
         в одну строку"""
def max(ar):
    if len(ar)==2:
        print('\t',ar)
        return ar[0] if ar[0]>ar[1] else ar[1]
    x=ar.pop(0)
    print(x,'.')
    y=ar[0]
    print('\t'*1,y,'..')
    m=(max(ar))
    print('\t'*2,m,'m')
    return m if m>x else x if x>y else x
print(max([6,2,31,84]))

""" Минимальное значение с РОР
         в одну строку"""
def max(ar):
    if len(ar)==2:
        print('\t',ar)
        return ar[0] if ar[0]<ar[1] else ar[1]
    x=ar.pop(0)
    print(x,'.')
    y=ar[0]
    print('\t'*1,y,'..')
    m=(max(ar))
    print('\t'*2,m,'m')
    return m if m<x else x if m<y else y
print(max([6,2,31,5]))

""" Минимальное значение с РОР
         в одну строку"""
def max(ar):
    if len(ar)==2:
        return ar[0] if ar[0]<ar[1] else ar[1]
    x=ar.pop(0)
    y=ar[0]
    return (max(ar)) if (max(ar))<x else x if (max(ar))<y else y
print(max([56,2,31,15,4]))


# Рекурсия сложение чисел
# def foo():
#     x = input("enter : ")
#     if x == "":     # базовый случай
#         print(0.0)
#         return 0.0
#     else:
#         return float(x) + foo() # рекурсивный случай
# sum = foo()
# print(f" сумма = {sum}")

# Сумма каждых вторых элементов списка:

def foo(x):
    if not x:
        return 0
    return foo(x[2:]) + x[0]

print(f"Сумма каждых вторых элементов списка: {foo([3, 5, 7, 10, 15])}")

# Сумма элементов списка срезами
def foo(x, i=0):
    if i == 3:
        print(x[i-1:], x[1-i], i,">>>>")
        print(type(x))
        return 0
    print(x[i:], i)
    return foo(x, i + 1) + x[i]
print(f"Сумма элементов списка срезами: {foo([3, 5, 7])  }")

# Сумма элементов списка извлечение POP()
def foo(x):
    if not x:
        return 0
    print(x)
    y = x.pop(0)
    return foo(x) + y
print(f"Сумма элементов списка извлечение POP(): {foo([3, 5, 7])}")


# Быстрая сортировка Рекурсией
def foo(ar):
    if len(ar) < 2:  # Базовый случай
        return ar
    pivot = ar[0]  # Опорный элемент
    less = [x for x in ar[1:] if x < pivot]  # Ркурсивный случай, Уменьшение аргумента ar, массив в слева от опорного элемента
    greater = [x for x in ar[1:] if x > pivot]  # Ркурсивный случай, Уменьшение аргумента ar, но массив в справа от опорного элемента
    return foo(less) + [pivot] + foo(greater)  # Сложение списков в отсортированный список


print(f"Быстрая сортировка Рекурсией: {foo([5, 2, 4])}")


# Схема Рекурсии
"""
foo([3, 5, 7]) -> foo([5, 7]) + 3
                 -> foo([7]) + 5 + 3
                     -> foo([]) + 7 + 5 + 3
                         -> 0 + 7 + 5 + 3
                             -> 15

"""

"""
Прямой ход:
foo([3, 5, 7]) -> вызывает foo([5, 7]) -> вызывает foo([7]) -> вызывает foo([])
Обратный ход:
foo([]) = 0 -> foo([7]) = 0 + 7 = 7 -> foo([5, 7]) = 7 + 5 = 12 -> foo([3, 5, 7]) = 12 + 3 = 15

"""


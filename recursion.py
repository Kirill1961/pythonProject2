
def rc(i):
    print(i,'one')  
    if i >3: # базовый случай
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

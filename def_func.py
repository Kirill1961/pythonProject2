#import datetime


def d():
    import datetime
    a = datetime.date.today().day
    b = datetime.date.today().month
    c = datetime.date.today().year
    
    return (a, b, c)
if __name__ == '__main__' :
    print(d())

#d()

#v = d()

#def t():
#print(datetime.date.today())

#t()
#tv = t()

#def sv(word):
#vowels=set('aeiou')
#word=input('Provide a word to search for vowels:')
#found=vowels.intersection(set(word))
#for vowel in found:
#print(vowel)
#sv('aeiou')


def s4v(phrase: str) -> set:
    ''' принимает арг'''
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def s4l(phrase: str, letters: str = 'aeiou') -> set:
    return set(letters).intersection(set(phrase))


def ly(y):
    y = y * 3
    print(y)
    return (y)


def lx():
    ly(3)
    x = 2
    x = x * 2
    print(x)
    #ly(3)
    return (x)


lx()

km = {1, 2, 3}

""" Вызов ф-ции с аргументом из итерации  """
y = [54, 27, 301]
n = 0
while n < len(y):
    n += 1
def opt(x):
        print(x)
[opt(i)for i in y]


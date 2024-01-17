word = {'w', 't', 'u', 'l', 'f'}
frase = {'futur'}
for w in word:
    for f in frase:
        if w in f:
            print('ok')

""" Словарь из 2х множеств с генератором"""
print({w:f for w in word for f in frase if w in f})


""" Словарь из 2х множеств , обмен местами key/value с генератором"""
print({f:[w for w in word if w in f]for f in frase})

""" Множество из итерируемого множества, итерировать можно list или tuple """
print({i + 1000 for i in (j ** 2 for j in {1, 2, 3})})

print ([p for p in [x*3 for x in (1,2,3)]])

for p in [x*3 for x in (1,2,3,4,5)]:
    print(p)

for p in (x * 3 for x in (1, 2, 3, 4, 5)):
    print(p)


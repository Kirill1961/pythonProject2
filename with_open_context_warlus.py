fil = open('pass.txt', 'w')
fil.write('1,2,b,g')
print('  ', 'b  a  n  d', file=fil)
fil = open('pass.txt', 'r')
for it in fil:
    print(it)
fil.close()

a =lst = []
for i in range(5):
    fil = open('pass.txt', 'w')
    fil.write('q W e T')
    fil = open('pass.txt')
    for r in fil:
        print(r)
    lst.append(r)
    print(lst)

    fil.close()


# with open('pass.txt','w') as fi:
#     fi.write('1,5,9')
#     fi.write('ok')
# for i in fi:
#     print(i)

def v_t_l():
    contents = []

    with open('vs.log', 'w') as log:
        print('<a>', file=log)
        print('<b>', file=log)
        print('<c>', file=log)
        log.write('plot')
    with open('vs.log') as log:
        for line in log:

            contents.append([])

            for item in line.split('|'):
                contents[-1].append((item))
    return (str(contents))


print(v_t_l())

# Walrus - Читаем из txt и обрабатываем строки в своей директории
with open("file.txt") as files:
    while reader := files.readline():
        print(reader.strip(), "Walrus - Читаем из txt и обрабатываем строки")
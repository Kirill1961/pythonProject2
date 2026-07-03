fil = open("pass.txt", "w")
fil.write("1,2,b,g")
print("  ", "b  a  n  d", file=fil)
fil = open("pass.txt", "r")
for it in fil:
    print(it)
fil.close()

a = lst = []
for i in range(5):
    fil = open("pass.txt", "w")
    fil.write("q W e T")
    fil = open("pass.txt")
    for r in fil:
        print(r)
    lst.append(r)
    print(lst)

    fil.close()


with open('pass.txt','w') as fi:
    fi.write('1,5,9')
    fi.write('ok')
for i in fi:
    print(i)


def v_t_l():
    contents = []

    with open("vs.log", "w") as log:
        print("<a>", file=log)
        print("<b>", file=log)
        print("<c>", file=log)
        log.write("plot")
    with open("vs.log") as log:
        for line in log:

            contents.append([])

            for item in line.split("|"):
                contents[-1].append((item))
    return str(contents)


print(v_t_l())

# Walrus - Читаем из txt и обрабатываем строки в своей директории
with open("file.txt") as files:
    while reader := files.readline():
        print(reader.strip(), "Walrus - Читаем из txt и обрабатываем строки", "\n")

print(" Открываем, читаем, и останавливаем цикл по условию истинности :", "\n")
# " Открываем, читаем, и останавливаем цикл по условию истинности "
with open("names.csv", "r") as n:
    while True:
        n_ = n.readline()
        if n_:
            print(n_)
        else:
            break


print("Или так :", "\n")
with open("names.csv", "r") as n:
    while True:
        n_ = n.readline()
        print(n_)
        if not n_:
            break

# Запись из редактора в папку
path = r"C:\Users\Julia\Documents\results\forecast.txt"

with open(path, "w", encoding="utf-8") as f:
    f.write("Привет, мир!")

#%%
import numpy as np
import pandas as pd


data_new = pd.DataFrame(np.arange(1, 13).reshape(3, -1))

# TODO Запись датсета в файл csv на диске через to_csv
#  index=False — убирает лишний столбец индекса
data_new.to_csv('D:/Eduson_data/data_new.csv', index=False)


# TODO Запись датсета в файл csv на диске через numpy - savetxt
np.savetxt("D:/Eduson_data/2_wn.csv", data_new, delimiter=",")

#  TODO Создать папку в директории для файлов
import os
os.makedirs('D:/PROB')

# TODO Запись файла с DF в папку которая в дереве проекта
data_new.to_csv(r'C:\Users\Kirill\PycharmProjects\Practica\dataset\data_new.csv', index=False)
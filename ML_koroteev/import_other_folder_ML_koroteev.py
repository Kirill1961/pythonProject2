import os
import sys
# import a_safe_bernoulli as b
# from ML_koroteev import simple_analysis_open_py_xl as o

print(os.getcwd(), " Р а с п о л о ж е н и е данного файла ", "\n")  # os.getcwd() - место расположение файла где мы находимся
# print(os.path.join(os.getcwd()))

k = sys.path.append(os.path.join(os.getcwd(), "..", "bbb"))  # sys.path.append() - добавит указанные пути
k_ = sys.path.append(os.path.join(os.getcwd(), "..", "a_ae"))  # os.path.join - сцепляет указанные отрезки пути


print(sys.path, ".....................")

print(k, ">>>>>>>>>>>>>>>>>>>>")

# print(b.f() , "функция из файла map.py")
# print(o.count_vs_while(2), "> > > функция из файла simple_analysis_open_py_xl.py > > >")
from lesson import map
map.app_end([90, 80, 70])


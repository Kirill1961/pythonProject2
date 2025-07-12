import pandas as pd
import openpyxl
import glob
import matplotlib.pyplot as plt
import os
import sys


# print(os.getcwd(), " Р а с п о л о ж е н и е данного файла ", "\n")
sys.path.append(os.path.join(os.getcwd(), r"D:\downloads\Spam_Asassians\data_koroteev\data3.xlsx"))
path = r"D:\downloads\Spam_Asassians\data_koroteev\data3.xlsx"
print(os.path.exists(path))  # Проверить, существует ли файл по этому пути
files = glob.glob(path)
print(files[0])
tabl = pd.read_excel(files[0], engine='openpyxl', skiprows=2)
print(tabl)
# path = r"D:\downloads\SPAM Assassian\data_koroteev\data3.xlsx"

# path = r"C:\Users\Kirill\PycharmProjects\pythonProject2\ML_koroteev\data_base_1.csv"
# data_2 = pd.read_csv(files[0])
# print(data_2)
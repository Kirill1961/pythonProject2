import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv\
    ("https://raw.githubusercontent.com/koroteevmv/ML_course/2023/ML2.2%20real%20classification/data/diabetes.csv")
print(data.head())

data_1 = pd.read_csv("data_base_1.csv")
print(data_1.head())
#
# X = data.x
# y = data.y
#
# plt.scatter(X, y)

# x = pd.read_csv('https://raw.githubusercontent.com/koroteevmv/ML_course/2023/ML1.1%20linear%20regression/data/x.csv')
# y = pd.read_csv('https://raw.githubusercontent.com/koroteevmv/ML_course/2023/ML1.1%20linear%20regression/data/y.csv')
#
# print(x.head())
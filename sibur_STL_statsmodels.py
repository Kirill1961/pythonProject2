"""
Dataset sibur создаём признаки и целевые
* Выявляем сезонность
* Вычисляем частоту в index признаков через pd.infer_freq(), для окна rolling
* Подбираем размер окна для rolling(H) по сезонности
"""

import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose, STL
from statsmodels.tsa.ardl import ardl_select_order
from statsmodels.datasets.danish_data import load
from statsmodels.tsa.api import ARDL

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # или 'Qt5Agg', если есть Qt5

# TODO data train test target

df_tr = pd.read_csv('D:\Eduson_data\sibur_train_features.csv')

df_ts = pd.read_csv('D:\Eduson_data\sibur_test_features.csv')

df_tg = pd.read_csv('D:\Eduson_data\sibur_train_targets.csv')

df_sb = pd.read_csv('D:\Eduson_data\sibur_sample_submission.csv')

print(df_tr.columns, '\n')
print(df_ts.columns, '\n')
print(df_tg.columns, '\n')
print(f' train : {df_tr.shape} \n test : {df_ts.shape}'
      f' \n target : {df_tg.shape} \n submisiion : {df_sb.shape}', '\n')

# TODO exp на train выборке
df_tr['timestamp'] = pd.to_datetime(df_tr['timestamp'])

df_tr = df_tr.set_index('timestamp')

print(df_tr.index, '\n')

print(df_tr.index.freq, '\n')

print(pd.infer_freq(df_tr.index), '\n')

stl = STL(df_tr['A_CH4'], period=48)  # period = предполагаемый сезонный цикл

res = stl.fit()

res.plot()

plt.show()

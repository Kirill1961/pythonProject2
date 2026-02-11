import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from statsmodels.tsa.seasonal import seasonal_decompose, STL

# import matplotlib.pyplot as plt

from statsmodels.tsa.ardl import ardl_select_order
from statsmodels.datasets.danish_data import load
from statsmodels.tsa.api import ARDL



# TODO data train test target

df_tr = pd.read_csv('D:\Eduson_data\sibur_train_features.csv')

df_ts = pd.read_csv('D:\Eduson_data\sibur_test_features.csv')

df_tg = pd.read_csv('D:\Eduson_data\sibur_train_targets.csv')

df_sb = pd.read_csv('D:\Eduson_data\sibur_sample_submission.csv')

print(df_tg.columns, '\n')
print(df_tr.columns, '\n')
print(df_ts.columns, '\n')
print(f' train : {df_tr.shape} \n test : {df_ts.shape}'
      f' \n target : {df_tg.shape} \n submisiion : {df_sb.shape}', '\n')


df_tg['timestamp'] = pd.to_datetime(df_tg['timestamp'])

df_tg = df_tg.set_index('timestamp')

print(df_tg['B_C2H6'])

print('Частота : \n', pd.infer_freq(df_tg['B_C2H6'].index))

stl = STL(df_tg['B_C2H6'],  period=7)  # period = предполагаемый сезонный цикл

res = stl.fit()

res.plot()
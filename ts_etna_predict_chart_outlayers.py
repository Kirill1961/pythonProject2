"""
pandas - полный вывод таблицы
"""

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


import numpy as np

from datetime import date, datetime, timedelta
import datetime

import matplotlib

# matplotlib.use("Agg")
matplotlib.use("TkAgg")
# matplotlib.use("QtAgg")
# matplotlib.use("WebAgg")
import matplotlib.pyplot as plt

import plotly.express as px

from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose, STL

from etna.datasets import generate_const_df
from etna.datasets import TSDataset
from etna.analysis import acf_plot
from etna.analysis import plot_correlation_matrix

#%%
# TODO data

data = pd.read_csv('D:\Eduson_data\example_dataset.csv')
data1 = pd.read_csv('D:\Eduson_data\monthly_australian_wine_sales.csv')
data2 = pd.read_csv('D:\Eduson_data\online_retail.csv')


exog = data.copy()

exog['lag1'] = exog['target'].shift(1).astype(float).interpolate(limit_direction='both')
#%%

data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)
# TSDataset(data, freq='M')
data.dtypes

#%%
# TODO TSDataset describe

# Число сегментов
print(data['segment'].unique())

# to_dataset - можно не делать тк TSDataset сам всё сделает
df = TSDataset.to_dataset(data)

ts = TSDataset(df, freq='D')

ts.describe()

ts.info()

#%%
# TODO ts.plot

ts.plot()
plt.show()

#%%
# TODO ACF PACF
acf_plot(ts, lags=21)
plt.show()




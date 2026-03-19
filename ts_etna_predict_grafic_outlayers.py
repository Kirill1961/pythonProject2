import pandas as pd
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

#%%
# TODO data

data = pd.read_csv('D:\Eduson_data\example_dataset.csv')
data1 = pd.read_csv('D:\Eduson_data\monthly_australian_wine_sales.csv')
data2 = pd.read_csv('D:\Eduson_data\online_retail.csv')

#%%

data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)
# TSDataset(data, freq='M')
data.dtypes



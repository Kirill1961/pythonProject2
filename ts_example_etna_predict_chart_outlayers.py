"""
pandas - полный вывод таблицы
"""

import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)


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
from etna.analysis import (
    acf_plot,
    plot_correlation_matrix,
    cross_corr_plot,
    distribution_plot,
    plot_trend,
    stl_plot,
    seasonal_plot,
)
from etna.transforms import LagTransform
from etna.transforms import LinearTrendTransform

from etna.datasets import TSDataset  # импорт через публичный API
from etna.datasets.tsdataset import TSDataset  # импорт напрямую из внутреннего модуля

# %%
# TODO data

data = pd.read_csv("D:\Eduson_data\example_dataset.csv")
data1 = pd.read_csv("D:\Eduson_data\monthly_australian_wine_sales.csv")
data2 = pd.read_csv("D:\Eduson_data\online_retail.csv")

# %%
# TODO Лаг по сегментам
data_ex = data.copy()
data_ex["lag1"] = data_ex.groupby("segment")["target"].shift(1)
data_ex["lag1"] = data_ex["lag1"].interpolate(limit_direction="both")
# %%

data["timestamp"] = pd.to_datetime(data["timestamp"])
data.set_index("timestamp", inplace=True)
# TSDataset(data, freq='M')
data.dtypes

# %%
# TODO TSDataset describe

# Число сегментов
print(data["segment"].unique())

# to_dataset - можно не делать тк TSDataset сам всё сделает
df = TSDataset.to_dataset(data)

ts = TSDataset(df, freq="D")

ts.describe()

ts.info()

# %%
# TODO ts.plot

ts.plot()
plt.show()

# %%
# TODO ACF через ETNA acf_plot

acf_plot(ts, lags=21)
plt.show()

# %%
# TODO EDA vmin, vmax - Граница цветовой шкалы
#  Заданные Лаги через LagTransform и Heatmap сегментов целевой с её лагами

lag = LagTransform(in_column="target", lags=[1, 2, 3], out_column="lag")

ts.fit_transform([lag])

# Корреляция Лагов временных рядов
plot_correlation_matrix(
    ts,
    columns=["lag_1", "lag_2", "target"],
    segments=["segment_a", "segment_b"],
    method="spearman",
    vmin=0.5,
    vmax=1,
)
plt.show()

# Корреляция временных рядов друг с другом
plot_correlation_matrix(
    ts,
    columns=["target", "lag_2", "lag_3"],
    segments=["segment_a", "segment_b", "segment_c", "segment_d"],
    method="spearman",
    vmin=0.5,
    vmax=1,
)
plt.show()

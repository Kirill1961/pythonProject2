import pandas as pd
import numpy as np

from datetime import date, datetime, timedelta
import datetime

import matplotlib

# matplotlib.use("Agg")
matplotlib.use("TkAgg")
# matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose, STL

#%%
# TODO data
#  Параметр λ (lambda), lam=30 — это среднее число событий за интервал 10min.
date_rng = pd.date_range("2018-03-01", "2018-08-31 23:50", freq="10min")

np.random.seed(42)
# orders = np.random.poisson(lam=30, size=len(date_rng))
orders = np.sort(np.random.poisson(lam=30, size=len(date_rng)))

trend = 0.0001 * np.arange(len(orders))

# trend = 0

# orders = 0.2 * orders + (1 - 0.2) * orders


# season_day = 5 * np.sin(2 * np.pi * np.arange(len(orders)) / 144)
season_day = 5 * np.sin(2 * np.pi * np.arange(len(orders)) / 144)


# season_day = 0

orders_trend = orders + trend + season_day


df = pd.DataFrame({"num_orders": orders_trend}, index=date_rng)

# df1 = pd.DataFrame({'num_orders': orders}, index=date_rng)

df.index.name = "datetime"

print(df.head())
# print(df1.head())

print(df.shape)
# print(df1.shape)


print(df.min(), df.max())

#%%
# TODO Декомпозиция через STL

stl = STL(endog=df["num_orders"], period=144)

res = stl.fit()

res.plot()
plt.show()

#%%
# TODO Декомпозиция через acf

plot_acf(df.num_orders, lags=30)
plt.show()

#%%
# TODO frequency & period
print(pd.infer_freq(df.index))
df.diff().value_counts()

#%%
# TODO train и test через percentile
train_size = np.percentile(df, 90)
train = df[df['num_orders'] < train_size]
test = df[~(df['num_orders'] < train_size)]

#%%
# TODO target


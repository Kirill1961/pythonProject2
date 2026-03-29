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
# TODO MY data
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


df = pd.DataFrame({"datetime": date_rng,  "num_orders": orders_trend})

# df1 = pd.DataFrame({'num_orders': orders}, index=date_rng)

# df.index.name = "datetime"

print(df.head())
# print(df1.head())

print(df.shape)
# print(df1.shape)

print(df.min(), df.max())

# 1️⃣ TODO Eduson taxi/data
#%%

df = pd.read_csv(r"D:/Eduson_data/taxi.csv")


#%%
# TODO Декомпозиция через STL, подбор периода

stl = STL(endog=df["num_orders"], period=6*24*14)

res = stl.fit()

res.plot()
plt.show()

#%%
# TODO Декомпозиция через acf + diff(1) / diff(24)
df['datetime'] = pd.to_datetime(df['datetime'])
df = df.set_index('datetime')

df['num_orders'] = df['num_orders'].diff(1)  # Убираем тренд
# df['num_orders'] = df['num_orders'].diff(24)  # Убираем сезон

df.dropna(inplace=True, axis=0)

plot_acf(df.num_orders, lags=30)
plt.show()


#%%
# TODO frequency & period
print('infer_freq >>> ', pd.infer_freq(df.index))
df.diff().value_counts()

#%%
# TODO train и test через percentile и IndexSlice
idx = pd.IndexSlice
row_end = pd.to_datetime(np.percentile(df.index, 90))
# train_start = df.index[0]

# 1️⃣ Просто срез можно, 👉 но при type datetime
tr = df[df.index[0]: row_end]

# 2️⃣ Срез через IndexSlice
train = df.loc[idx[:row_end]]
test = df.loc[idx[row_end:]]

# 3️⃣ Срез через len
split = int((len(df) * 0.9))
trn = df.iloc[: split]
tst = df.iloc[split:]

print(trn.index.max())
print(tst.index.min())


#%%
# TODO wide long table через melt
df = pd.DataFrame(np.random.randint(1, 15, size=9).reshape(-1, 3),
                  columns=list("ABC"),
                  index=pd.date_range('01-01-2005', periods=3, freq='10D')
                  )
df.index.name = 'timestamp'

print('Исходный : \n', df, '\n')

freq = pd.infer_freq(df.index)

df = df.reset_index().melt(id_vars="timestamp", var_name="segment", value_name="target")

ts = TSDataset(df=df, freq=freq)

print('long table :\n', df, '\n')

print('TSDataset :\n', ts)

#%%
# TODO  long -> wide через to_dataset()

df = pd.DataFrame(
    np.random.randint(1, 15, size=9).reshape(-1, 3),
    columns=list("ABC"),
    index=pd.date_range("2005-01-01", periods=3, freq="10D")
)

df.index.name = 'timestamp'

freq = pd.infer_freq(df.index)

df = df.reset_index().melt(id_vars="timestamp", var_name="segment", value_name="target")

print('long table :\n', df, '\n')

df = TSDataset.to_dataset(df)

print('wide table :\n', df, '\n')

#%%
# 2️⃣ TODO lesson, convert через strftime

df.info()

print(df.datetime.min(), df.datetime.max())

df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S')

# Convert data через strftime
print(df.datetime.dt.strftime('%d-%m-%Y'))

#%%
# TODO графики, plotly через 'browser', дату на лету переносим в индекс
# 📈
df.set_index('datetime').plot(title="taxi")
plt.show()

# 📈
# plt.plot(df.set_index('datetime'))
# plt.show()

# 📈
import plotly.io as pio
pio.renderers.default = 'browser'
# pio.renderers.default = 'svg'
# pio.renderers.default = 'png'

# fig = px.line(df, x='datetime', y='num_orders')
# fig.set_size_inches(8, 4)
# fig.show()





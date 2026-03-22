import random
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

from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose, STL

from etna.datasets import TSDataset
from etna.transforms import LagTransform
from etna.transforms import LinearTrendTransform
from etna.analysis import acf_plot

# %%
# TODO функция генерит df
def foo(flag=False):
    dt = pd.date_range("2020-01-01", periods=6, freq="ME")

    df = pd.DataFrame(
        np.array(list("wwwsssfffvvvqqqddd")).reshape(-1, 3),
        columns=list("ABC"),
        index=dt,
    )

    df1 = pd.DataFrame(np.arange(1, 19).reshape(-1, 3), columns=list("ABC"), index=dt)

    if flag == True:
        df = df.rename(columns={"C": "y=C"})

        df["lag_1"] = df["A"].shift(periods=1)
        df["lag_2"] = df["B"].shift(periods=2)

        # df = df.drop('C', axis=1)

        df["y_1"] = df["y=C"].shift(-1)
        df["y_2"] = df["y=C"].shift(-2)

        #  Переставить столбцы через reindex - для красоты, тк 'y=C' удаляется
        df = df.reindex(["A", "B", "lag_1", "lag_2", "y=C", "y_1", "y_2"], axis=1)

        print("Признаки и Целевые в одном df, Заготовка :\n\n  ", df, "\n")

        df = df.drop("y=C", axis=1).dropna()

        print(
            "Признаки и Целевые в одном df, Готовые к следующим этапам :\n\n  ",
            df,
            "\n",
        )

    return df, df1


foo(flag=True)

# %%
df_init = foo(flag=False)
df_init

# %%
# TODO генерим ts
dt = pd.date_range("2010-01-01", periods=6, freq="ME")

df = pd.DataFrame(
    np.array(list("wwwsssfffvvvqqqddd")).reshape(-1, 3), columns=list("ABC"), index=dt
)

df1 = pd.DataFrame(np.arange(1, 19).reshape(-1, 3), columns=list("ABC"), index=dt)

print("Исходный df : \n", df, "\n")

# %%
# TODO генерим df, тип даты object
df = pd.DataFrame(
    {
        "month": pd.date_range("2010-01-01", periods=12, freq="ME").astype(str),
        "val": np.arange(10, 130, 10),
    }
)

df.dtypes
# %%
#
# TODO создаём лаговые признаки и лаговые целевые
df["x_lag1"] = df["A"].shift(1)
df["x_lag2"] = df["B"].shift(2)
df["y_lag1"] = df["A"].shift(-1)
df["y_lag2"] = df["B"].shift(-2)

df

# %%
df.ffill(inplace=True)

df

# %%
df.bfill(inplace=True)

df

# %%
# TODO Вызов df и df1 через foo
df, df1 = foo(flag=False)

df
# %%
# TODO sample_submission
#  * Инициализация sample_submission = 0, замена нулей на значения
df_sub = df.copy()

# df_sub[['A', 'B', 'C']] = df_sub.iloc[:, :] = 0

df_sub.iloc[:, :] = 0

df_sub

# %%
df_sub = df1

df_sub

# %%
# TODO Кастомная CV
#  окно для cv через numpy, с шагом 5
#  i * 5 - это скользящее окно

# фолд = 10 строк
# шаг окна = 5 строк
# число фолдов = 10
# размер df2 = (100, 3)
df2 = pd.DataFrame(np.arange(1, 301).reshape(-1, 3), columns=list("ABC"))

# train = df2.iloc[:71, :]
# test = df2.iloc[70:, :]

cv_idx = [[np.arange(0 + i * 5, 10 + i * 5), np.arange(0, 10)] for i in range(10)]

cv_idx

# %%
# TODO Вывод train и test по idx от скользящего окна
for idx_tr, idx_ts in cv_idx:
    print(f"TRAIN : \n {df2.iloc[idx_tr, :].head(2)}")
    print(f"TEST : \n {df2.iloc[idx_ts, :].head(2)}")

# %%
# TODO Интервал ряда между наблюдениями
#  diff() - Это разница между всеми соседними значениями в наборе данных
np.random.seed(0)
dt = pd.date_range(start="1/1/2020", end="12/31/2020", freq="0.5h")

ts = pd.DataFrame(
    np.random.randint(1, 100, size=dt.shape[0] * 3).reshape(-1, 3),
    columns=["x1", "x2", "Y"],
    index=dt,
)

# %%
# TODO Интервал ряда между наблюдениями простой способ, если расстояния идеально одинаковы
print(
    "Интервал если расстояния идеально одинаковы : \n", ts.index[0] - ts.index[1], "\n"
)

print(
    "Интервал если infer_freq неизвестный: \n",
    ts.index.diff().to_series().value_counts(),
)

# %%
# TODO Один временной ряд "main", Подготовка df к TSDataset
df["timestamp"] = pd.to_datetime(df["month"])
df["target"] = df["val"].shift(-1)
df["segment"] = "main"
df = df.drop(["month", "val"], axis=1)

df

# %%
# TODO ts - slice на прямую и через to_pandas
np.random.seed(0)
dt = pd.date_range(start="1/1/2020", end="12/31/2020", freq="ME")

df = pd.DataFrame(
    {"timestamp": dt, "target": np.random.randint(1, 100, size=dt.shape[0])}
)

df["segment"] = "main"

ts = TSDataset(df, freq="ME")

# Через to_pandas
print(ts.to_pandas().iloc[:3])

# На прямую
print(ts["2020-04-30":"2020-06-30"])

# print(ts[:5, :, :])             # первые 5 точек
# print(ts[:, 'segment_b', :])      # один сегмент
# print(ts[:, :, 'target'])          # только target
# ts['2020':'2021', :, :]       # по датам

# %%
# TODO LagTransform - создание лагов pipline и в ручную

np.random.seed(4)
df = pd.DataFrame(
    {
        "TS": pd.date_range("2020-01-01", periods=12, freq="ME"),
        "A": np.random.randint(0, 2, size=12),
        "B": np.round(np.random.rand(12), 3),
    }
)

df.rename(columns={"TS": "timestamp"}, inplace=True)

ds = df.melt(id_vars="timestamp", var_name="segment", value_name="target")

ts = TSDataset(ds, freq="ME")

# 1️⃣ pipeline-стиль, [lag] - список трансформов
lag = LagTransform(in_column="target", out_column="target_lag", lags=[1, 3])

ts.fit_transform([lag])

print(ts)

# 2️⃣ Ручной стиль
# lag = LagTransform(in_column='target', out_column='lag', lags=[1, 3])
#
# lag.fit_transform(ts)
#
# ts.head()

# %%
# TODO LinearTrendTransform
#  Графики принимают более горизонтальное положение после LinearTrendTransform
df = pd.read_csv("D:\Eduson_data\example_dataset.csv")

ts = TSDataset(df, freq='D')

ts.plot()
plt.show()

dtrend = LinearTrendTransform(in_column='target', poly_degree=3)

dtrend.fit_transform(ts)

ts.plot()
plt.show()

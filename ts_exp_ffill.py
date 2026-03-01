import random
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta
import datetime
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose, STL


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


#%%
# TODO Вывод train и test по idx от скользящего окна
for idx_tr, idx_ts in cv_idx:
    print(f'TRAIN : \n {df2.iloc[idx_tr, :].head(2)}')
    print(f'TEST : \n {df2.iloc[idx_ts, :].head(2)}')






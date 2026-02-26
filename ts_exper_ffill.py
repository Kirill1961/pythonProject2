
import random
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta
import datetime
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose, STL

#%%
def foo(flag=False):
    dt = pd.date_range('2020-01-01', periods=6, freq='ME')

    df = pd.DataFrame(np.array(list('wwwsssfffvvvqqqddd')).reshape(-1, 3),
                      columns=list('ABC'), index=dt)

    df = df.rename(columns={'C': 'y=C'})

    if flag == True:
        df['lag_1'] = df['A'].shift(periods=1)
        df['lag_2'] = df['B'].shift(periods=2)

        # df = df.drop('C', axis=1)

        df['y_1'] = df['y=C'].shift(-1)
        df['y_2'] = df['y=C'].shift(-2)

        #  Переставить столбцы через reindex - для красоты, тк 'y=C' удаляется
        df = df.reindex(['A', 'B', 'lag_1', 'lag_2', 'y=C', 'y_1', 'y_2'], axis=1)

        print('Признаки и Целевые в одном df, Заготовка :\n\n  ', df, '\n')

        df = df.drop('y=C', axis=1).dropna()

        print('Признаки и Целевые в одном df, Готовые к следующим этапам :\n\n  ', df, '\n')

    return df


foo(flag=True)

#%%
df_init = foo(flag=False)
df_init


#%%
# TODO генерим ts
dt = pd.date_range('2010-01-01', periods=6, freq='ME' )

df = pd.DataFrame(np.array(list('wwwsssfffvvvqqqddd')).reshape(-1, 3),
                  columns=list('ABC'), index=dt)

df1 = pd.DataFrame(np.arange(1, 19).reshape(-1, 3),
                  columns=list('ABC'), index=dt)

print('Исходный df : \n', df, '\n')

#%%
# TODO создаём лаговые признаки и лаговые целевые
df['x_lag1'] = df['A'].shift(1)
df['x_lag2'] = df['B'].shift(2)
df['y_lag1'] = df['A'].shift(-1)
df['y_lag2'] = df['B'].shift(-2)

df

#%%
df.ffill(inplace=True)

df

#%%
df.bfill(inplace=True)

df

#%%
# TODO data train test target
df_tr = pd.read_csv('D:\Eduson_data\sibur_train_features.csv')

df_ts = pd.read_csv('D:\Eduson_data\sibur_test_features.csv')

df_tg = pd.read_csv('D:\Eduson_data\sibur_train_targets.csv')

df_sb = pd.read_csv('D:\Eduson_data\sibur_sample_submission.csv')

print(df_tr.columns)
print(df_ts.columns)
print(df_tr.shape, df_ts.shape, df_tg.shape, df_sb.shape)

#%%
df_tr['A_rate'][0]
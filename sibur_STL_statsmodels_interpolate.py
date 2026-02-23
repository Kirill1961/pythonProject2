"""
Dataset sibur создаём признаки и целевые
* Выявляем сезонность
* Вычисляем частоту в index признаков через pd.infer_freq(), для окна rolling
* Подбираем размер окна для rolling(H) по сезонности
"""

# TODO START
from typing import Iterable

import numpy as np
import pandas as pd
from pandas import DataFrame
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

print('train :\n', df_tr.columns, '\n')
print('test  :\n', df_ts.columns, '\n')
print('target :\n', df_tg.columns, '\n')
print(f' train : {df_tr.shape} \n test : {df_ts.shape}'
      f' \n target : {df_tg.shape} \n submisiion : {df_sb.shape}', '\n')

print('infer_freq :\n', pd.infer_freq(df_tr['timestamp']), '\n')

# TODO init train
df_tr['timestamp'] = pd.to_datetime(df_tr['timestamp'])

df_tr = df_tr.set_index('timestamp')

# print('df_tr.index :\n', df_tr.index, '\n')
#
# print('df_tr.index.freq :\n ', df_tr.index.freq, '\n')

# TODO init target
df_tg['timestamp'] = pd.to_datetime(df_tg['timestamp'])

df_tg = df_tg.set_index('timestamp')


#%%
# TODO STL
#  STL не отыскивает сезон, задавая period= ... мы формируем гипотезу о размере season, число наблюдений в сезоне
def run_stl(data: DataFrame, samples: Iterable[str], period: int, plot=False):
    res_stl = {}

    for sample in samples:
        # TODO limit_direction="both" - Заполнение NA в начале и в конце df, astype(float) - перестраховка типа данных
        feature = data[sample].astype(float).interpolate(limit_direction="both")

        stl = STL(feature, period=period)  # period = предполагаемый сезонный цикл

        res = stl.fit()

        if plot:
            res.plot()

        res_stl[sample] = res

    if plot:
        plt.show()

    return res_stl


run_stl(df_tr, df_tr.columns, 48, plot=True)


#%%
# TODO оценка качества сезонности через std и isna, проверяем наличие сезонности
def estimate_season(data, samples, period):
    res_estim = run_stl(data, df_tr.columns, 48, plot=False)

    for sample in samples:
        res = res_estim[sample]

        print(f'seasonal : {sample} = {res.seasonal.std()}')
        print(f'trend : {sample} = {res.trend.std()}')
        print(f'resid : {sample} = {res.resid.std()}')
        print(f'seasonal.isna : {sample} = {res.seasonal.isna().sum()}')
        print(f'trend.isna : {sample} = {res.trend.isna().sum()}', '\n')
        print(f'***********\n ratio std: {sample} = {res.seasonal.std() / res.resid.std()}')
        print(f' variance explained: {sample} = {1 - np.var(res.seasonal) / np.var(res.seasonal + res.resid)}', '\n')


estimate_season(df_tr, df_tr.columns, 48)


#%%
# TODO оценка ряда перед использованием в STL
def estimator(data, samples, period: int):
    for sample in samples:
        s = data[sample]
        print("unique:", s.nunique())  # если unique ≈ len(data) сигнал не квантованный ≈ не дискретный
        print("std:", s.std())  # std > 0, чем больше std тем больше вариативность, хорошо для LOESS
        print("diff std:", s.diff().std())  # diff.std > 0 → локальная динамика есть
        print("value counts head:")
        print(s.value_counts()[s.value_counts() > 5], '\n')  # Если значение залипло - повторяется много раз → плохо


estimator(df_tr, df_tr.columns, 48)


#%%
# TODO Наличе сезонности по графику через среднее группировки по hour или day_week
def indicator_sesone(data, samples, period):
    df_tr['day_week'] = df_tr.index.day_of_week  # Создание временных признаков
    df_tr['day'] = df_tr.index.day
    df_tr['hour'] = df_tr.index.hour

    data.groupby('day').mean().plot()
    data.groupby('day_week').mean().plot()
    data.groupby('hour').mean().plot()
    plt.show()

indicator_sesone(df_tr, df_tr.columns, 48)

# TODO сила/слабость сезонности в % от std
#  Добавим столбец дни недели, и groupby по столбцу day
# df_tr['day'] = df_tr.index.day_ofweek()
# g = df_tr.groupby('day').mean()
# (g.max() - g.min()) / df_tr.std()

print(df_tr.isna().any())

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
    plot_periodogram,
    get_anomalies_density,
    get_anomalies_median,
    plot_anomalies,
    find_change_points,
    plot_change_points_interactive,
    plot_time_series_with_change_points
)
from ruptures.detection import Binseg

from etna.transforms import LagTransform
from etna.transforms import LinearTrendTransform

from etna.datasets import TSDataset  # импорт через публичный API
from etna.datasets.tsdataset import TSDataset  # импорт напрямую из внутреннего модуля

# %%
# 1️⃣ TODO data

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
# 2️⃣ TODO TSDataset describe

# Число сегментов
print(data["segment"].unique())

# to_dataset - можно не делать тк TSDataset сам всё сделает
df = TSDataset.to_dataset(data)

ts = TSDataset(df, freq="D")

ts.describe()

ts.info()

# %%
# TODO ts.plot
ts.plot(figsize=(5, 3))
plt.show()

# %%
# TODO ACF через ETNA acf_plot
acf_plot(ts, lags=21, figsize=(5, 3))
plt.show()

#%%
# TODO PACF то же через acf_plot
acf_plot(ts, lags=21, figsize=(5, 3), partial=True)
plt.show()

#%%
# TODO Корреляция рядов между собой
plot_correlation_matrix(
    ts,
    columns=["target"],
    segments=["segment_a", "segment_b", "segment_c", "segment_d"],
    method="spearman",
    vmin=0.5,
    vmax=1,
    figsize=(10, 10)
)
plt.show()

# %%
# TODO Задаём  Лаги для plot_correlation_matrix
#  EDA vmin, vmax - Граница цветовой шкалы
#  Задаём  Лаги через LagTransform и Heatmap сегментов целевой с её лагами

lag = LagTransform(in_column="target", lags=[2, 3, 4, 7], out_column="lag")

ts.fit_transform([lag])

#%%
# TODO Корреляция Лагов временных рядов
#  Если сравнить heatmap с ACF то результаты совпадут
plot_correlation_matrix(
    ts,
    columns=['lag_2', "lag_3", "lag_4", 'lag_7', "target"],
    segments=["segment_a"],
    method="spearman",
    vmin=0.5,
    vmax=1,
    figsize=(5, 5)
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
    figsize=(10, 10)
)
plt.show()

#%%
# TODO Перекрестная корреляция - Cross-correlation

cross_corr_plot(ts, maxlags=100, figsize=(7, 2))

#%%
# TODO TREND
#  plot_trend - Визуализация  тренда для каждого сегмента
#  выбор подходящей модели для его описания
#  LinearTrendTransform - Преобразование, использующее Лин. Регр. с полиномиальными признаками для удаления тренда.

trends = [
    LinearTrendTransform(in_column="target", poly_degree=1),
    LinearTrendTransform(in_column="target", poly_degree=2)
]

plot_trend(ts, trend_transform=trends, figsize=(7, 5))
plt.show()

#%%
# TODO Удаляем тренд и обучаем модель
transform = LinearTrendTransform(in_column="target", poly_degree=1)
ts.fit_transform([transform])

ts.plot(figsize=(5, 3))
plt.show()

#%%
#  SEASON Методы Анализа Сезонности: plot_periodogram, seasonal_plot, stl_plot
# TODO визуализиция амплитуды компонент Фурье
#  Spectral - разобрали на частоты по Фурье
#  Power - нашли силу (вклад) каждой частоты,
#  Density - распределили эту силу по оси частот

plot_periodogram(ts,
                 period=365.2425,
                 amplitude_aggregation_mode="per-segment",
                 xticks=[1, 2, 4, 6, 12, 26, 52, 104],
                 figsize=(6, 3)
                 )
plt.show()

#%%
# TODO STL Визуализация разложения - Декомпозиция ряда
#   plot_periodogram - пик указал на период 1/52 года ~ неделя, этот период возьмём для stl_plot
stl_plot(ts=ts, period=52, figsize=(6, 3))
plt.show()

#%%
# TODO seasonal_plot - визуализация конкретного периода сезонности (час, день, неделя, месяц, квартал, год)
seasonal_plot(ts=ts, cycle="quarter", figsize=(6, 3))
plt.show()

#%%
# TODO distribution_plot - Распределение z-значений, сгруппированных по сегментам и временной частоте
#  После z-нормирования сравниваем сегменты: Шум, Стабильность распределения, Выбросы
distribution_plot(ts, freq="1Y", figsize=(5, 3))
plt.show()

#%%
# TODO Outliers / Выбросы
#  Метод медианы
anomaly_dict = get_anomalies_median(ts, window_size=100)
plot_anomalies(ts, anomaly_dict, figsize=(5, 3))

#%%
# TODO Метод определения плотности, локально на отрезках
#  ищем аномалии через локальную плотность значений ряда
anomaly_dict = get_anomalies_density(ts)
plot_anomalies(ts, anomaly_dict, figsize=(5, 3))

#%%
#  TODO Добавим параметры:
#   distance_coef=1 - дистанция не аномального расстояния до соседа
#   n_neighbors=4 - число соседей меньше которого точка - аномальная
anomaly_dict = get_anomalies_density(ts, window_size=18, distance_coef=1, n_neighbors=4)
plot_anomalies(ts, anomaly_dict, figsize=(5, 3))

#%%
# TODO Change Point
#  Args:
#          n_bkps (int): number of breakpoints to find before stopping.
#          penalty (float): penalty value (>0), штраф (penalty) за добавление новой точки изменения.
#          epsilon (float): reconstruction budget (>0)
#          min_size (int, optional): minimum segment length, min num observer between two points, Defaults to 2 samples.

change_points = find_change_points(ts=ts, in_column="target", change_point_model=Binseg(), pen=1e5)  # 1e5 = 100000
plot_time_series_with_change_points(ts=ts, change_points=change_points, figsize=(5, 3))

#%%
# TODO интерактивные методы разведочного анализа данных (EDA)

params_bounds = {"n_bkps": [1, 8, 2], "min_size": [0, 10, 3]}
plot_change_points_interactive(
    ts=ts,
    change_point_model=Binseg,
    model="l2",
    params_bounds=params_bounds,
    model_params=["min_size"],
    predict_params=["n_bkps"],
    figsize=(5, 3),
)
plt.show()
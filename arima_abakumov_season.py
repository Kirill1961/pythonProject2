"""
1 dataset из pmdarima
2 Сам добавил индекс 'timestamp'
3 Преобразовали мультипликативный ряд в аддитивный через log10
4 Через auto_arima подобрали модель и параметры
5 Подгонка и прогноз fit + predict
6 Обратно масштабировали датасет через 10**log10
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

import pmdarima as pm
from pmdarima.datasets import load_airpassengers

from statsmodels.tsa.seasonal import seasonal_decompose, STL
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
#%%
# TODO data_pmdarima
data_p = load_airpassengers(True)

data_p.head()

data_p.shape

#%%
# TODO index, Сам добавил индекс
data_p.index = pd.date_range('01-01-2020', periods=len(data_p), freq='D', name='timestamp')
data_p.index
#%%
# TODO Мультипликативный ряд
data_p.plot(figsize=(7, 3))

plt.xlabel('data')
plt.ylabel('quantity')
plt.title('pass transport')
plt.show()

#%%
# TODO Логарифмирование
data_p_add = np.log10(data_p)
data_p_add.head()
#%%
# TODO Аддитивный ряд
data_p_add.plot(figsize=(7, 3))

plt.xlabel('data')
plt.ylabel('quantity')
plt.title('pass transport')
plt.show()

#%%
# TODO aut_arima подбор модели и параметров
seas_period_ = 12
# freq = 4
# freq = 7
# freq = 24

# model = pm.auto_arima(data_add, m = seas_period_)
model_p = pm.auto_arima(
    data_p_add,
    X=None,
    start_p=2,
    d=None,
    start_q=2,
    max_p=2,
    max_d=2,
    max_q=2,
    start_P=1,
    D=None,
    start_Q=1,
    max_P=2,
    max_D=2,
    max_Q=2,
    max_order=8,
    m=seas_period_,
    seasonal=True,
    stationary=False,
    information_criterion='aic',
    alpha=0.05,
    test='kpss',
    seasonal_test='ocsb',
    stepwise=True,
    n_jobs=1,
    start_params=None,
    trend=None,
    method='lbfgs',
    maxiter=50,
    offset_test_args=None,
    seasonal_test_args=None,
    suppress_warnings=True,
    error_action='trace',
    trace=False,
    random=False,
    random_state=None,
    n_fits=10,
    return_valid_fits=False,
    out_of_sample_size=0,
    scoring='mse',
    scoring_args=None,
    with_intercept="auto",
    sarimax_kwargs=None

)

#%%
# TODO summary()
model_p.summary()

#%%
# TODO fit + predict
seas_period_ = 12

model_p.fit(data_p_add)

pred_p = model_p.predict(n_periods=seas_period_)

pred_p

#%%
#TODO Обратное преобразование из логарифма
pred_p = 10**pred_p

#%%
# TODO График Исходного и Прогноза
plt.figure(figsize=(7, 3))
data_p.plot()
pred_p.plot()
plt.xlabel('data')
plt.ylabel('quantity')
plt.title('pass transport')
plt.show()

#%%
# TODO задавая period - мы формируем гипотезу о размере season, число наблюдений в сезоне

stl = STL(endog=data_p, period=6*2*2)

res = stl.fit()

res.plot()
plt.show()

#%%
#TODO Определение сезонности, одинаковый паттерн - это правильно выбранный период
"""
Атрибуты seasonal_decompose:
             * res.plot()
             * res.trend
             * res.seasonal
             * res.resid
             * res.observed
"""


#  Сезонная декомпозиция
decomposition = seasonal_decompose(data_p, model='multiplicative', period=12)
# fig = decomposition.plot()
fig1 = decomposition.seasonal.plot()
plt.show()

#%%
# TODO Атрибуты seasonal_decompose
decomposition.seasonal.plot()
plt.show()

#%%
# TODO ACF
# Автокорреляционная функция (ACF)
data_p_d = data_p.diff().dropna()
plot_acf(data_p_d, lags=24)
plt.title('ACF: проверка сезонности')
plt.show()

#%%
# TODO PACF
# data_p_d = data_p.diff().dropna()
plot_pacf(data_p, lags=24)
plt.title('PACF: partial corelation')
plt.show()


#%%
# TODO Спектральный анализ FFT
#  Перевод в реальные единицы  Т = 1 / f, Т - период/количество наблюдений, f - значение на оси Х
# Преобразование Фурье
fft_vals = np.fft.fft(data_p)
fft_freq = np.fft.fftfreq(len(data_p))

# Амплитуда
amplitude = np.abs(fft_vals)

# График
plt.figure(figsize=(10, 4))
plt.plot(fft_freq[:len(fft_freq)//2], amplitude[:len(amplitude)//2])
plt.xlabel('Частота')
plt.ylabel('Амплитуда')
plt.title('Спектральный анализ')
plt.show()

# Пик на частоте 1/24 → период = 24



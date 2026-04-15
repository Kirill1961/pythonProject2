from statsmodels.tsa.arima_model import ARIMA

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import acf, pacf

import pandas as pd
import numpy as np
from pandas import DataFrame

import matplotlib.pyplot as plt

from pathlib import Path

import statsmodels.api as sm
#%%
# TODO data random.normal
mu = 0
sigma = 1.5
np.random.seed(1)
data = pd.DataFrame(np.random.normal(mu, sigma, 30), columns=['V1'])
data.plot()
plt.show()

#%%
# TODO data default_rng
#  rng - Объект Генератора
mu = 0
sigma = 1.5
rng = np.random.default_rng(1)
data = pd.DataFrame(rng.normal(mu, sigma, 30), columns=['V1'])
data.plot()
plt.show()

#%%
# TODO Проверка сгенерированных данных по mu и std
print(abs(mu - np.mean(data)))
print(abs(sigma - np.std(data, ddof=1)))

#%%
# TODO Запись датсета в файл csv на диске через to_csv
#  index=False — убирает лишний столбец индекса
data.to_csv('D:/Eduson_data/1_wn.csv', index=False)

#%%
# TODO Запись датсета в файл csv на диске через numpy - savetxt
np.savetxt("D:/Eduson_data/2_wn.csv", data, delimiter=",")

#%%
# TODO pathlib чтение и convert в df
from io import StringIO
p = Path('D:/Eduson_data')/'1_wn.csv'
text = p.read_text()

# Убираем лишние символы через replace - в этом случае df через StringIO не получится
# text = text.replace('\n', ',').strip('V1,')

# Обратный convert в df через StringIO
df = pd.read_csv(StringIO(text))

df

#%%
# TODO plot_acf, plot_pacf, gca() - Get the current Axes.
#  method - способ оценивания автокорреляций / частичных автокорреляций.
plt.subplot(211)  # Ось 1-го графика
plot_acf(data['V1'], lags=20, ax=plt.gca())
plt.subplot(212)  # Ось 2-го графика
plot_pacf(data['V1'], method='ywm', lags=15, ax=plt.gca())
plt.show()

#%%
# TODO acf, pacf
#   method='ols' 👉 построит нереальный pacf с корреляцией > 1
acf(data['V1'])
pacf(data['V1'], nlags=15, method='ols')

#%%
# TODO Dow-Jones
data = pd.read_csv('D:\Eduson_data\dj.csv')

data.drop('t', axis=1,  inplace=True)

data.plot()
plt.show()

#%%
# TODO Dow-Jones acf, pacf
plt.subplot(211)  # Ось 1-го графика
plot_acf(data, lags=20, ax=plt.gca())
plt.subplot(212)  # Ось 2-го графика
plot_pacf(data, method='ywm', lags=20, ax=plt.gca())
plt.show()

#%%
# TODO Плавно-убывающая ACF для Dow-Jones требует diff
data_diff = data.diff()


#%%
data_diff.plot()
plt.show()

#%%
# TODO тк после diff появился NA то его удаляем
data_diff.dropna(inplace=True)

plt.subplot(211)  # Ось 1-го графика
plot_acf(data_diff, lags=20, ax=plt.gca())
plt.subplot(212)  # Ось 2-го графика
plot_pacf(data_diff, method='ywm', lags=20, ax=plt.gca())
plt.show()
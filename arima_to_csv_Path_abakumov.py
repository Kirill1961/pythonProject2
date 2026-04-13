from statsmodels.tsa.arima_model import ARIMA

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

import pandas as pd
import numpy as np
from pandas import DataFrame

import matplotlib.pyplot as plt

from pathlib import Path

np.random.seed(1)
data = pd.DataFrame(np.random.normal(0, 1, 30), columns=['V1'])
# data.plot()
# plt.show()

#%%
# TODO Генерация и Запись датсета в csv через to_csv
#  index=False — убирает лишний столбец индекса
data.to_csv('D:/Eduson_data/1_wn.csv', index=False)

#%%
# TODO Генерация и Запись датсета в csv через numpy - savetxt
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
# TODO acf, pacf
plt.subplot(211)
plot_acf(data['V1'], lags=20, ax=plt.gca())
plt.subplot(212)
plot_pacf(data['V1'], method='ywmle', lags=15, ax=plt.gca())
plt.show()


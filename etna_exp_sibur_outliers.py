"""
Внутри ETNA данные превращаются в wide-таблицу,
Но пользователю дают long-формат, потому что с ним проще работать.

"""


import pandas as pd
import numpy as np

from etna.datasets import TSDataset
from etna.metrics import MAE
from etna.metrics import MSE
from etna.metrics import SMAPE
from etna.models import MovingAverageModel
from etna.models import ProphetModel
from etna.pipeline import Pipeline

from etna.analysis import get_anomalies_density
from etna.analysis import get_anomalies_hist
from etna.analysis import get_anomalies_median
from etna.analysis import get_anomalies_prediction_interval
from etna.analysis import plot_anomalies

#%%
df = pd.read_csv("D:\Eduson_data\sibur_train_features.csv")

# df.dropna(inplace=True)

df['segment'] = df['A_CH4'] - df['A_C2H6']

ts = TSDataset(df, freq="0.5h")
ts.head(5)

#%%
ts.plot()



#%%
anomaly_dict = get_anomalies_median(ts, window_size=100)
plot_anomalies(ts, anomaly_dict)


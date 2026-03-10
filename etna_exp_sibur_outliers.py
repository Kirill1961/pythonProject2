"""
Ищем Аутлаеры
* Input - long table
* Внутри ETNA данные превращаются в wide-таблицу,
    * Но пользователю дают long-формат, потому что с ним проще работать.
* convert sibur - wide table в long table
"""



import matplotlib
# matplotlib.use("Agg")
# matplotlib.use("TkAgg")
# matplotlib.use("Qt5Agg")
# matplotlib.use("WebAgg")
import matplotlib.pyplot as plt
plt.switch_backend("TkAgg")


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
# TODO data
df_tg = pd.read_csv("D:\Eduson_data\sibur_train_targets.csv")
df_tr = pd.read_csv("D:\Eduson_data\sibur_train_features.csv")

#%%
# TODO convert sibur - wide table в long table
#  melt → merge → TSDataset

#  Сначала target приводим к long table
df_long = pd.melt(df_tg, id_vars=['timestamp'], var_name='segment', value_name= 'target')

#  Затем мерджим train с target_long
df = df_long.merge(df_tr, on='timestamp')

ts = TSDataset(df=df, freq="30min")
ts.head(5)

#%%
# TODO Графики
# 👉 ts.plot() рисует только целевые

# ts.to_pandas().plot()

# 1️⃣
ts.plot()
plt.show()

# 2️⃣
# ts.to_pandas().loc[:, ("A_C2H6", "timestamp")].plot()
# ts.to_pandas().loc[:, ("B_C2H6", "target")].plot()

# 3️⃣
# df_targets = ts.to_pandas().xs("target", level="feature", axis=1)
# df_targets.plot()
# plt.show()

# 4️⃣ все target ряды
# df_targets = ts.to_pandas().xs("target", level="feature", axis=1)
# df_targets.plot(title="Target series")
# plt.show()

# 5️⃣ все признаки
# df_features = ts.to_pandas().loc[:, ts.to_pandas().columns.get_level_values("feature") != "target"]
# df_features.plot(title="Features")
# plt.show()

#%%
# TODO Аутлаеры через Median method
anomaly_dict = get_anomalies_median(ts, window_size=1000)
plot_anomalies(ts, anomaly_dict)
plt.show()




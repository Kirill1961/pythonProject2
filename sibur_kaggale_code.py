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

matplotlib.use("TkAgg")  # или 'Qt5Agg', если есть Qt5
#%%
# TODO data train test target

df_tr = pd.read_csv("D:\Eduson_data\sibur_train_features.csv")

df_ts = pd.read_csv("D:\Eduson_data\sibur_test_features.csv")

df_tg = pd.read_csv("D:\Eduson_data\sibur_train_targets.csv")

df_sb = pd.read_csv("D:\Eduson_data\sibur_sample_submission.csv")

print("train :\n", df_tr.columns, "\n")
print("test  :\n", df_ts.columns, "\n")
print("target :\n", df_tg.columns, "\n")
print(
    f" train : {df_tr.shape} \n test : {df_ts.shape}"
    f" \n target : {df_tg.shape} \n submisiion : {df_sb.shape}",
    "\n",
)

print("infer_freq :\n", pd.infer_freq(df_tr["timestamp"]), "\n")

# TODO init train
df_tr["timestamp"] = pd.to_datetime(df_tr["timestamp"])

df_tr = df_tr.set_index("timestamp")

# TODO init target
df_tg["timestamp"] = pd.to_datetime(df_tg["timestamp"])

df_tg = df_tg.set_index("timestamp")

#%%
df_tr.isna().sum()
df_ts.isna().sum()




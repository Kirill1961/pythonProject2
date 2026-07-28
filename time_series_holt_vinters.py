from statsmodels.datasets import co2
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.datasets import co2
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error

#%%
# ============================
# Загружаем данные
# ============================

data = co2.load_pandas().data

#%%
# Удаляем пропуски
series = data["co2"].dropna()

# Приводим к месячной частоте
series = series.resample("MS").mean().interpolate()

# ============================
# Train / Test
# ============================


train = series[:-24]
test = series[-24:]

#%%
# ============================
# Модели
# ============================

models = {
    "add_add":
        ExponentialSmoothing(
            train,
            trend="add",
            seasonal="add",
            seasonal_periods=12
        ),

    "add_mul":
        ExponentialSmoothing(
            train,
            trend="add",
            seasonal="mul",
            seasonal_periods=12
        ),

    "mul_add":
        ExponentialSmoothing(
            train,
            trend="mul",
            seasonal="add",
            seasonal_periods=12
        ),

    "mul_mul":
        ExponentialSmoothing(
            train,
            trend="mul",
            seasonal="mul",
            seasonal_periods=12
        ),
}

# ============================
# Обучение
# ============================

fitted_models = {
    name: model.fit()
    for name, model in models.items()
}

# ============================
# Прогноз
# ============================

forecasts = {
    name: model.forecast(len(test))
    for name, model in fitted_models.items()
}

# ============================
# MAE
# ============================

print("MAE\n")

for name, forecast in forecasts.items():

    mae = mean_absolute_error(test, forecast)

    print(f"{name:10s}  {mae:.3f}")
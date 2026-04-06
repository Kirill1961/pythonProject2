import pmdarima as pm
import pandas as pd
import numpy as np

# Создаём пример данных
n_samples = 200
dates = pd.date_range('2020-01-01', periods=n_samples, freq='ME')
target = np.sin(2 * np.pi * np.arange(n_samples) / 12) + np.random.normal(0, 0.1, n_samples)
exog1 = np.cos(2 * np.pi * np.arange(n_samples) / 12) + np.random.normal(0, 0.05, n_samples)  # Экзогенная переменная 1
exog2 = np.random.randn(n_samples) * 0.2  # Экзогенная переменная 2

data = pd.DataFrame({
    'Target': target,
    'Exog1': exog1,
    'Exog2': exog2
}, index=dates)

# Разделяем данные
endog = data['Target']
exog = data[['Exog1', 'Exog2']]

# Автоподбор SARIMAX модели с экзогенными переменными
model = pm.auto_arima(
    y=endog,
    exogenous=exog,  # Передаём экзогенные переменные для SARIMAX
    seasonal=True,  # Включаем поиск сезонных параметров
    m=12,  # Период сезонности: 12 месяцев
    start_p=0, max_p=3,
    start_q=0, max_q=3,
    d=None,  # Автоматическое определение d (тест Дики-Фуллера)
    D=None,  # Автоматическое определение D (тест Канова-Хансена)
    trace=True,
    error_action='ignore',
    suppress_warnings=True,
    stepwise=True,
    information_criterion='aic'
)

print(model.summary())

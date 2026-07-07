"""
Прогноз состава компонентов через 14 часов, на входе в сатуратор .

Скрипт выполняет:
- загрузку исходных данных;
- предварительную обработку;
- построение прогноза;
- сохранение результатов в dataset/data.csv.

Автор: Кирилл
Дата: 2026-05-03
"""

# импорт библиотек
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from etna.datasets.tsdataset import TSDataset
from etna.models import NaiveModel
from etna.metrics import MAPE
import time
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    stream=sys.stdout
)
start = time.perf_counter()


def A_B_flow_restore(a_flow, b_flow, window, sigma):
    """
    Функция восстанавливающая значения A_flow и B_flow
    В окне считаем статистики
    Через среднеквадратичноое отклонение (std) определяем аутлаеры
    При отсутствии одного значения из пары A_flow и B_flow, строим регрессию для восстановления второго.
    Если неизвестны оба, заполняем на основе предыдущих значений
    Значения для окон 20 и 100 предварительно определяются через CV
    """
    a_flow = a_flow.copy()
    b_flow = b_flow.copy()

    result_a = [a_flow[0]]
    result_b = [b_flow[0]]

    for n in range(1, len(a_flow)):
        mean_a = np.array(result_a[-20:]).mean()
        diff_a = (pd.Series(result_a[-100:]) - pd.Series(result_a[-100:]).shift(1)).mean()
        mean_a += diff_a
        diff_mean_a = abs(pd.Series(result_a[-window:]) - pd.Series(result_a[-window:]).shift(1)).mean()
        diff_std_a = abs(pd.Series(result_a[-window:]) - pd.Series(result_a[-window:]).shift(1)).std()
        mean_b = np.array(result_b[-20:]).mean()
        diff_b = (pd.Series(result_b[-100:]) - pd.Series(result_b[-100:]).shift(1)).mean()
        mean_b += diff_b

        diff_mean_b = abs(pd.Series(result_b[-window:]) - pd.Series(result_b[-window:]).shift(1)).mean()
        diff_std_b = abs(pd.Series(result_b[-window:]) - pd.Series(result_b[-window:]).shift(1)).std()

        if n < window:
            pass
        else:
            if abs(a_flow[n] - result_a[n - 1]) > diff_mean_a + diff_std_a * sigma:
                a_flow[n] = None

            if abs(b_flow[n] - result_b[n - 1]) > diff_mean_b + diff_std_b * sigma:
                b_flow[n] = None

        if pd.isnull(a_flow[n]) and pd.isnull(b_flow[n]):
            result_a.append(mean_a)
            result_b.append(mean_b)

        elif pd.isnull(a_flow[n]):

            model = Ridge()
            model.fit(np.array(result_b[-3000:]).reshape(-1, 1), result_a[-3000:])
            result_a.append(model.predict(np.array(b_flow[n]).reshape(-1, 1))[0])

            result_b.append(b_flow[n])


        elif pd.isnull(b_flow[n]):

            model = Ridge()
            model.fit(np.array(result_a[-3000:]).reshape(-1, 1), result_b[-3000:])
            result_b.append(model.predict(np.array(a_flow[n]).reshape(-1, 1))[0])

            result_a.append(a_flow[n])


        else:
            result_a.append(a_flow[n])
            result_b.append(b_flow[n])

    return pd.Series(result_a), pd.Series(result_b)


def restore_data(series, window, window_mean, window_resid, sigma):
    """
    Функция, восстанавливает значения химических элементов
    В окне считаем статистики, затем основываясь на среднеквадратичном отклонении (std) определяем аутлаеры
    И на основе статистик заполняем пропуски
    """
    series = series.copy()

    result = [series[0]]

    for n in range(1, len(series)):

        mean_level = np.array(result[-window_mean:]).mean()

        diff_level = (pd.Series(result[-window_resid:]) - pd.Series(result[-window_resid:]).shift(1)).mean()

        mean_level += diff_level

        diff_mean = abs(pd.Series(result[-window:]) - pd.Series(result[-window:]).shift(1)).mean()
        diff_std = abs(pd.Series(result[-window:]) - pd.Series(result[-window:]).shift(1)).std()

        if n < window:
            pass
        else:

            if abs(series[n] - result[n - 1]) > diff_mean + diff_std * sigma:
                series[n] = None

        if pd.isnull(series[n]):
            result.append(mean_level)
        else:
            result.append(series[n])

    return pd.Series(result)


def restore_total_percent(data):
    """
    Функция восстановления процентов состава
    После восстановления пропусков некоторые наблюдения по сумме компонентов вышли за рамки 100%
    Пропорционально восстанавливаем их

    """
    data = data.copy()

    data['sum'] = data.iloc[:, 1:-1].T.sum()

    data['coef'] = 99.95 / data['sum']

    outlier_indexes = data[(data['sum'] > 99.99) | (data['sum'] < 99.92)].index

    for feat in range(1, 9):
        data.iloc[outlier_indexes, feat] = data.iloc[outlier_indexes, feat] * data.iloc[outlier_indexes, -1]

    return data.iloc[:, :-2]


# загрузка данных
data = pd.read_csv(r'C:\Users\Kirill\PycharmProjects\Practica\dataset\data.csv')

data = data.copy()

# разделяем на признаки и на таргеты данные
features = data.iloc[:, :10]
targets = data.iloc[:, 10:]

# чистим признаки по выше описаным функциям
features['A_flow'], features['B_flow'] = A_B_flow_restore(features['A_flow'], features['B_flow'], 500, 10)

features['A_4'] = restore_data(features['A_4'], 500, 20, 100, 9)
features['A_26'] = restore_data(features['A_26'], 400, 20, 100, 10)
features['A_38'] = restore_data(features['A_38'], 500, 20, 100, 14)
features['A_4101'] = restore_data(features['A_4101'], 500, 20, 100, 11)
features['A_4102'] = restore_data(features['A_4102'], 500, 20, 100, 11)
features['A_5121'] = restore_data(features['A_5121'], 400, 20, 100, 8)
features['A_5122'] = restore_data(features['A_5122'], 400, 20, 100, 9)
features['A_614'] = restore_data(features['A_614'], 500, 20, 100, 18)

# считаем средний B_rate в скользящем окне
features['B_flow_roll'] = features['B_flow'].rolling(190, min_periods=1).mean()

__doc__ = '''
Производим адаптивные сдвиги признаков относительно таргета, так как была найдена
взаимосвязь между напором в трубе и временем через которое смесь приходит в точку назначения.
Обычный сдвиг на константу давал результат хуже.
В зависимости от расхода в точке В, мы берем более или менее старые данные из прошлого.
 '''

# Для удобства дальнейшего использования переименовываем признаки и целевые
raw_train = features
raw_targets = targets

# инициализируем новые датафреймы
new_features = features.copy()
new_features.iloc[:, :] = 0

new_targets = targets.copy()
new_targets.iloc[:, :] = 0

# первые 250 значений игнорируем, так как не имеем о них качественных значений из прошлого
for i in range(features.shape[0]):
    if i < 250:
        new_features.iloc[i] = features.iloc[0]
        new_targets.iloc[i] = targets.iloc[0]
    else:

        # берем значение скользящего B_rate в момент времени n
        b_flow = features.iloc[i]['B_flow_roll']
        # сдвиг, константы были взяты по валидации на тренировочной выборке и среднему расхода (67) на выходе B_flow
        shift = 67 / b_flow * 190

        # исходя из подсчитаного сдвига берем n-shift значение признаков из прошлого
        new_features.iloc[i] = features.iloc[int(round(i - shift))]

        # таргеты берем в n время
        new_targets.iloc[i] = targets.iloc[i]

# обрезаем лишние признаки
new_features = new_features.iloc[:, :10]
new_features = new_features.reset_index(drop=True)
new_targets = new_targets.reset_index(drop=True)

# обрезаем мусорные 250 значений
new_features = new_features[250:].reset_index(drop=True)
new_targets = new_targets[250:].reset_index(drop=True)

# обрезаем часть тренировочной выборки с аномальными таргетами
new_features = new_features.drop(range(2250, 2450), axis=0).reset_index(drop=True)
new_targets = new_targets.drop(range(2250, 2450), axis=0).reset_index(drop=True)

# обрезаем часть тренировочной выборки, где таргеты были очень странно сглажены
new_features = new_features.drop(range(1290, 1440), axis=0).reset_index(drop=True)
new_targets = new_targets.drop(range(1290, 1440), axis=0).reset_index(drop=True)

# объединяем трейн и таргеты, чтобы удалить пропуски по таргетам,
# так же у нас удаляться тестовые значений, так как для них таргетов нет
data = pd.concat([new_features, new_targets], axis=1).dropna(
    subset=['B_26', 'B_38', 'B_4101', 'B_4102']).reset_index(drop=True)

# добавляем к тренировочным признакам временную метку, и отделяем их от таргетов
new_features = data.iloc[:, :11].reset_index(drop=True)
new_targets = data.iloc[:, 11:].reset_index(drop=True)

# сохраняем тренировочные значения и таргеты
train = new_features.copy()

# объединение данных
data = pd.concat([raw_train, raw_targets], axis=1)

# инициализация списка индексов с мусорными объектами
trash_indexes = list()

# в первых 190 строках очень шумные данные по многим хим элементам
trash_indexes += range(0, 190)

# Удаление пустых/странных значений хим элементов в перемешку с пропусками таргета
trash_indexes += range(1191, 1886)
trash_indexes += range(4523, 4689)

# Удаляем trash_indexes
data = data.drop(trash_indexes, axis=0).reset_index(drop=True)

raw_train = data.iloc[:, :10]
raw_targets = data.iloc[:, 10:]

# инициализация списка индексов с мусорными объектами (индексы взяты с учетом предыдущего удаления и сбросом индексов)
trash_indexes = list()

# пропуски по элементам
trash_indexes += raw_train[raw_train['A_38'].isnull()].index.to_list()

# пропуски в таргетах
trash_indexes += raw_targets[raw_targets.iloc[:, 1:5].isnull().T.sum() > 0].index.to_list()

# аутлаеры по A_rate
trash_indexes += range(1131, 1138)
trash_indexes += range(2822, 2828)
trash_indexes += [4032]
trash_indexes += range(4150, 4154)
trash_indexes += range(4214, 4217)
trash_indexes += range(4345, 4348)

# аутлаеры по B_rate
trash_indexes += range(2110, 2112)
trash_indexes += range(4492, 4495)

# аутлаеры по A_CH4
trash_indexes += [3850]
trash_indexes += range(843, 871)
trash_indexes += range(1250, 1254)

# аутлаеры по A_C2H6
trash_indexes += range(3850, 3855)
trash_indexes += range(2829, 2831)
trash_indexes += range(4348, 4350)
trash_indexes += range(1475, 1478)

# аутлаеры по A_C3H8
trash_indexes += range(3534, 3539)
trash_indexes += range(3578, 3586)

# аутлаеры по таргетам
trash_indexes += range(3638, 3641)
trash_indexes += range(1341, 1349)
trash_indexes += range(2835, 2837)

# Восстановление данных
raw_train['A_flow'], raw_train['B_flow'] = A_B_flow_restore(raw_train['A_flow'], raw_train['B_flow'], 1000, 12)

raw_train['A_4'] = restore_data(raw_train['A_4'], 500, 20, 100, 10)
raw_train['A_26'] = restore_data(raw_train['A_26'], 500, 20, 100, 14)
raw_train['A_38'] = restore_data(raw_train['A_38'], 500, 20, 100, 15)
raw_train['A_4101'] = restore_data(raw_train['A_4101'], 500, 20, 100, 11)
raw_train['A_4102'] = restore_data(raw_train['A_4102'], 500, 20, 100, 11)
raw_train['A_5121'] = restore_data(raw_train['A_5121'], 500, 20, 100, 7)
raw_train['A_5122'] = restore_data(raw_train['A_5122'], 400, 20, 100, 9)
raw_train['A_614'] = restore_data(raw_train['A_614'], 500, 20, 100, 18)

# восстановление процентов
raw_train = restore_total_percent(raw_train)

# данные для предсказания
final_train = raw_train.copy()
final_targets = raw_targets.copy()

# удаляем ранее отмеченные аутлаеры и пропуски
data = pd.concat([final_train, final_targets], axis=1)
data.drop(list(set(trash_indexes)), axis=0, inplace=True)
data = data.reset_index(drop=True)

# Отделяем трейн и таргеты
final_train = data.iloc[:, :10].copy()
final_targets = data.iloc[:, 10:].copy()

# Дополнительная чистка трейна
data = pd.concat([final_train, final_targets], axis=1)
data = data.drop([1353, 1354, 1355, 1437], axis=0)

# переносим метку времени в трейн и таргет
final_train = data.iloc[:, :12]
final_targets = data.iloc[:, 11:]

# по временной метке мерджим старые и новые данные
comb_data = pd.merge(final_train, train, on='timestamp', how='left')

# выделяем индексы для которых у нас есть новые значения
idx = comb_data[~comb_data['A_flow_y'].isnull()].index

# comb_train = final_train.iloc[:, :11].copy()
comb_train = final_train.drop('B_flow_roll', axis=1).copy()

# Переставим для удобства в comb_train  timestamp в начало таблицы
cols = comb_train.drop('timestamp', axis=1).columns.to_list()
cols_true = ['timestamp'] + cols
comb_train = comb_train[cols_true]

# заменяем часть трейна на новые данные
comb_train.iloc[idx] = comb_data[~comb_data['A_flow_y'].isnull()].iloc[:, 11:]

# сохраняем тренировочную выборку
final_train = comb_train.copy()

# Переносим столбец timestamp в таблицу, требование ETNA
final_train['timestamp'] = final_train['timestamp'].astype('datetime64[ns]')  # str to datetime64
final_targets['timestamp'] = final_targets['timestamp'].astype('datetime64[ns]')  # str to datetime64

# timestamp - переводим в индекс для дальнейшего связывания индексов
final_targets.set_index('timestamp', inplace=True)
final_train.set_index('timestamp', inplace=True)
# Синхронизация Индексов
final_train.index = final_targets.index

# Возвращаем timestamp из индекса в таблицу
final_targets.reset_index(inplace=True)
final_train.reset_index(inplace=True)

# Явно задаём частоту и интерполируем train
df_train = final_train.set_index("timestamp")
df_train = df_train.asfreq("30min")
df_train = df_train.interpolate(method="time")

# Явно задаём частоту и интерполируем targets
df_targets = final_targets.set_index("timestamp")
df_targets = df_targets.asfreq("30min")
df_targets = df_targets.interpolate(method="time")

# Сохраняем готовые train и targets
final_train = df_train.reset_index()
final_targets = df_targets.reset_index()

# Преобразуем данные в длинный формат ETNA
df_regressors2 = final_train.melt(id_vars="timestamp", var_name="segment", value_name="target")
df_to_forecast2 = final_targets.melt(id_vars="timestamp", var_name="segment", value_name="target")

# Создаем ETNA TSDataset с целевыми рядами и экзогенными признаками
ts = TSDataset(
    df=df_to_forecast2,
    freq="30min",
    df_exog=df_regressors2
)

# Горизонт прогноза по ТЗ: 14 часов (28 шагов по 30 минут)
horizon = 28

#  Делим на тренировочную и тестовую выборки
train_ts, test_ts = ts.train_test_split(test_size=horizon)

# Создаём объект NaiveModel
model = NaiveModel(lag=1)

# Обучение на тренировочной выборке
model.fit(train_ts)

# Формируем будущий период с учётом исторического контекста модели
future_ts = train_ts.make_future(future_steps=horizon,
                                  tail_steps=model.context_size)

# Получаем прогноз на заданный горизонт
forecast_ts = model.forecast(future_ts,
                             prediction_size=horizon)

# Оцениваем качество прогноза по метрике MAPE
mape = MAPE()
score_mape = mape(y_true=test_ts, y_pred=forecast_ts)

# Выбираем MAPE для целевых сегментов и рассчитываем суммарную ошибку
loss_mape = {}
loss_mape_total = [0]
for component, loss in score_mape.items():
    if component in ['B_26', 'B_38', 'B_4101', 'B_4102']:
        loss_mape[component] = round(loss, 4)
        loss_mape_total += loss
print('Cуммарная Ошибка (MAPE, %) по всем компонентам =', loss_mape_total[0])
print('Ошибка (MAPE, %) по компонентам: \n', loss_mape)

# Запись прогноза
forecast = targets.copy()
forecast_values = forecast_ts.to_pandas()[['B_26', 'B_38', 'B_4101', 'B_4102']]
forecast.update(forecast_values)
forecast = forecast.dropna()
forecast.to_csv(r'C:\Users\Kirill\PycharmProjects\Practica\dataset\forecast.csv', index=False)

elapsed = time.time() - start
logging.info(f"Forecast completed in {elapsed:.2f} seconds")

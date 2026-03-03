"""
Сглаживание,
Кастомные CV и заполнения,
Удаление аутлаеров и мусора
size=9792
"""

# TODO START
# импорт библиотек
import numpy as np
import pandas as pd
import time
from sklearn.linear_model import Ridge

import matplotlib

# matplotlib.use("Agg")
matplotlib.use("TkAgg")
# matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

import seaborn as sns

# plt.style.use('seaborn')
plt.style.use('seaborn-v0_8-bright')
# plt.style.available

from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose, STL

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

df2 = pd.DataFrame(np.arange(1, 46).reshape(-1, 3), columns=list("ABC"))
df3 = pd.DataFrame(np.arange(1, 301).reshape(-1, 3), columns=list("ABC"))

#%%
# TODO init train
# df_tr["timestamp"] = pd.to_datetime(df_tr["timestamp"])
#
# df_tr = df_tr.set_index("timestamp")
#
# # TODO init target
# df_tg["timestamp"] = pd.to_datetime(df_tg["timestamp"])
#
# df_tg = df_tg.set_index("timestamp")


#%%
# TODO 1 часть: функции
def mean_abs_per_err(y_true, y_pred):
    """
    Функция подсчета MAPE
    """
    return (abs((y_true - y_pred) / y_true)).mean() * 100


#%%
def exponential_smoothing(series, alpha):
    """
    Функция экспоненциального сглаживания, Рекурсивно.
    Получаем на вход сериес, и последовательно сглаживаем значения с "силой" alpha и сдвигом 1 шаг в перёд
    """
    # инициализация новой сериес result с 1-м индексом для сдвига на 1 шаг
    # заполняется со второго индекса
    # result это предыдущее сглаженное значение
    result = [series[0]]

    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n - 1])

    return pd.Series(result)


#%%
# TODO end
def A_B_rate_restore(a_rate, b_rate, window, sigma):
    """
    Функция, которая восстанавливает значения A_rate и B_rate
    В окне считаем статистики, затем основываясь на среднеквадратичном отклонении определяем аутлаеры
    Если после этого у нас не хватает только одного значения из пары A_rate и B_rate, то строим регрессию
    И восстанавливаем второе. Если неизвестны оба, заполняем на основе предыдущих значений
    Руками находим значения для окон 20 и 100 через CV
    Размер окон 20 и 100, при infer_freq = 30min, 20 - 10 часов и 100 - 50часов примерно 2 дня,
    * 10 часов локальной динамики
    * 2 суток устойчивого направления
    """
    a_rate = a_rate.copy()
    b_rate = b_rate.copy()

    # инициализируем новые массивы значений
    # result_a и result_b - список
    result_a = [a_rate[0]]
    result_b = [b_rate[0]]

    # в цикле проходим изначальный массив, заполняя на один шаг вперед основываясь 👉 на прошлых данных
    for n in range(1, len(a_rate)):

        # Для заполнения A_rate и B_rate:
        # статистики по A_rate, считаем среднее значение последних 20 объектов
        # находим среднее изменение по последним 100 объектам
        # создаём прогноз на следующий элемент, если у нас будет пропуск
        # 👉 result_a[-20:] это скользящее окно для заполняемого списка result_a
        mean_a_gup = np.array(result_a[-20:]).mean()
        # 👉 Средний прирост (наклон)
        resid_a_gup = (pd.Series(result_a[-100:]) - pd.Series(result_a[-100:]).shift(1)).mean()
        # 👉 текущий уровень + средняя скорость изменения
        mean_a_gup += resid_a_gup
        # среднее значение в заданном окне и среднее квадратичное изменение
        resid_mean_a = abs(pd.Series(result_a[-window:]) - pd.Series(result_a[-window:]).shift(1)).mean()
        resid_std_a = abs(pd.Series(result_a[-window:]) - pd.Series(result_a[-window:]).shift(1)).std()

        # Статистики по A_rate -/-
        mean_b_gup = np.array(result_b[-20:]).mean()
        resid_b_gup = (pd.Series(result_b[-100:]) - pd.Series(result_b[-100:]).shift(1)).mean()
        mean_b_gup += resid_b_gup

        resid_mean_b = abs(pd.Series(result_b[-window:]) - pd.Series(result_b[-window:]).shift(1)).mean()
        resid_std_b = abs(pd.Series(result_b[-window:]) - pd.Series(result_b[-window:]).shift(1)).std()

        # для первых значений аутлаеры не ищем, пока не наберется заданое окно значений
        if n < window:
            pass
        else:
            # находим аутлаеры, изменение которых сильно больше обычного и заменяем их на Null значение
            if abs(a_rate[n] - result_a[n - 1]) > resid_mean_a + resid_std_a * sigma:
                a_rate[n] = None

            if abs(b_rate[n] - result_b[n - 1]) > resid_mean_b + resid_std_b * sigma:
                b_rate[n] = None

        # если у нового объекта оба значений пропущенны, вставляем срадние значения за предыдущий период
        if pd.isnull(a_rate[n]) and pd.isnull(b_rate[n]):
            result_a.append(mean_a_gup)
            result_b.append(mean_b_gup)

        # если значений A_rate известно
        elif pd.isnull(a_rate[n]):

            # строим регрессию по последним 3000 объектов между A_rate и B_rate
            model = Ridge()
            model.fit(np.array(result_b[-3000:]).reshape(-1, 1), result_a[-3000:])
            result_a.append(model.predict(np.array(b_rate[n]).reshape(-1, 1))[0])
            # добавляем известное значение B_rate
            result_b.append(b_rate[n])

        # если значений B_rate известно
        elif pd.isnull(b_rate[n]):

            # строим регрессию по последним 3000 объектов между A_rate и B_rate
            model = Ridge()
            model.fit(np.array(result_a[-3000:]).reshape(-1, 1), result_b[-3000:])
            result_b.append(model.predict(np.array(a_rate[n]).reshape(-1, 1))[0])
            # добавляем известное значение A_rate
            result_a.append(a_rate[n])

        # если оба известны, просто добавляем их в новые последовательности
        else:
            result_a.append(a_rate[n])
            result_b.append(b_rate[n])

    return pd.Series(result_a), pd.Series(result_b)


A_B_rate_restore(df3.A, df3.B, 20, 5)


#%%
def chemical_data_restore(series, window, window_mean, window_resid, sigma):
    """
    Функция, которая восстанавливает значения химических элементов
    В окне считаем статистики, затем основываясь на среднеквадратичном отклонении определяем аутлаеры
    И на основе статистик заполняем пропуски
    """
    series = series.copy()

    # инициализируем новый массив значений
    result = [series[0]]

    # в цикле проходим изначальный массив, заполняя на один шаг вперед основываясь на прошлых данных
    for n in range(1, len(series)):

        # статистики по химическому элементу
        # находим среднее значение по последним window_mean объектам
        mean_gup = np.array(result[-window_mean:]).mean()
        # находим среднее изменение по последним window_resid объектам
        resid_gup = (pd.Series(result[-window_resid:]) - pd.Series(result[-window_resid:]).shift(1)).mean()
        # получаем прогноз на следующий элемент, если у нас будет пропуск
        mean_gup += resid_gup

        # среднее значение в заданном окне и среднее изменение
        resid_mean = abs(pd.Series(result[-window:]) - pd.Series(result[-window:]).shift(1)).mean()
        resid_std = abs(pd.Series(result[-window:]) - pd.Series(result[-window:]).shift(1)).std()

        # для первых значений аутлаеры не ищем, пока не наберется заданое окно значений
        if n < window:
            pass
        else:
            # находим аутлаеры, изменение которых сильно больше обычного и заменяем их на Null значение
            if abs(series[n] - result[n - 1]) > resid_mean + resid_std * sigma:
                series[n] = None

        # если пропуск, вставляем расчитаное до этого значение
        if pd.isnull(series[n]):
            result.append(mean_gup)
        else:
            result.append(series[n])

    return pd.Series(result)


#%%
def restore_percent(data):
    """
    Функция восстановления процентов состава
    После восстановления пропусков некоторые суммы улетели за логичные значения
    Больше 100, или меньше 99,2
    Пропорционально восстанавливаем их
    """
    data = data.copy()
    # находим сумму элементов
    data['sum'] = data.iloc[:, 1:-1].T.sum()
    # находим кэффициент на который сумма отличается от эталоного значения
    data['coef'] = 99.95 / data['sum']
    # определяем индексы объектов со сломанной суммой
    outlier_indexes = data[(data['sum'] > 99.99) | (data['sum'] < 99.92)].index

    # в цикле пропорционально восстанавливаем значения элементов
    for feat in range(1, 9):
        data.iloc[outlier_indexes, feat] = data.iloc[outlier_indexes, feat] * data.iloc[outlier_indexes, -1]

    return data.iloc[:, :-2]


#%%
# TODO 2 часть: подготовка данных с новыми адаптивными сдвигами

# загрузка данных
raw_train = df_tr
raw_test = df_ts
sample = df_sb
raw_targets = df_tg

# удаление временных промежутков, в таргетах он нам нужен для мержда с основным пайплайном
raw_train.drop('timestamp', axis=1, inplace=True)
raw_test.drop('timestamp', axis=1, inplace=True)
# raw_targets.drop('timestamp', axis=1, inplace=True)

# склеиваем все данные вместе
data = pd.concat([raw_train, raw_targets], axis=1)
data = pd.concat([data, raw_test], axis=0).reset_index(drop=True)

# обрезаем начало трейна, так как все что раньше слишком шумно и пробрасываться не будет
data = data[2200:].reset_index(drop=True)

# разделяем на признаки и на таргеты данные
features = data.iloc[:, :10]
targets = data.iloc[:, 10:]

#%%
# TODO features
start = time.time()
# чистим признаки по выше описаным функциям, некоторые параметры подбирались исходя из структуры изменения признака

features['A_rate'], features['B_rate'] = A_B_rate_restore(features['A_rate'], features['B_rate'], 500, 10)

features['A_CH4'] = chemical_data_restore(features['A_CH4'], 500, 20, 100, 9)
# features['A_C2H6'] = chemical_data_restore(features['A_C2H6'], 400, 20, 100, 10)
# features['A_C3H8'] = chemical_data_restore(features['A_C3H8'], 500, 20, 100, 14)
# features['A_iC4H10'] = chemical_data_restore(features['A_iC4H10'], 500, 20, 100, 11)
# features['A_nC4H10'] = chemical_data_restore(features['A_nC4H10'], 500, 20, 100, 11)
# features['A_iC5H12'] = chemical_data_restore(features['A_iC5H12'], 400, 20, 100, 8)
# features['A_nC5H12'] = chemical_data_restore(features['A_nC5H12'], 400, 20, 100, 9)
# features['A_C6H14'] = chemical_data_restore(features['A_C6H14'], 500, 20, 100, 18)

end = time.time()
print(end - start)

#%%
# считаем средний B_rate в скользящем окне
features['B_rate_roll'] = features['B_rate'].rolling(190, min_periods=1).mean()

"""
Дальше происходит процесс адаптивных сдвигов признаков относительно таргета, так как была найдена
взаимосвязь между напором в трубе и временем через которое газ приходит в точку назначения. 
Обычный сдвиг на константу давал результат хуже. Поэтому в зависимости от напора мы берем более или менее старые данные из прошлого.
"""
# инициализируем новые датафреймы
new_features = features.copy()
new_features.iloc[:, :] = 0

new_targets = targets.copy()
new_targets.iloc[:, :] = 0

# первые 250 значений мусорим, так как не имеем о них качественных значений из прошлого
for i in range(features.shape[0]):
    if i < 250:
        new_features.iloc[i] = features.iloc[0]
        new_targets.iloc[i] = targets.iloc[0]
    else:
        # берем значение скользящего B_rate в момент времени n
        b_rate = features.iloc[i]['B_rate_roll']
        # расчитываем для него сдвиг, константы были взяты по валидации на тренировочной выборке
        # был посчитан средний рейт и оптимальный сдвиг на небольшом куске данных и потом в цикле значения уточнялись
        shift = 67 / b_rate * 198
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

# сохраняем тестовые значения, 3984 это размер тестовой выборки, отрезаем с конца ее
test = new_features[-3984:].reset_index(drop=True)

# объединяем трен и таргеты, чтобы удалить пропуски по таргетам, так же у нас удаляться тестовые значений, так как для них таргетов нет
data = pd.concat([new_features, new_targets], axis=1).dropna(
    subset=['B_C2H6', 'B_C3H8', 'B_iC4H10', 'B_nC4H10']).reset_index(drop=True)

# добавляем к тренировочным признакам временную метку, и отделяем их от таргетов
new_features = data.iloc[:, :11].reset_index(drop=True)
new_targets = data.iloc[:, 11:].reset_index(drop=True)

# сохраняем тренировочные значения и таргеты
train = new_features.copy()
train_targets = new_targets.copy()

#%%
# загрузка данных
raw_train = pd.read_csv("D:\Eduson_data\sibur_train_features.csv")
raw_test = pd.read_csv("D:\Eduson_data\sibur_test_features.csv")
raw_targets = pd.read_csv("D:\Eduson_data\sibur_train_targets.csv")

# удаление временных промежутков, в таргетах он нам нужен для мержда с новыми данными
raw_train.drop('timestamp', axis=1, inplace=True)
raw_test.drop('timestamp', axis=1, inplace=True)
# raw_targets.drop('timestamp', axis=1, inplace=True)

# в этом случае использовался константный сдвиг
shift = 192
full_size = 9792
size_test = 3984 + shift
size_train = full_size - size_test

# объединение данных
data = pd.concat([raw_train, raw_targets], axis=1)
data = pd.concat([data, raw_test], axis=0)

# сдвиг таргетов на фиксированое число
data = pd.concat([data.iloc[:, :9].reset_index(drop=True),
                  data.iloc[1:, 9].reset_index(drop=True),
                  data.iloc[shift:, 10:].reset_index(drop=True)], axis=1)

# получение тренировочной, тестовой выборки и таргетов
raw_train = data.iloc[:size_train, :10].reset_index(drop=True)
raw_targets = data.iloc[:size_train, 10:].reset_index(drop=True)
raw_test = data.iloc[size_train:-shift, :10].reset_index(drop=True)

#%%
# предварительная чистка трейна

data = pd.concat([raw_train, raw_targets], axis=1)

# инициализация списка индексов с мусорными объектами
trash_indexes = list()
# в первых 190 строках очень шумные данные по многим хим элементам
trash_indexes += range(0, 190)
# # огромный сэмпл пустых/странных значений хим элементов в перемешку с пропусками таргета
trash_indexes += range(1191, 1886)
# # сэмпл трейна, где таргеты ведут себя очень странно
trash_indexes += range(4523, 4689)

data = data.drop(trash_indexes, axis=0).reset_index(drop=True)

raw_train = data.iloc[:, :10]
raw_targets = data.iloc[:, 10:]

#%%
# чтобы получить максимально чистые тренировочные данные, до процесса очистки и заполнения пропусков
# 👉 руками были найденны аутлаеры/пропуски в трейне, которые будут удаленны после восстановления

# инициализация списка индексов с мусорными объектами (индексы взяты с учетом предыдущего удаления и сбросом индексов)
trash_indexes = list()
# пропуски по элементам
trash_indexes += raw_train[raw_train['A_C3H8'].isnull()].index.to_list()
# # пропуски в таргетах
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

#%%
# восстановливаем только тренировочные данные, так как тестовые целиком будут взяты из данных с новыми сдвигами

raw_train['A_rate'], raw_train['B_rate'] = A_B_rate_restore(raw_train['A_rate'], raw_train['B_rate'], 1000, 12)

raw_train['A_CH4'] = chemical_data_restore(raw_train['A_CH4'], 500, 20, 100, 10)
raw_train['A_C2H6'] = chemical_data_restore(raw_train['A_C2H6'], 500, 20, 100, 14)
raw_train['A_C3H8'] = chemical_data_restore(raw_train['A_C3H8'], 500, 20, 100, 15)
raw_train['A_iC4H10'] = chemical_data_restore(raw_train['A_iC4H10'], 500, 20, 100, 11)
raw_train['A_nC4H10'] = chemical_data_restore(raw_train['A_nC4H10'], 500, 20, 100, 11)
raw_train['A_iC5H12'] = chemical_data_restore(raw_train['A_iC5H12'], 500, 20, 100, 7)
raw_train['A_nC5H12'] = chemical_data_restore(raw_train['A_nC5H12'], 400, 20, 100, 9)
raw_train['A_C6H14'] = chemical_data_restore(raw_train['A_C6H14'], 500, 20, 100, 18)

# восстановление процентов
raw_train = restore_percent(raw_train)


#%%
# TODO acf, STL
# TODO limit_direction="both" - Заполнение NA в начале и в конце df

def stl_init(sample, period, flag=False):
    """
    Построение через res.plot() и в ручную
    """

    if flag == False:

        feature = sample.astype(float).interpolate(limit_direction='both')

        stl = STL(feature, period=period, robust=True)  # period = предполагаемый сезонный цикл

        res = stl.fit()

        res.plot()
        plt.show()

    else:
        feature = sample.astype(float)

        stl = STL(feature, period=period)  # period = предполагаемый сезонный цикл

        res = stl.fit()

        res.plot()
        plt.show()

    # 1️⃣ В ручную
    # feature = sample
    #
    # stl = STL(feature, period=period, robust=True)
    # res = stl.fit()
    #
    # fig, ax = plt.subplots(4, 1, figsize=(12, 8), sharex=True)
    #
    # ax[0].plot(feature)
    # ax[0].set_title("Original")
    #
    # ax[1].plot(res.trend)
    # ax[1].set_title("Trend")
    #
    # ax[2].plot(res.seasonal)
    # ax[2].set_title("Seasonal")
    #
    # ax[3].plot(res.resid)
    # ax[3].set_title("Residual")
    #
    # plt.tight_layout()
    # plt.show()

# stl_init(df_tr['A_rate'], 48, flag=False)
# stl_init(features['A_rate'], 48, flag=True)

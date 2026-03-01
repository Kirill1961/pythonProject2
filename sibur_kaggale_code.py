# TODO START
# импорт библиотек
import numpy as np
import pandas as pd
import time
from sklearn.linear_model import Ridge

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# plt.style.use('seaborn')
plt.style.use('seaborn-v0_8-bright')
# plt.style.available


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

#%%
# TODO init train
df_tr["timestamp"] = pd.to_datetime(df_tr["timestamp"])

df_tr = df_tr.set_index("timestamp")

# TODO init target
df_tg["timestamp"] = pd.to_datetime(df_tg["timestamp"])

df_tg = df_tg.set_index("timestamp")


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
    функция экспоненциального сглаживания
    Получаем на вход сериес, и последовательно сглаживаем значения с "силой" alpha
    """
    # инициализация новой сериес ?? с одним значением под индекс
    result = [series[0]]

    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n - 1])

    return pd.Series(result)


#%%
def A_B_rate_restore(a_rate, b_rate, window, sigma):
    """
    Функция, которая восстанавливает значения A_rate и B_rate
    В окне считаем статистики, затем основываясь на среднеквадратичном отклонении определяем аутлаеры
    Если после этого у нас не хватает только одного значения из пары A_rate и B_rate, то строим регрессию
    И восстанавливаем второе. Если неизвестны оба, заполняем на основе предыдущих значений
    """
    a_rate = a_rate.copy()
    b_rate = b_rate.copy()

    # инициализируем новые массивы значений
    result_a = [a_rate[0]]
    result_b = [b_rate[0]]

    # в цикле проходим изначальный массив, заполняя на один шаг вперед основываясь на прошлых данных
    for n in range(1, len(a_rate)):

        # статистики по A_rate, считаем среднее значение последних 20 объектов
        # находим среднее изменение по последним 100 объектам
        # получаем прогноз на следующий элемент, если у нас будет пропуск
        mean_a_gup = np.array(result_a[-20:]).mean()
        resid_a_gup = (pd.Series(result_a[-100:]) - pd.Series(result_a[-100:]).shift(1)).mean()
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
start = time.time()
# чистим признаки по выше описаным функциям, некоторые параметры подбирались исходя из структуры изменения признака

features['A_rate'], features['B_rate'] = A_B_rate_restore(features['A_rate'], features['B_rate'], 500, 10)

features['A_CH4'] = chemical_data_restore(features['A_CH4'], 500, 20, 100, 9)
features['A_C2H6'] = chemical_data_restore(features['A_C2H6'], 400, 20, 100, 10)
features['A_C3H8'] = chemical_data_restore(features['A_C3H8'], 500, 20, 100, 14)
features['A_iC4H10'] = chemical_data_restore(features['A_iC4H10'], 500, 20, 100, 11)
features['A_nC4H10'] = chemical_data_restore(features['A_nC4H10'], 500, 20, 100, 11)
features['A_iC5H12'] = chemical_data_restore(features['A_iC5H12'], 400, 20, 100, 8)
features['A_nC5H12'] = chemical_data_restore(features['A_nC5H12'], 400, 20, 100, 9)
features['A_C6H14'] = chemical_data_restore(features['A_C6H14'], 500, 20, 100, 18)

end = time.time()
print(end - start)
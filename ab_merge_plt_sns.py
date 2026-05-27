"""
A/B test
В рамках этого проекта вам предстоит разобраться в результатах A/B-тестирования, проведенного интернет-магазином.
Компания разработала новую веб-страницу, чтобы попытаться увеличить количество пользователей, совершающих «конверсию»,
то есть количество пользователей, решивших оплатить продукт компании.
Ваша задача — с помощью этого блокнота помочь компании понять, следует ли ей внедрить новую страницу,
оставить старую или, возможно, продлить эксперимент, чтобы принять окончательное решение.
 * id - уникальный идентификатор пользователя
 * time - время события/визита пользователя
 * con_treat - (или чаще group)	в какую группу эксперимента попал пользователь: control или treatment
    * control - пользователи, которые видят старую страницу
    * treatment - пользователи, которые видят новую страницу
    * num - моя колонка, для ttest
 * page - какую версию страницы увидел пользователь
 * converted - совершил ли пользователь целевое действие
 * country - страна пользователя
"""
#%%
import numpy as np
import pandas as pd
from scipy.stats import norm, ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
import statsmodels.api as sm


#%%
# TODO data
ab_test = pd.read_csv('D:/Eduson_data/ab_test.csv')
countries = pd.read_csv('D:/Eduson_data/countries_ab.csv')
print(ab_test.shape, '\n', countries.shape)


#%%
# TODO merge 2-х таблиц

# np.random.seed(1)  # Средние  num по control/treatment  почти не различаются
np.random.seed(10)  # Средние num по control/treatment хорошо различаются
data = pd.merge(ab_test, countries, on='id', how='left')
data['num'] = np.random.randint(1, 100, size=len(data))
data.shape


#%%
# TODO Число дубликатов

duplicate = data.duplicated(subset=['id']).sum()
duplicate


#%%
# TODO seaborn Подписи столбцов Гистограммы, числа из контейнера

ax = sns.histplot(data, x='country')
for i in ax.containers:
    ax.bar_label(i)
    ax.set(
        xlabel="country",
        ylabel="число пользователей",
        title="id пользователей из стран"
        # xlim=(xmin, xmax),
        # xticks=[...],
        # xticklabels=[...],
    )
plt.show()


#%%
# TODO Новый seaborn.objects

(
    so.Plot(data, "country")
    .add(so.Bar(), so.Hist())
    .show()
)


#%%
# TODO matplotlib Подписи столбцов Гистограммы

# create a histogram of user IDs by country
plt.hist(data['country'])
plt.title('User IDs by Country')
plt.xlabel('Country')
plt.ylabel('Count')
for i, country in enumerate(data['country'].unique()):
    count = data[data['country'] == country]['id'].count()
    plt.text(i, count, str(count), ha='center', va='bottom')
plt.show()


#%%
# TODO Рассчитайте коэффициенты конверсии для каждой группы.
#  🚀 mean - по сути для Бернулли (1/0) это оценка вероятности успеха -> P_успех / P_число испытаний

control_rate = data.loc[data['con_treat'] == 'control', 'converted'].mean()
treatment_rate = data.loc[data['con_treat'] == 'treatment', 'converted'].mean()

#%%
# TODO Cat - Bin >>> группировка >>> Bin 0/1 - распределение Бернулли

group_trials = data.groupby(['con_treat'])['converted'].count()
print(group_trials)

group_success = data.groupby(['con_treat'])['converted'].sum()
print(group_success)

trials = pd.DataFrame(group_trials).values.ravel().tolist()
success = pd.DataFrame(group_success).values.ravel().tolist()
print(trials, success)

#%%
# TODO Z - test, пропорции, Cat-Bin, признаки con_treat и converted

stat, p_val = sm.stats.proportions_ztest(success, trials)
print(stat, p_val)

#%%
# TODO t - test, средние, Cat-Num, признаки con_treat и num

group_con_treat = data.groupby(['con_treat'])['num'].mean()
print(group_con_treat)

# array-like наборы для ttest_ind
treatment = data.loc[data['con_treat'] == 'treatment']['num']
control = data.loc[data['con_treat'] == 'control']['num']

# t-тест и p-value
tstat, pvalue = ttest_ind(treatment, control)
print(tstat, pvalue)

#%% TODO conversion rates через seaborn
ax = sns.barplot(data, x=data['con_treat'], y=data['converted'])

for i in ax.containers:
    ax.bar_label(i)
    ax.set(
        xlabel="группы пользователей",
        ylabel="среднее конверсии",
        title="Коэффициент конверсии юзеров",
        ylim=(0, 0.2)  # ограничение значений шкалы Y
        # xticks=[...],
        # xticklabels=[...],
    )
plt.show()


#%% TODO conversion rates через matplotlib

# create a bar chart of the conversion rates
plt.bar(['Control', 'Treatment'], [control_rate, treatment_rate])
plt.title('Conversion Rates by Group')
plt.ylabel('Conversion Rate')
plt.ylim(0, 0.15)
plt.text(0, control_rate + 0.01, f'{control_rate:.4f}')
plt.text(1, treatment_rate + 0.01, f'{treatment_rate:.4f}')
plt.show()



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
 * page - какую версию страницы увидел пользователь
 * converted - совершил ли пользователь целевое действие
 * country - страна пользователя
"""
#%%
import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

#%%
# TODO data
ab_test = pd.read_csv('D:/Eduson_data/ab_test.csv')
countries = pd.read_csv('D:/Eduson_data/countries_ab.csv')
print(ab_test.shape, '\n', countries.shape)


#%%
# TODO merge 2-х таблиц

data = pd.merge(ab_test, countries, on='id', how='left')
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

control_rate =  data.loc[data['con_treat'] == 'control', 'converted'].mean()
treatment_rate =  data.loc[data['con_treat'] == 'treatment', 'converted'].mean()

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



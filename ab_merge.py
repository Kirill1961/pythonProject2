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

#%%
# TODO data
ab_test = pd.read_csv('D:/Eduson_data/ab_test.csv')
countries = pd.read_csv('D:/Eduson_data/countries_ab.csv')
print(ab_test.shape, '\n', countries.shape)


#%%
data = pd.merge(ab_test, countries, on='id', how='left')
data.shape


# TODO Число дубликатов
#%%
duplicate = data.duplicated(subset=['id']).sum()
duplicate


#%%
# data[data['country'] == 'US']['id'].unique().shape
# data[data['country'] == 'US']['id']
cnt = data.groupby('country')['id'].count()
print(cnt)

# plt.hist(cnt.values)
# plt.show()

sns.histplot(data['country'])
plt.show()



#%%
plt.hist(data['country'])
# for n, name in enumerate(data['country'].unique()):
#    print( data[data['country'] == name]['id'].count())
#    # plt.hist(data[data['country'] == name]['id'].count(), bins=30)
plt.show()



"""
A/B test
В рамках этого проекта вам предстоит разобраться в результатах A/B-тестирования, проведенного интернет-магазином.
Компания разработала новую веб-страницу, чтобы попытаться увеличить количество пользователей, совершающих «конверсию»,
то есть количество пользователей, решивших оплатить продукт компании.
Ваша задача — с помощью этого блокнота помочь компании понять, следует ли ей внедрить новую страницу,
оставить старую или, возможно, продлить эксперимент, чтобы принять окончательное решение.
"""
#%%
import numpy as np
import pandas as pd
from scipy.stats import norm


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

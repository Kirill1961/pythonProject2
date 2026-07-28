'''
Подключение к БД из кода python
'''

from sqlalchemy import create_engine
import pandas as pd
import numpy as np

#  Локально подключились к БД
engine = create_engine(
    "postgresql://postgres:1961km1@localhost:5432/db333"
)


t = pd.date_range('2010-01-01', periods=12, freq='W')
dt = pd.DataFrame(np.random.randint(10, 100, size=len(t)), index=t)
dt.columns = ['value']

np.random.seed(1)
print('Исходный dt c freq = WEEK : \n', dt, '\n')


# Добавим NA в индекс и в value
dt = dt.reset_index()
dt.loc[[2, 7], 'index'] = pd.NaT
dt.loc[[3, 5], 'value'] = np.nan
dt.set_index('index', drop=True, inplace=True)

df = dt.reset_index()

print(df)

# Передаём таблицу в БД SQL
__doc__='''
index=False - Индекс Удаляется
index=True - Индекс Переносится в Столбец
'''
df.to_sql(
    "date_for_resample",
    con=engine,
    if_exists="replace",
    index=False
)
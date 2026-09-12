import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
from datetime import datetime, timedelta
import sqlite3

#%%
# TODO Генерация таблиц с данными sales и digital

np.random.seed(1)
start_date = datetime(2025, 1, 1)

dates = [
    start_date + timedelta(days=np.random.randint(0, 365))
    for _ in range(4000)
]

dt = pd.date_range('2025-01-01', periods=365, freq="d")

#%%
products = ['Phone', 'Laptop', 'Tablet', 'Monitor']

client_id = np.random.randint(1, 100, 4000)

quantity = np.random.choice(
    [1, 2, 3, 4, 5],
    4000,
    p=[0.3, 0.25, 0.2, 0.15, 0.1]
)

sales = pd.DataFrame({
    'client_id': client_id,
    'product': np.random.choice(products, 4000),
    'date': dates,
    'quantity': quantity
})

probs = [0.6, 0.4]

digital = pd.DataFrame({
    'client_id': np.random.randint(1, 100, 4000),
    'product': np.random.choice(products, 4000),
    'date': dates,
    'event': np.random.choice(
        ['Click', 'Impression'],
        4000,
        p=probs
    ),
    'cnt': np.random.choice(
        [1, 3, 5, 4],
        4000,
        p=[0.5, 0.2, 0.2, 0.1]
    )
})

#%%
# TODO Подключение к базе в памяти
conn = sqlite3.connect(":memory:")

digital.to_sql("digital", conn, index=False, if_exists="replace")
sales.to_sql("sales", conn, index=False, if_exists="replace")

#%%
# TODO Запрос через read_sql
query = """
select 
product,
cnt, 
max_val
from      
    (select 
    product,
    count(date) as cnt,
    --row_number() over(order by count(date) desc )
    max(count(date)) over () as max_val
    from sales
    where date >= '2025-02-01' and date < '2025-03-01' 
    group by  product)
where cnt = max_val
"""

result = pd.read_sql_query(query, conn)

result

#%%
#TODO Фильтр по дате без WHERE

query = """
select 
s.product,
sum(quantity) as cnt,
s.client_id
from sales s
join digital d on s.date = d.date 
                and s.product = d.product
                and s.client_id = d.client_id
                and d.date >= '2025-02-01' 
                and d.date < '2025-03-01'
group by s.product, s.client_id
order by 2 desc 
"""

result = pd.read_sql_query(query, conn)

result[:10]

import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
from datetime import datetime, timedelta
import sqlite3

#%%
# TODO Генерация таблиц с данными sales и digital
n_rows = 4000

probs = [0.3, 0.7]

np.random.seed(10)
start_date = datetime(2025, 1, 1)

dates = [
    start_date + timedelta(days=np.random.randint(0, 365))
    for _ in range(n_rows)
]

dt = pd.date_range('2025-01-01', periods=365, freq="d")

products = ['Phone', 'Laptop', 'Tablet', 'Monitor']

client_id = np.random.randint(1, 100, n_rows)

quantity = np.random.choice(
    [1, 2, 3, 4, 5],
    n_rows,
    p=[0.3, 0.25, 0.2, 0.15, 0.1]
)

sales = pd.DataFrame({
    'client_id': client_id,
    'product': np.random.choice(products, n_rows),
    'date': dates,
    'quantity': quantity
})


digital = pd.DataFrame({
    'client_id': np.random.randint(1, 100, n_rows),
    'product': np.random.choice(products, n_rows),
    'date': dates,
    'event': np.random.choice(
        ['Click', 'Impression'],
        n_rows,
        p=probs
    ),
    'cnt': np.random.choice(
        [1, 3, 5, 4],
        n_rows,
        p=[0.1, 0.2, 0.2, 0.5]
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
# TODO Фильтр по дате без WHERE

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

#%%
# TODO
#  IN - используем когда case по нескольким категориям,
#  Умножение на 1.0 это для вещественного деления для преобразования в float
#  CAST - такое же преобразование в float
#  :: - не работает потом что это не PSQL а DuckDB
#  100.0 - это умножение приводит к значения к % Процентам, неявно заставляем вычисление стать вещественным
query = """
select  
--SUM(CASE WHEN event = 'Click' THEN cnt END)::float
CAST(sum(case when event in ('Impression') then cnt end) as float) as all_Impression,
CAST(sum(case when event = 'Click' then cnt end) as float )as all_Click,
1.0 * sum(case when event = 'Click' then cnt end)/sum(case when event in ('Impression') then cnt end) as CTR, 
100.0 * sum(case when event = 'Click' then cnt end)/sum(case when event in ('Impression') then cnt end) as CTR, 
CAST(sum(case when event = 'Click' then cnt end) as float )/CAST(sum(case when event in ('Impression') then cnt end) as float) as CTR 
from digital
"""

result = pd.read_sql_query(query, conn)

result[:10]

#%%
# TODO ЗАДАЧА : Посчитать количество просмотров , кликов, уникальных просмотров, уникальных кликов, CTR, продажи, CR
#  Суммарные продажи считаем через quantity, поэтому джойним с sales
query = """
select 
d.date,
d.product,
sum(case when d.event == 'Impression' then d.cnt end) as Impression,
sum(case when d.event == 'Click' then d.cnt end) as Click,
--count(distinct case when d.event = 'Impression' then d.client_id end) as uniq_impression,
--count(distinct case when d.event = 'Click' then d.client_id end) as uniq_Click,
count(distinct d.client_id) filter ( where d.event = 'Impression' ) as uniq_Impression,
count(distinct d.client_id) filter ( where d.event = 'Click' ) as uniq_Click1,
--cast (count(distinct d.client_id) as float)/sum(case when d.event == 'Impression' then cnt end) as CR,
100.0 * count(distinct d.client_id)/sum(case when d.event == 'Impression' then d.cnt end) as CR,
sum(coalesce (s.quantity, 0)) as sales
from digital d
left join sales s 
on d.client_id = s.client_id and d.product = s.product and d.date = s.date
group by 
d.product, 
d.date
;
"""

result = pd.read_sql_query(query, conn)

result[:10]

#%%
query = """
    select *
    from sales s
    left join digital d on d.client_id = s.client_id
    ;
"""


result = pd.read_sql_query(query, conn)

result[:10]
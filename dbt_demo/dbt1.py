import sqlite3
# import duckdb
import pandas as pd
import numpy as np

# path = r"C:/Users/Kirill/PycharmProjects/pythonProject2/tut.db"

# conn = sqlite3.connect("tut.db")
# conn = sqlite3.connect("delta.db")
#
# cur = conn.cursor()
#
# res = cur.fetchall()

# cur.execute("select * from Shop")
# res = cur.fetchmany(size=10)
# print(res)

# TODO Имена столбцов таблицы
# cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
# print(cur.fetchall())



np.random.seed(10)

n = 100

products = {
    'Laptop': 1200.00,
    'Keyboard': 80.00,
    'Mouse': 25.00,
    'Monitor': 300.00,
    'Tablet': 500.00
}

df = pd.DataFrame({
    'order_id': range(1001, 1001 + n),
    'user_id': np.random.randint(101, 151, n),
    'date': pd.date_range('2026-01-01', periods=n, freq='D'),
    'product': np.random.choice(list(products.keys()), n),
    'quantity': np.random.randint(1, 5, n),
    'store': np.random.choice(['A', 'B', 'C'], n)
})

df['price'] = df['product'].map(products)

# порядок столбцов
df = df[
    ['order_id', 'user_id', 'date',
     'product', 'price', 'quantity', 'store']
]

df = df.sample(frac=1, random_state=10).reset_index(drop=True)

df.to_csv('raw_orders.csv', index=False)

print(df.head())

















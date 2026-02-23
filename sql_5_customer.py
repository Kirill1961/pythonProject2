"""
В этом коде, удаляем столбец таблицы Customers так:
- создаём дубликат Customers_one
- переносим нужные колонки из Customers в Customers_one
- удаляем Customers
- переименовываем Customers_one в Customers
"""


import sqlite3

con = sqlite3.connect("ordered.db")
cur = con.cursor()

# Создаём таблицы в базе ordered.db
cur.execute("""
    CREATE TABLE IF NOT EXISTS Orders(
    order_num INTEGER PRIMARY KEY AUTOINCREMENT,
    id_customer INTEGER,
    FOREIGN KEY (id_customer) REFERENCES Customers(id_customer)
)
""")

# Создам нову таблицу Orders_one, тк немогу убрать None
cur.execute("""
    CREATE TABLE IF NOT EXISTS Orders_one(
    order_num INTEGER PRIMARY KEY AUTOINCREMENT,
    id_customer INTEGER,
    FOREIGN KEY (id_customer) REFERENCES Customers(id_customer)
)
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Customers(
    id_customer INTEGER PRIMARY KEY AUTOINCREMENT,
    name_custom TEXT UNIQUE
);
""")

# Так как удаление колонки невозможно в sqlite3, создаём новую таблицу
cur.execute("""
    CREATE TABLE IF NOT EXISTS Customers_one (
    id_customer INTEGER PRIMARY KEY AUTOINCREMENT,
    name_custom TEXT
);
""")

# переносим из старой таблицы нужные колонки
cur.execute("""
INSERT INTO Customers_one (id_customer, name_custom)
SELECT id_customer, name_custom FROM Customers;

""")

# Удаляем старую таблицу
cur.execute("DROP TABLE Customers;")

# Переименовываем промежуточную таблицу, заменяем на имя от старой таблицы
cur.execute("ALTER TABLE Customers_one RENAME TO Customers;")

con.commit()

# добавили в Customers имена и id покупателей
data_customer = [("U"), ("A"), ("K"), ("S"), ("K")]
cur.executemany("INSERT OR IGNORE INTO Customers ( name_custom) VALUES (?)", data_customer)

# Извлекаем PK - колонку id_customer  из табл Customers
id_customer = cur.execute("SELECT id_customer FROM Customers ").fetchall()
print(id_customer, "d_customer  из табл Customers")

# Пишем в табл Orders в Колонку id_customer - id_customer из Customers
cur.executemany("INSERT OR IGNORE INTO Orders (id_customer) VALUES (?)", (id_customer))

# Вывод всех таблиц в базе
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(f" Таблицы:{cur.fetchall()}")

# Проверка структуры таблицы
cur.execute("PRAGMA table_info(Customers)")
print(cur.fetchall())

# вывод строк
cur.execute("SELECT * FROM Customers")
rows = cur.fetchall()
for row in rows:
    print(row, "Customers")

# Структура таблиц
cur.execute("PRAGMA table_info(Orders)")
print(cur.fetchall())

cur.execute("PRAGMA table_info(Orders_one)")
print(cur.fetchall())

# Вывод строк таблица Orders из колонок order_num, id_customer
cur.execute("SELECT order_num, id_customer FROM Orders")

rows = cur.fetchall()
for row in rows:
    print(row, "Orders")

res = cur.execute("SELECT name FROM sqlite_master WHERE name='ordered.db'")
print(res.fetchall())

" Удаляем все строки из таблицы "
cur.execute("DELETE FROM Orders")
cur.execute("DELETE FROM Customers")

con.commit()

" Удаление таблиц"
# for table in tables:
#     table_name = table[0]
# cur.execute(f"DROP TABLE IF EXISTS {'Customers_one'}")
# print(f"Таблица {'Customers_one'} удалена.")


cur.close()
con.close()
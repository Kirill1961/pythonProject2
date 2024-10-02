import sqlite3

con = sqlite3.connect("ordered.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Orders(
    order_num INTEGER PRIMARY KEY AUTOINCREMENT,
    id INTEGER,
    id_customer INTEGER,
    FOREIGN KEY (id_customer) REFERENCES Customers(id_customer)
)
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Customers(
    id_customer INTEGER PRIMARY KEY AUTOINCREMENT,
    name_custom TEXT
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
data_customer = [("U"), ("A"), ("K")]
cur.executemany("INSERT OR IGNORE INTO Customers ( name_custom) VALUES (?)", data_customer)



# Вывод всех таблиц в базе
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(f" Таблицы:{cur.fetchall()}")

# Проверка структуры таблицы
cur.execute("PRAGMA table_info(Orders)")
print(cur.fetchall())

cur.execute("SELECT * FROM Orders")
rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()
con.close()
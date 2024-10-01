import sqlite3

# Подключение к базе данных
con = sqlite3.connect("deltaks.db")
cur = con.cursor()

# Таблица Shop с уникальной датой (data)
cur.execute('''
CREATE TABLE IF NOT EXISTS Shop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT UNIQUE
)
''')

# Таблица Manager с именем менеджера
cur.execute('''
CREATE TABLE IF NOT EXISTS Manager (
    id_manager INTEGER PRIMARY KEY AUTOINCREMENT,
    manager_name TEXT
)
''')

# Таблица Orders с внешними ключами на Shop и Manager, а также стоимостью заказа
cur.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_id INTEGER,
    manager_id INTEGER,
    cost_orders INTEGER,
    FOREIGN KEY (data_id) REFERENCES Shop(id),
    FOREIGN KEY (manager_id) REFERENCES Manager(id_manager)
)
''')

# Таблица Sales с внешними ключами на Shop и Manager, а также стоимостью продаж
cur.execute('''
CREATE TABLE IF NOT EXISTS Sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_id INTEGER,
    manager_id INTEGER,
    cost_sales INTEGER,
    FOREIGN KEY (data_id) REFERENCES Shop(id),
    FOREIGN KEY (manager_id) REFERENCES Manager(id_manager)
)
''')

con.commit()

# Пример ввода данных
# Вставка в таблицу Shop
cur.execute("INSERT OR IGNORE INTO Shop (data) VALUES (?)", ("01.10.24",))

# Вставка в таблицу Manager
cur.execute("INSERT OR IGNORE INTO Manager (manager_name) VALUES (?)", ("U",))

# Получение ID только что вставленных записей
shop_id = cur.execute("SELECT id FROM Shop WHERE data = ?", ("01.10.24",)).fetchone()[0]
manager_id = cur.execute("SELECT id_manager FROM Manager WHERE manager_name = ?", ("U",)).fetchone()[0]

# Вставка данных в таблицу Orders
cur.execute("INSERT INTO Orders (data_id, manager_id, cost_orders) VALUES (?, ?, ?)",
            (shop_id, manager_id, 50000))

# Вставка данных в таблицу Sales
cur.execute("INSERT INTO Sales (data_id, manager_id, cost_sales) VALUES (?, ?, ?)",
            (shop_id, manager_id, 100000))

con.commit()

# Вывод данных
cur.execute("SELECT Shop.id, Shop.data, Manager.manager_name, Orders.cost_orders FROM Orders JOIN Shop ON Orders.data_id = Shop.id JOIN Manager ON Orders.manager_id = Manager.id_manager")
orders_result = cur.fetchall()
print("Orders:", orders_result)

cur.execute("SELECT Shop.id,  Shop.data, Manager.manager_name, Sales.cost_sales FROM Sales JOIN Shop ON Sales.data_id = Shop.id JOIN Manager ON Sales.manager_id = Manager.id_manager")
sales_result = cur.fetchall()
print("Sales:", sales_result)

cur.close()
con.close()

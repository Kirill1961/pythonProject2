import sqlite3

con = sqlite3.connect("delta.db")
cur = con.cursor()

# Таблица Shop, UNIQUE - ограничения на одинаковые значения

cur.execute('''
CREATE TABLE IF NOT EXISTS Shop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_event TEXT UNIQUE
)
''')


# INSERT OR IGNORE, в случае попытки вставки дубликата,
# ✅ SQL просто игнорирует команду вставки вместо того, чтобы выбрасывать ошибку
shop = cur.execute("""INSERT OR IGNORE INTO Shop (data_event) VALUES ("30.09.2024")""")
con.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS Manager (
    id_manager INTEGER PRIMARY KEY AUTOINCREMENT,
    manager_name TEXT
)
''')

manager = cur.execute("""INSERT INTO Manager (id_manager, manager_name) VALUES (NULL, "U")""")
con.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_id INTEGER,
    manager_id INTEGER,
    FOREIGN KEY (data_id) REFERENCES Shop(id),
    FOREIGN KEY (manager_id) REFERENCES Manager(id_manager)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_id INTEGER,
    manager_id INTEGER,
    FOREIGN KEY (data_id) REFERENCES Shop(id),
    FOREIGN KEY (manager_id) REFERENCES Manager(id_manager)
)
''')

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())


res_1 = cur.execute("SELECT id, data_event FROM Shop")
print(res_1.fetchone(), "res_1")



# Проверка структуры таблицы
cur.execute("PRAGMA table_info(Manager)")
print(cur.fetchall())

cur.execute("SELECT * FROM Manager")
rows = cur.fetchall()

# Вывод строк
for row in rows:
    print(row)

cur.close()
con.close()
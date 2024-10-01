import sqlite3

con = sqlite3.connect("delta.db")
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Shop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_event TEXT UNIQUE
)
''')

# shop = cur.execute("""INSERT INTO Shop (data_event) VALUES ("30.09.2024")""")
# con.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS Manager (
    id_manager INTEGER PRIMARY KEY AUTOINCREMENT,
    manager_name TEXT
)
''')

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


res_1 = cur.execute("SELECT data_event FROM Shop")
print(res_1.fetchall())


# Проверка структуры таблицы
cur.execute("PRAGMA table_info(Shop)")
print(cur.fetchall())

cur.close()
con.close()
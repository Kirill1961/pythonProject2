import sqlite3

# Создаём Connection
con = sqlite3.connect("tut.db")
cur = con.cursor()

# Создаем таблицу с id как PRIMARY KEY
cur.execute("""
CREATE TABLE IF NOT EXISTS tab3 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Data_event TEXT,
    Manager TEXT,
    Orders INTEGER, 
    Sales INTEGER
)
""")

# Коммитим
con.commit()

# Вставляем строки (id пропускается, т.к. оно автогенерируется)
data = [
    ("24.09.24", "U", 15000, 250000),
    ("25.09.24", "A", 11000, 270000),
    ("26.09.24", "U", 113000, 310000),
    ("27.09.24", "A", 117000, 380000),
    ("28.09.24", "U", 119000, 350000)
]

# Вставка данных без указания id
cur.executemany("INSERT INTO tab3 (Data_event, Manager, Orders, Sales) VALUES (?, ?, ?, ?)", data)
con.commit()

# Выводим первые пять строк, включая id
for row in cur.execute("SELECT * FROM tab3 LIMIT 5"):
    print(row)

# Вывод уникальных значений колонок
unic = list(cur.execute("SELECT DISTINCT Manager FROM tab3"))
print(f" Уникальные значения колонки Manager {unic}")

# Проверка структуры таблицы
cur.execute("PRAGMA table_info(tab3)")
print(cur.fetchall())


# Вывод всех таблиц в базе
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())
# tables = cur.fetchall()

# Удаление таблиц
# for table in tables:
#     table_name = table[0]
cur.execute(f"DROP TABLE IF EXISTS {'tab'}")
print(f"Таблица {'tab'} удалена.")


# Закрытие курсора и соединения
cur.close()
con.close()


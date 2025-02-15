"""
- Красивый Вывод всех таблиц в базе
- Метаданные колонок
"""

import sqlite3

# Создаём ОБ Connection
con = sqlite3.connect("tut.db")
# Из Connection-объекта берём метод cursor
cur = con.cursor()

# Создали таблицу, задаём имена столбов, IF NOT EXISTS - что бы не дублировать
cur.execute("""
CREATE TABLE IF NOT EXISTS tab3(
id INTEGER PRIMARY KEY AUTOINCREMENT,
Data_event TEXT UNIQUE,
Orders INTEGER UNIQUE, 
Sales INTEGER UNIQUE
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS tab4(
id INTEGER PRIMARY KEY,
Name TEXT,
Age INTEGER
)
""")

# Добавим колонку
# cur.execute("ALTER TABLE tab3 ADD COLUMN Manager TEXT")

# Коммитим
con.commit()

# Проверка структуры таблицы
cur.execute("PRAGMA table_info(tab4)")
print(f"Структура -> {cur.fetchall()}")

# sqlite_master - Проверяем создание таблицы, WHERE name - поиск по имени
res = cur.execute("SELECT name FROM sqlite_master WHERE name='tab3'")
print(res.fetchall(), ">>>>>>>")

# Вставляем строки в таблицу, число элементов строки равны числу столбов
cur.execute("""
INSERT OR IGNORE INTO tab3 (Data_event, Manager, Orders, Sales) VALUES 
            ("24.09.24", "U", 15000, 250000),
            ("25.09.24", "A", 11000, 270000)
""")

cur.execute("INSERT INTO tab4 (Name, Age) VALUES('Kirill', 53)" )
print(cur.execute("SELECT * FROM tab4").fetchall())

# cur.execute("""
# INSERT INTO tab4 (id, Name, Age) VALUES(NULL, "Kirill", 53)
# """)

# commit() - Коммитим, Фиксируем транзакцию
con.commit()

# Вывод строки из указанного столба
res_1 = cur.execute("SELECT Data_event FROM tab3")
# print(res_1.fetchall())

# Вставим дополнительные строки из словаря data
data = [
    ("26.09.24", "U", 113000, 310000),
    ("27.09.24", "A", 117000, 380000),
    ("28.09.24", "U", 119000, 350000),
]

# (?, ?, ?, ?) - заполнители, executemany - автоматически подставляет значения из строки НА место вопроса ?
# Явно указать имена колонок так как неправильно расставлены при вводе
cur.executemany("INSERT OR IGNORE INTO tab3 (Data_event, Manager, Orders, Sales) VALUES  (?, ?, ?, ?)", data)
con.commit()


# Среднее колонки
avereg = cur.execute("SELECT AVG(Orders) FROM tab3")
print(list(avereg))


# Вывод заданных колонок
# for row in cur.execute(("SELECT  Data_event ,  Manager  FROM tab3 ORDER BY  Orders")):
#     print(row)



# Вывод всех колонок, rowid - вывод id
# * это имена всех колонок,
for row in cur.execute("SELECT * FROM tab3"):
    ...
    # print(row)


# Вывести все колонки, последние 5 строк из таблицы tab3, сортируя по id в обратном порядке
# ORDER BY id DESC сортирует записи по убывающей, начиная с самой последней
# cur.execute("SELECT * FROM tab3 ORDER BY id DESC LIMIT 5")
# rows = cur.fetchall()

# Вывод строк
# for row in rows:
#     print(row)

# Метаданные для одной таблицы
column_names = [description[0] for description in cur.description]
print(f"Метаданные tab3: {column_names}")

# Проверка структуры таблицы
cur.execute("PRAGMA table_info(tab3)")
print(cur.fetchall())


# Вывод всех таблиц в базе
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())

# Красивый Вывод всех таблиц в базе
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
if tables:
    print("База данных существует и содержит следующие таблицы:")
    for table in tables:
        print(table[0])
else:
    print("База данных создана, но не содержит таблиц.")
cur.close()
con.close()
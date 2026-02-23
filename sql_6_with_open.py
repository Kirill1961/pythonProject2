"""
- Менеджер контекста
- используется для небольших скриптов и коротких сессий работы с базами данных.
- ✅ не требуется Комитить и закрывать соединение(con.commit(), cur.close(), con.close()
"""

import pandas as pd
import sqlite3

with sqlite3.connect("base_orders.db")as con:
    cur = con.cursor()

res = cur.execute("SELECT name FROM sqlite_master WHERE name='base_orders.db'")
print(res.fetchall())

# Создаём таблицы в базе ordered.db
query = ("""
    CREATE TABLE IF NOT EXISTS Orders(
    order_num INTEGER PRIMARY KEY AUTOINCREMENT,
    id_customer INTEGER,
    FOREIGN KEY (id_customer) REFERENCES Customers(id_customer)
);
   CREATE TABLE IF NOT EXISTS Customers(
    id_customer INTEGER PRIMARY KEY AUTOINCREMENT,
    name_custom TEXT UNIQUE
)
""")



# Удаляем все строки из таблицы base_orders.db
# cur.execute("DELETE FROM Orders")
# cur.execute("DELETE FROM Customers")
# con.commit()
def data():
    name = input("Name: ")
    # добавили в Customers имена и id покупателей
    cur.execute("INSERT OR IGNORE INTO Customers ( name_custom) VALUES (?)", [name])

    # 1-й вариант Извлечение из табл Customers значения id_customer
    id = cur.execute("SELECT id_customer FROM Customers").fetchall()
    print(f"fetch id from Customers -> {id}")

    # 2-й вариант lastrowid - извлечь только что сгенерированный идентификатор id_customer
    # (cur.lastrowid,) - запятая для изменения типа int на тип tuple
    value = (cur.lastrowid,)
    print(f"(lastrowid,)-меняем тип структуры с int на tuple -> {value}")

    # Запись в табл Orders в поле id_customer из табл Customers
    cur.executemany("INSERT INTO Orders (id_customer) VALUES (?)", id)

    # Проверка структуры таблицы
    cur.execute("PRAGMA table_info(Orders)")
    print(f"Структура -> {cur.fetchall()}")

    column_names = [description[0] for description in cur.description]
    print(f"Метаданные : {column_names}")

    row_customer = cur.execute("SELECT id_customer, name_custom FROM Customers").fetchall()
    # print(row_customer, "Customers")

    # Извелечение id для определённого name_custom
    row_order = cur.execute("SELECT id_customer, order_num FROM Orders").fetchall()
    # print(row_order, "Orders")


    # Совместный вывод двух таблиц Orders и Customers, извлекаем по условию совпадения id_customer
    total = cur.execute("SELECT Orders.order_num, Customers.id_customer, "
                        "Customers.name_custom FROM Orders JOIN Customers ON Orders.id_customer = Customers.id_customer")
    # print(total)
    df = pd.DataFrame(total, columns=[ "order_num", "id_customer", "name_custom"])
    print(df)


data()



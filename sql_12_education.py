import psycopg2

conn = psycopg2.connect(
    dbname="db333",
    user="postgres",
    password="1961km1",
    host="localhost",
    port=5432
)

cur = conn.cursor()

# Автокоммит Назначен
conn.autocommit = True

famil = ("""CREATE TABLE IF NOT EXISTS famil(
           id  SERIAL,
            val_int int,
            val_char char (10)
)           
""")

data_val = [
    (100, 'Kir'),
    (25, 'Svet'),
    (500, 'Andr'),
    (33, 'Jul'),
    (777, 'Arty')
]

# Первоначальное заполнение таблицы
# insrt = ("""
# INSERT INTO  famil( val_int, val_char) VALUES (%s, %s)
# """)

# Запрос Создание таблицы
cur.execute(famil)

# Запрос Первоначальное заполнение таблицы
# cur.executemany(insrt, data_val)

# Вставка ещё одной строки
# cur.execute(
#     """
#     insert into famil  (val_int, val_char)
#     values (99, 'Bim')
#     """
# )


# Вывод запроса
cur.execute("""
SELECT * FROM famil
""")
f = cur.fetchall()
print(f)

# Наличие Автокомита
print(conn.autocommit)

# В Ручную Подтверждаем изменени
# conn.commit()

# Закрываем курсор и соединение
cur.close()
conn.close()





import psycopg2

# Данные для подключения
conn = psycopg2.connect(
    host="your_host",      # Хост (например, elephantsql.com)
    port="5432",           # Порт
    database="your_db",    # Имя базы данных
    user="your_user",      # Логин
    password="your_password" # Пароль
)

cur = conn.cursor()
cur.execute("SELECT * FROM your_table")
rows = cur.fetchall()
print(rows)

# Используем менеджер контекста для автоматического закрытия соединения
with psycopg2.connect(dbname="my_database", user="my_user", password="my_password", host="localhost") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM my_table")
        rows = cur.fetchall()
        for row in rows:
            print(row)

cur.close()
conn.close()

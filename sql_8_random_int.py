import psycopg2
import random
from psycopg2 import OperationalError


# Подключение к базе данных
conn = psycopg2.connect(
    dbname="db3",  # имя базы данных
    user="postgres",  # ваш логин
    password="1961km1",  # ваш пароль
    host="localhost",  # хост, например, localhost
    port="5432"  # порт, стандартный для PostgreSQL
)

# Создаем курсор для выполнения SQL запросов
cur = conn.cursor()

cur.execute("INSERT INTO public.tab5(num) values (55)")


# SQL-запрос для получения всех таблиц в текущей базе данных
cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public';
        """)

# print(cur.fetchall())

# Извлекаем результат запроса и выводим таблицы
tables = cur.fetchall()
for table in tables:
    print(table)
# def check_connection():
#     try:
#         # Попытка подключения
#         conn = psycopg2.connect(
#             dbname="db3",  # имя базы данных
#             user="postgres",  # ваш логин
#             password="1961km1",  # ваш пароль
#             host="localhost",  # хост, например, localhost
#             port="5432"  # порт, стандартный для PostgreSQL
#         )
#         print("Подключение успешно!")
#         conn.close()
#     except OperationalError as e:
#         # Если ошибка при подключении, выводим сообщение
#         print(f"Ошибка подключения: {e}")
#
# # Вызов функции проверки подключения
# check_connection()

# Генерация случайных чисел и вставка их в таблицу
random_numbers = [(random.randint(1, 100),) for _ in range(10)]
insert_query = "INSERT INTO tab4 (num) VALUES (%s)"
cur.executemany(insert_query, random_numbers)

# вывод колонки num
cur.execute("SELECT num FROM tab4 ")
print(cur.fetchall())
cur.execute("SELECT num FROM tab5 ")
print(cur.fetchall())

# Подтверждаем изменения
conn.commit()

# Закрываем курсор и соединение
cur.close()
conn.close()

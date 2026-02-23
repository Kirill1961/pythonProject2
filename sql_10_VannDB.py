import psycopg2
import random
from psycopg2 import OperationalError


# Подключение к базе данных
conn = psycopg2.connect(
    dbname="VannDB",  # имя базы данных
    user="postgres",  # ваш логин
    password="1961km1",  # ваш пароль
    host="localhost",  # хост, например, localhost
    port="5432"  # порт, стандартный для PostgreSQL
)

# Создаем курсор для выполнения SQL-запроса
# conn.autocommit = True
cur = conn.cursor()

# Выполняем запрос на создание базы данных
# cur.execute("CREATE DATABASE dbVan")



cur.execute("""CREATE TABLE IF NOT EXISTS basket_a 
    a INT PRIMARY KEY,
    fruit_a VARCHAR (100) NOT NULL,
    FOREIGN KEY (a) REFERENCES (b)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL,
    FOREIGN KEY b REFERENCES a
)""")

cur.execute("""INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber')""")


cur.execute("""INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear')""")


cur.execute("SELECT fruit_a FROM basket_a ")
print(cur.fetchall())

cur.execute("SELECT fruit_b FROM basket_b ")
print(cur.fetchall())

# Подтверждаем изменения
conn.commit()

# Закрываем курсор и соединение
cur.close()
conn.close()
import psycopg2


# Подключение к базе данных
conn = psycopg2.connect(
    dbname="Eduson",  # имя базы данных
    user="student",  # ваш логин
    password="QweAsd1234567890!",  # ваш пароль
    host="185.86.147.205",  # хост, например, localhost
    port=5432  # порт, стандартный для PostgreSQL
)

# conn = psycopg2.connect(
#     dbname='nordwind',  # имя базы данных
#     user='student',  # ваш логин
#     # password="qweasd1234567890",  # ваш пароль
#     password='qweasd963',  # ваш пароль
#     host='89.208.197.76',  # хост, например, localhost
#     port=5432  # порт, стандартный для PostgreSQL
# )


# Создаем курсор для выполнения SQL запросов
cur = conn.cursor()

# cur.execute("SELECT * FROM shippers")
# print(cur.fetchall())

cur.execute(
   """select *
from employee_territories et 
full join territories t 
on et.territory_id = t.territory_id;"""
)
cur_fetch = cur.fetchall()
for i in cur_fetch:
    print (i)


# f_connect("Eduson", "student", "QweAsd1234567890!", "185.86.147.205", 5432)
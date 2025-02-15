import psycopg2
from psycopg2 import sql

# Параметры подключения к серверу PostgreSQL (сначала подключаемся без базы данных)
connection_params = {
    "dbname": "postgres",  # Стандартная база для управления
    "user": "postgres",    # Ваш пользователь PostgreSQL
    "password": "1961km1",  # Ваш пароль
    "host": "localhost",   # Адрес сервера
    "port": "5432"         # Порт (по умолчанию)
}

# Имя базы данных, которую нужно создать
new_database_name = "NorthWind"

try:
    # Подключаемся к серверу PostgreSQL
    with psycopg2.connect(**connection_params) as conn:
        conn.autocommit = True  # Для выполнения CREATE DATABASE


    # Создаем курсор для выполнения команд SQL
    with conn.cursor() as cur:
            # SQL-запрос для создания базы данных
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_database_name)))
        print(f"База данных '{new_database_name}' успешно создана.")

except psycopg2.Error as e:
    print("Ошибка при создании базы данных:", e)
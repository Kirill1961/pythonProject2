import sqlite3
# import duckdb

# # NorthWind
# HOST = "localhost"
# PORT = 5432
# DATABASE = "NorthWind"
# USER = "postgres"
# PASSWORD = "1961km1"

path = r"C:/Users/Kirill/PycharmProjects/pythonProject2/tut.db"

# conn = sqlite3.connect("tut.db")
conn = sqlite3.connect("delta.db")

cur = conn.cursor()

res = cur.fetchall()

# cur.execute("select * from Shop")
# res = cur.fetchmany(size=10)
# print(res)

# TODO Имена столбцов таблицы
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())

















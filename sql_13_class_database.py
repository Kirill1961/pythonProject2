import psycopg2

# db333
HOST = "localhost"
PORT = 5432
DATABASE = "db333"
USER = "postgres"
PASSWORD = "1961km1"

# NorthWind
# HOST = "localhost"
# PORT = 5432
# DATABASE = "NorthWind"
# USER = "postgres"
# PASSWORD = "1961km1"

class DB333:
    def __init__(self, dbname, host, port, user, password, autocommit=False):
        self.conn = psycopg2.connect(
            dbname=dbname,
            host=host,
            port=port,
            user=user,
            password=password
        )

        self.cur = self.conn.cursor()

# Подтверждение автокоммита в случае запуска с autocommit = True
        if autocommit:
            self.conn.autocommit = True

# Запрос и Вывод fetchall сразу в Запросе
    def select(self, req, vars=None):
        self.cur.execute(req, (vars,))  # !!! Кортеж обязателен
        res_ex = self.cur.fetchall()
        return res_ex

# Можно так Отдельно Вывод fetchall
    def res_select(self):
        res_fetch = self.cur.fetchall()
        return res_fetch


# Явное задание автокоммита для DELETE, UPDATE и тд,  если стандартно autocommit = False
    def post(self, req, vars=None):
        self.cur.execute(req, vars)
        if not self.conn.autocommit:
            self.conn.commit()   # Явно в ручную Закоммиченн результат запроса




db1 = DB333(
DATABASE,
HOST,
PORT,
USER,
PASSWORD
)

# Запрос через Экземпляр в DB333
res_333_1 = db1.select(
    """
    select *
    from famil
    """
)

print(res_333_1)


res_333_2 = db1.post(
    """
    update famil
    set val_char = 'BimBos'
    where id = 13
    """
)


# Запрос через Экземпляр в NorthWind
# res_N1 = db1.select(
#     """
#     select order_id
#     from orders
#     limit 2
#     """
# )
#
# print(f'Запрос из orders через Экземпляр в NorthWind: {res_N1}')
#
# res_N2 = db1.select(
#     """
#     select order_id
#     from order_details
#     limit 4
#     """
# )
#
# print(res_N2)
#
# #  Преобразование запроса из orders
# id_ord = tuple(i[0] for i in res_N1)
# print(f'Преобразование запроса из orders в tuple(int): {id_ord}')
#
# res_N3 = db1.select(
#     """
#     select *
#     from order_details
#     where order_id in %s
#     """,
# id_ord
# )
#
# print(res_N3)
from collections import Counter, defaultdict

frdsh = [(0, 3), (2, 0), (3, 2), (1, 3), (4, 0)]
users: list[dict] = [{'id': 50, 'name': 'Sveta'}, {'id': 10, 'name': 'Jhon'}, {'id': 20, 'name': 'Ray'},
                     {'id': 30, 'name': 'Ciril'}, {'id': 40, 'name': 'David'}]

# Дружественные связи

for user in users:
    user['friends'] = []

for i, j in frdsh:
    print(i, j, ' connect fr')

    users[i]['friends'].append(j)

    users[j]['friends'].append(i)

print(users, ' users ')


# user имеющий наибольшее кол-во связей

def max_friend():  # user имеющий наибольшее кол-во связей
    list_bound = [len(val['friends']) for val in users]
    max_bound_friend = max(list_bound)
    index_max_bound = list_bound.index(max_bound_friend)
    return users[index_max_bound]['name']


print(max_friend(), ' have_max_bound_friend')


def max_friend():
    for user in users:
        print(user['id'], len(user['friends']), ' max_friend')


max_friend()


# def fr_of_fr_id_b(user):
#
#     for friend in user['friends']:
#         print(friend,  'friends of user vs id "0"')
#         for k in users[friend]['friends']:
#             print(k, '   index friend of friend user[0]', len(users))
#             # print(users[k]['friends'], '  foaf user[0]')
#             users[0]['foaf'] = [k]
# fr_of_fr_id_b(users[0])


# индексы друзей его(user) друзей

def fr_of_fr_id_b(user):
    # res = [users[foaf] for friend in user['friends'] for foaf in users[friend]['friends']]
    res = [foaf for friend in user['friends'] for foaf in users[friend]['friends']]
    user['foaf'] = res  # индексы друзей его(user) друзей
    return (len(res))


print(fr_of_fr_id_b(users[1]), ' -  кол-во друзей у друзей данного user[id]')

print(users)

# print('   индексы друзей - друзей user[id]')
#
# print([friend for friend in users[0]['friends']])
# print([friend for friend in users[1]['friends']])
# print([friend for friend in users[2]['friends']])
# print([friend for friend in users[3]['friends']])


print('  WHILE  индексы друзей - друзей user[id]')
a = 0
while a < len(users):
    a += 1
    res_friend = [friend for friend in users[a - 1]['friends']]
    print(res_friend)

print('  WHILE  количество друзей - друзей user[id]')
a = 0
while a < len(users):
    a += 1


    def fr_of_fr_id_b(user):
        # res = [users[foaf] for friend in user['friends'] for foaf in users[friend]['friends']]
        res = [foaf for friend in user['friends'] for foaf in users[friend]['friends']]
        user['foaf'] = res  # индексы друзей его(user) друзей
        return (len(res))


    print(fr_of_fr_id_b(users[a - 1]), ' -  кол-во друзей у друзей данного user  ' + f'{a - 1}')

# если id разные то пользователи неодинаковые
print('  compare user of [id] for to choose "user " and "other_user" ')


def not_the_same(user, other_user):
    return (user != other_user)


print(not_the_same(users[0]['friends'], users[3]['friends']), '           если id разные то пользователи неодинаковые')

print('  friends my friends but without me')


def not_the_same(user: [dict], other_user):
    return user['id'] != users[other_user]['id']


def not_friends(user, other_user):
    return all(not_the_same(user, friend) for friend in user['friends'])


# id друзей его друзей исключая меня
def friends_of_friend_ids(user):
    return Counter(foaf for friend in user['friends'] for foaf in users[friend]['friends']
                   if not_the_same(user, foaf) and not_friends(user, foaf))

    # return Counter(foaf for friend in user['friends'] for foaf in users[friend]['friends'] )


print(friends_of_friend_ids(users[2]), '        id друзей его друзей исключая меня')

# Сортировак по увлечениям

interests = [(50, 'Hadoop'), (50, 'Python'), (50, 'HBase'), (50, 'Java'), (50, 'Spark'), (50, 'Storm'),
             (10, 'NoSQL'), (10, 'MongoDB'), (10, 'HBase'), (10, 'data science'), (10, 'Java'), (10, 'Storm'),
             (20, 'Hadoop'), (20, 'numpy'), (20, 'pandas'), (20, 'Java'), (20, 'HBase'), (20, 'Python'),
             (30, 'pandas'), (30, 'Python'), (30, 'data science'), (30, 'numpy'), (30, 'Spark'), (30, 'NoSQL'),
             (40, 'Java'), (40, 'Python'), (40, 'Storm'), (40, 'numpy'), (40, 'HBase'), (40, 'NoSQL')]


def data_scien_hwo_like(target_interest: [str]):
    return [user_id for user_id, user_interest in interests if user_interest == target_interest]


print(data_scien_hwo_like('Hadoop'), '                <- какому id нравится данное увлечение ')


def all_users_by_interests():
    s = list(set([tuple_in_list[1] for tuple_in_list in interests]))
    n = 0
    while n < len(s):
        n += 1
        m = {s[n - 1]: [i[0] for i in interests if s[n - 1] == i[1]]}
        print(n - 1, m)


all_users_by_interests()

d = defaultdict(list)

for k, v in interests:
    # print(k, v)
    d[v] += [k]
print(d)

# Сортировка по стажу и ЗП

salary_by_tenure = defaultdict(list)
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 0.6),
                        (69000, 6.5), (76000, 7 / 5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
print(salary_by_tenure, '            salary_by_tenure')

average_salaries_and_tenures = {tenure: sum(salaries) / len(salaries) for tenure, salaries in salary_by_tenure.items()}
print(*average_salaries_and_tenures.keys())


def tenure_bucket(tenure):
    if tenure < 2:
        return 'менее двух'
    elif tenure < 5:
        return 'между двумя и пятью'
    else:
        return 'больше пяти'


salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {tenure_bucket: sum(salaries) / len(salaries) for tenure_bucket, salaries
                            in salary_by_tenure_bucket.items()}

print(average_salary_by_bucket, '       ЗП в зависимости от стажа')


#  какая группа по стажу вовремя оплачивает счета

def tenure_bucket(years_experience):
    if years_experience < 3.0:
        return 'уплочено'
    elif years_experience < 8.5:
        return 'не уплочено '
    else:
        return 'уплочено'


print(tenure_bucket(4.2), '          какая группа по стажу вовремя оплачивает счета')

words_and_counts = Counter(word for user, interest in interests for word in interest.lower().split())
print(words_and_counts)

# ВЕКТОРЫ, сложение ,вычитание , умножение и тд

v = [1, 2]  # вектор v
w = [2, 1]  # вектор w


def vector(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


print(vector([1, 2], [2, 1]), ' Сложение векторов *******************')

# partial, на основе класса int создаём ф-ю basetwo с доп аргументом

from functools import partial

str_int = '1001'

basetwo = partial(int, base=2)
print(basetwo(str_int))


def func(a, b, c=8):
    return a + b + c


functwo = partial(func, c=1000)  # на основе ф-ции func(a, b, c=8  создаём ф-ю basetwo с доп аргументом
print(functwo(200, 800))

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(A[1][2], 'shape')


def shape(A):
    rows = len(*A)
    cols = len(*A[0])
    return rows, cols


print(A)


def shape(*A):
    num_rows = len(A)  # количество строк
    num_cols = len(A[0])  # количество столбцов
    print(num_rows, num_cols, ' количество строк и столбцов ')


shape(*A)


def a_str(A, i):
    return A[i]  # i - ая строка в матрице n x k


print(a_str(A, i=0), ' i - ая строка в матрице n x k')


def a_cols(A, j):
    return [j_cols[j] for j_cols in A]  # j - ый столбец в матрице n x k


print(a_cols(A, 2), ' j - ый столбец в матрице n x k')


def i_j_elem(i, j):
    return A[i][j]  # (i, j) - й элемент в матрице


print(i_j_elem(2, 1))


# Создание единичной матрицы размер  num_rows х num_cols, вывод в строку
# (i, j) - й элемент в матрице = entry_fn(i,j)

def make_matrix(num_rows, num_cols, entry_fn):
    ret = [entry_fn(i, j) for j in range(num_cols) for i in range(num_rows)]
    print(ret, ' единичная матрица в строку без return')


def is_diagоnal(i, j):
    return 1 if i == j else 0


print(make_matrix(3, 3, is_diagоnal), ' единичная матрица в строку c return')


# Создание единичной матрицы размер x * y; единица по диагонали  и вывод в таблице

def mat(x, y):
    r = 0
    arr = []
    for i in range(x):
        arr.append([])
        for j in range(y):
            a = 1 if i == j else 0
            arr[i].append(a)
            # r+=1
    for u in range(x):
        print(arr[u])


mat(5, 5)


# Создание матрицы размер x * y, с содержанием числового ряда от счётчика r+=1

def mat(x, y):
    r = 0
    arr = []
    for i in range(x):
        arr.append([])  # вставка в список пустых списков ори же строки
        for j in range(y):
            arr[i].append(r)
            r += 1  # r+=1 это наполнение матрицы
    for u in range(x):  # цикл формирует таблицу в столбик
        print(arr[u])


mat(2, 2)

# Единичная матрица дружеств связей в коллективе, 1 - дружит; 0 - недружит
# анализ по индексу участников списка all_ppl
all_people = [{'id': 11, 'name': 'Joe'}, {'id': 22, 'name': 'Bob'}, {'id': 33, 'name': 'Tom'},
              {'id': 44, 'name': 'Nick'}]

connect_friend = [(0, 1), (0, 2), (1, 2), (3, 2), (3, 0), (1, 3)]


def conn_fre(x, y):
    arry = []
    for w in range(x):
        arry.append([])
        for r in y:
            a = 1 if (w in r) == True else 0
            arry[w].append(a)
            # print(w, r, connect_friend.index(r), w in r)
    print(' ', *[e for e in range(len(connect_friend))], sep='  ')  # распаковали список с помощью звезды " * "
    for l in range(x):
        print(l, arry[l])


conn_fre(len(all_people), connect_friend)


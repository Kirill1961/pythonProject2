"""MapReduce - вид модели  пишется под конкретную задачу,
    mapper - проектор который привязывает ЭЛЕМЕНТ к ПОКАЗАТЕЛЮ пример: (word, 1) или (name_matrix, (i, j), value)
    reducer - коллектор, производит результирующую операцию с показателями - сложение, умножение и тд."""

import datetime
from collections import defaultdict, Counter
import re

# TODO begin
status_update = [{"id": 1,
                  "username": "Kirill",
                  "text": "Is anyone , scikit learn, pandas, data science, scikit learn, scikit learn, data_gal",
                  "created_at": datetime.datetime(2024, 2, 2, 10, 30, 16, 416716),
                  # "created_at": datetime.datetime.now(),
                  "liked_by": ["scikit learn", "pandas", "data science", "pandas", "Is anyone"]
                  },
                 {"id": 1,
                  "username": "Kirill",
                  "text": "Is anyone , pandas, data_gal, data science, scikit learn",
                  "created_at": datetime.datetime.now(),
                  "liked_by": ["data_gay", "data_gal", "data science", "data science", "data science"]
                  },
                 {"id": 2,
                  "username": "Sveta",
                  "text": "Networkx , Gensim, data science, Gensim",
                  "created_at": datetime.datetime.now(),
                  "liked_by": ["Is the  anytwo"]
                  },
                 {"id": 3,
                  "username": "joelgruss",
                  "text": "Is anyone , data science, pandas ",
                  "created_at": datetime.datetime.now(),
                  "liked_by": ["data_gay", "data_gal", "data science", "data_gal"]
                  },
                 {"id": 3,
                  "username": "joelgruss",
                  "text": "Is anyone ,Is anyone , data science, pandas ",
                  "created_at": datetime.datetime.now(),
                  "liked_by": ["data_gay", "data_gal", "Is anyone", "Is anyone"]
                  }
                 ]
# Класс datetime
time_now = datetime.datetime.now()  # time Moscow
time_now_timezone = datetime.datetime.now(datetime.timezone.utc)  # время GMT, нулевой меридиан
set_timezone_hours = datetime.timezone(datetime.timedelta(hours=+3))  # UTC/GMT + 3ч
time_now_timezone_hours = datetime.datetime.now(set_timezone_hours)  # заданное время относительно UTC

print(time_now, "time Moscow")
print(time_now_timezone, "время GMT, нулевой меридиан")
print(time_now_timezone_hours, "заданное время относительно UTC", "\n")
print(status_update, "\n")
print(time_now.weekday(), "weekday", "\n")  # weekday() - возвращает день недели для указанной даты.

print("Год:", status_update[0]["created_at"].year, " ", end='@')
print("Месяц:", status_update[0]["created_at"].month, " ", end='@')
print("День:", status_update[0]["created_at"].day, end='@')
print("Часы:", status_update[0]["created_at"].hour, end='@')
print("Минуты:", status_update[0]["created_at"].minute, end='@')
print("Секунды:", status_update[0]["created_at"].second)


# mapper - проектор для числа упоминаний в дни недели
def data_scince_day_mapper(status_update):
    for status_update_day in status_update:
        # yield status_update_day["text"]
        if "data science" in status_update_day["text"].lower():
            day_of_week = status_update_day["created_at"].weekday()  # weekday() - возвращает указанные дни недели
            yield day_of_week, 1
        else:
            day_of_week = status_update_day["created_at"].weekday()
            yield day_of_week, 0


# print(list(data_scince_day_mapper(status_update)), "tutorial:[(a, b)] a - день недели, b - число упоминаний слова ")

# редуктор
def sum_reduce(day_collect):
    for day_week, day_num in day_collect:
        yield day_week, sum(day_num)


# MapReduce
def map_reduce(in_put, mapper, reducer):
    collect = defaultdict(list)

    for day, count in mapper(in_put):
        collect[day].append(count)
    return reducer(collect.items())
    # yield collect


# дни когда упоминается "data science"
data_sciens_days = map_reduce(status_update, data_scince_day_mapper, sum_reduce)
print(list(data_sciens_days), "MapReduce - дни когда упоминается data science", "\n")


# проектор слова "data science" для каждого пользователя
def word_per_users_mapper(status_update):
    collect_user_word = defaultdict(list)
    for i in status_update:
        user, text = i["username"], i["text"]
        # print(user, text, "\n")
        word = "data science"
        if word in text:
            yield user, (word, 1)
        else:
            yield user, (word, 0)


# print(list(word_per_users_mapper(status_update)), "проектор слова data science для каждого пользователя", "\n")


# токенайзер
def tokenize(docum):
    # print(docum, ">>>>>>>>")
    pattern = r"[a-z0-9]+"
    # words = re.findall(pattern, docum)
    words = re.findall(r"[\W\w]+", docum)

    return [i.split(",") for i in words]


# проектор всех слов для одного пользователя
def word_per_user_mapper(stat_update):
    for doc in stat_update:
        user = doc["username"]
        for words in tokenize(doc["text"]):
            for word in words:
                yield [user, (word, 1)]


# print(list(word_per_user_mapper(status_update)), "проектор слов  для каждого пользователя", "\n")


# TODO mid

# Кол-во повторов слов для каждого user,
# defaultdict(int) считает повторы; defaultdict(dict)- update словарь с подсчётом {words:counts} к ключу users
def most_popular_word_reducer(words_and_counts):
    word_count = defaultdict(int)
    res_user_word_coun = defaultdict(dict)
    for user, (word, count) in words_and_counts:
        word_count[user, word] += count
        [(res_user_word_coun[users].update({words: counts})) for (users, words), counts in
         word_count.items()]  # изюменка
    # yield res_user_word_coun  # возврат генератора если вызываем напрямую most_popular_word_reducer()
    return res_user_word_coun  # простой возврат результата если используем обобщающую ф-цию mapp_reduce()


# print(list(most_popular_word_reducer(word_per_user_mapper(status_update))), "\n")  # Прямой вызов


#  Итоговая ф-ция включающая вспомогательные ф-ции word_per_user_mappe и most_popular_word_reducer
def map_reduce(in_put, mapper, reducer):
    # pass
    mapper_r = mapper(in_put)
    reducer_r = reducer(mapper_r)
    yield reducer_r


words_users = map_reduce(status_update, word_per_user_mapper, most_popular_word_reducer)
print(list(words_users), "MapReducer - сообщений всех юзеров ", "\n")


# Самопис подсчёта лайков
def liker_mapper(input):
    liker_count = defaultdict(int)
    liker_of_user = defaultdict(dict)
    wc = [(i['username'], i['liked_by']) for i in input]
    for user, liker in wc:
        for word in liker:
            words, counts = word, 1
            liker_count[user, words] += counts
            # liker_of_user[user].update(liker_count)
        for (user, words), counts in liker_count.items():  # крутим items(), перегруппировываем user, words, counts
            liker_of_user[user].update({words: counts})  # подсчитанные liker записываем в value liker_of_user
    return (liker_of_user)  # возврат для вызова через map_reducer()
    # yield (liker_of_user) # генератор прямого вызова liker_mapper()


# print(list(liker_mapper(status_update)), "прямой вызов")
# TODO end

#  Для каждого пользователя число пользователей которым нравится новостная лента данного user
def count_distinct_reducer(like_map):
    lm = [i for i in like_map]
    return lm

#  коллектор для count_distinct_reducer
def map_reducer(in_put, mapper, reducer):
    like_map = mapper(in_put)
    num_user_like = reducer(like_map)
    liker_reduce = defaultdict(int)
    for user in count_distinct_reducer(like_map):
        for other_user in like_map:
            if user != other_user:  # условие исключающее учёт собственного лайка данного пользователя
                if set(like_map[user].keys()).issubset(set(like_map[other_user].keys()))\
                        or set(like_map[user].keys()).issuperset(set(like_map[other_user].keys())):  # учёт лайков users
                    liker_reduce[user] += 1
                else:
                    liker_reduce[user] += 0


    yield liker_reduce


distinct_licers_per_user = map_reducer(status_update, liker_mapper, count_distinct_reducer)
print(list(distinct_licers_per_user), "Число пльзователей лайкнувших данного пользователя")

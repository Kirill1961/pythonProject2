import numpy as np
import math as mt
from collections import defaultdict, Counter

users_interests = [['MongoDB', 'data science', 'Spark', 'Postgres', 'pandas', 'NoSQL''Big Data'],
                   ['Storm', 'Java', 'pandas', 'MongoDB', 'data science', 'pandas', 'data science'],
                   ['C++', 'Scikit-learn', 'regression', 'neural network', 'MongoDB', 'Big Data', 'data science',
                    'NoSQL Big Data'],
                   ['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science'],
                   ['Storm', 'regression', 'neural network', 'MongoDB', 'Big Data', 'data science', 'NoSQL Big Data'],
                   ['C++', 'Scikit-learn', 'regression', 'neural network', 'Big Data', 'pandas'],
                   ['Scikit-learn', 'regression', 'neural network', 'MongoDB', 'Big Data', 'data science',
                    'NoSQL Big Data'],
                   ['statistic', 'R', 'go', 'scipy', 'numpy', 'data science', 'pandas', 'NoSQL''Big Data'],
                   ['Python', 'Hadoop', 'numpy', 'NoSQL', 'MongoDB', 'HBase', 'data science', 'NoSQL''Big Data'],
                   ['Cassandra', 'machine learning', 'Haskel', 'C++', 'scipy', 'data science', 'NoSQL Big Data'],
                   ['Python', 'Hadoop', 'numpy', 'NoSQL Big Data', 'pandas', 'NoSQL Big Data'],
                   ['statistic', 'Java', 'pandas', 'MongoDB', 'data science'],
                   ['numpy', 'decision trees', 'libsvm', 'MongoDB', 'probability'],
                   ['statistic', 'R', 'go', 'scipy', 'numpy', 'machine learning', 'data science', 'NoSQL Big Data'],
                   ['Python', 'Hadoop', 'numpy', 'data science', 'MongoDB', 'NoSQL''Big Data'],
                   ['HBase', 'Storm', 'Java', 'pandas'],
                   ['statistic', 'R', 'go', 'scipy', 'C++', 'MongoDB', 'pandas', 'data science', 'NoSQL Big Data'],
                   ['Spark', 'Postgres', 'Cassandra', 'machine learning', 'Haskel', 'pandas'],
                   ['statistic', 'R', 'go', 'scipy', 'HBase', 'pandas', 'data science'],
                   ['Python', 'Hadoop', 'numpy', 'NoSQL', 'HBase', 'NoSQL Big Data'],

                   ]

# users_interests = [['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science'],
#                    ['MongoDB', 'data science', 'Spark', 'Postgres', 'pandas', 'NoSQL''Big Data'],
#                    ['Storm', 'Java', 'pandas', 'MongoDB', 'data science', 'pandas', 'data science'],
#                    ['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science']
#                    ]


# TODO start filter user

# Подобие векторов - Измерение cos между векторами интересов
def cosine_similarity(v, w):
    return np.dot(v, w) / mt.sqrt((np.dot(v, v)) * np.dot(w, w))  # коэффициент подобия


unique_interests = sorted(list({interest for user_interests in users_interests for interest in user_interests}))


# вектор интересов: вектор интересов юзера и вектор интересов unique_interests при совпадении 1 else 0
def make_user_interest_vector(user_interests):
    return [1 if interest in user_interests else 0 for interest in unique_interests]  # вектор интересов


# Матрица совпадений unique_interests с интересами юзеров, 1 - совпадает / 0 - несовпадает
# строки матрицы по числу юзеров, столбцы unique_interests
user_interest_matrix = map(make_user_interest_vector, users_interests)  # матрица


# Попарный перебор векторов интересов для измерения cos, cos=1 сонаправлены, cos=0 разнонаправлены
# i - й пользователь сравнивается по интересам со всеми j - ми пользователями
user_similarities = [[cosine_similarity(interest_vector_i, interest_vector_j)
                      for interest_vector_i in user_interest_matrix]
                     for interest_vector_j in user_interest_matrix]
# print(user_similarities, "user_similarities")


# TODO mid filter user
# most_similar_users_to - создаём кортежи (юзер, подобие юзера с текущим) текущий user не отсеивается
def most_similar_users_to(user_id):
    # Другие юзеры со своими подобиями
    pairs = [(other_user_id, similaraty) for other_user_id, similaraty in enumerate(user_similarities[0])
             if user_id != other_user_id and similaraty > 0]  # отсев текущего юзера и подобия = 0
    return sorted(pairs, key=lambda similaraty: similaraty, reverse=True)


#  Рекомендации для данного пользователя
def user_based_suggetions(user_id, include_current_interests=False):
    suggetions = defaultdict(float)
    for other_user_id, similarity in most_similar_users_to(user_id):  # вытаскиваем id друга + подобие
        for interest in users_interests[other_user_id]:  # вытаскиваем интересы друзей
            suggetions[interest] += similarity  # пишем интересы друзей в key словаря : value - сумма подобий
    suggetions = sorted(suggetions.items(), key=lambda i: i[1], reverse=True)  # сортировка по подобию, [1]index кортежа
    # suggetions = sorted(suggetions.values(), reverse=True)  # Коэффициенты подобия для юзера user_id


    if include_current_interests:
        return suggetions
    else:
        return [(suggetion, wight)
                for suggetion, wight in suggetions if suggetion not in users_interests[user_id]], \
               f"Рекомендация для юзера - {user_id}"


print(user_based_suggetions(1))

# TODO end filter user












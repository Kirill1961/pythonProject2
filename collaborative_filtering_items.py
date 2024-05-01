import numpy as np
import math as mt
from collections import defaultdict, Counter

# users_interests = [['MongoDB', 'data science', 'Spark', 'Postgres', 'pandas', 'NoSQL''Big Data'],
#                    ['Storm', 'Java', 'pandas', 'MongoDB', 'data science', 'pandas', 'data science'],
#                    ['C++', 'Scikit-learn', 'regression', 'neural network', 'MongoDB', 'Big Data', 'data science',
#                     'NoSQL Big Data'],
#                    ['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science'],
#                    ['Storm', 'regression', 'neural network', 'MongoDB', 'Big Data', 'data science', 'NoSQL Big Data'],
#                    ['C++', 'Scikit-learn', 'regression', 'neural network', 'Big Data', 'pandas'],
#                    ['Scikit-learn', 'regression', 'neural network', 'MongoDB', 'Big Data', 'data science',
#                     'NoSQL Big Data'],
#                    ['statistic', 'R', 'go', 'scipy', 'numpy', 'data science', 'pandas', 'NoSQL''Big Data'],
#                    ['Python', 'Hadoop', 'numpy', 'NoSQL', 'MongoDB', 'HBase', 'data science', 'NoSQL''Big Data'],
#                    ['Cassandra', 'machine learning', 'Haskel', 'C++', 'scipy', 'data science', 'NoSQL Big Data'],
#                    ['Python', 'Hadoop', 'numpy', 'NoSQL Big Data', 'pandas', 'NoSQL Big Data'],
#                    ['statistic', 'Java', 'pandas', 'MongoDB', 'data science'],
#                    ['numpy', 'decision trees', 'libsvm', 'MongoDB', 'probability'],
#                    ['statistic', 'R', 'go', 'scipy', 'numpy', 'machine learning', 'data science', 'NoSQL Big Data'],
#                    ['Python', 'Hadoop', 'numpy', 'data science', 'MongoDB', 'NoSQL''Big Data'],
#                    ['HBase', 'Storm', 'Java', 'pandas'],
#                    ['statistic', 'R', 'go', 'scipy', 'C++', 'MongoDB', 'pandas', 'data science', 'NoSQL Big Data'],
#                    ['Spark', 'Postgres', 'Cassandra', 'machine learning', 'Haskel', 'pandas'],
#                    ['statistic', 'R', 'go', 'scipy', 'HBase', 'pandas', 'data science'],
#                    ['Python', 'Hadoop', 'numpy', 'NoSQL', 'HBase', 'NoSQL Big Data'],
#
#                    ]
users_interests = [['Java', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science'],
                   ['MongoDB', 'data science', 'Spark', 'Postgres', 'pandas', 'NoSQL''Big Data'],
                   ['Storm', 'Java', 'pandas', 'MongoDB', 'data science', 'pandas', 'data science'],
                   ['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science']
                   ]


# Подобие векторов - Измерение cos между векторами интересов
def cosine_similarity(v, w):
    # print(v, w)
    return np.dot(v, w) / mt.sqrt((np.dot(v, v)) * np.dot(w, w))  # коэффициент подобия


unique_interests = sorted(list({interest for user_interests in users_interests for interest in user_interests}))
print(unique_interests)


# вектор интересов: вектор интересов юзера и вектор интересов unique_interests при совпадении 1 else 0
def make_user_interest_vector(user_interests):
    itrs = (list(1 if interest in user_interests else 0 for interest in unique_interests), "вектор интересов")
    # print(itrs)
    return [1 if interest in user_interests else 0 for interest in unique_interests]  # вектор интересов


# Матрица совпадений unique_interests с интересами юзеров, 1 - совпадает / 0 - несовпадает
user_interest_matrix = [i for i in map(make_user_interest_vector, users_interests)]  # матрица, строка - кол-во юзеров

# user_interest_matrix  - Матрица совпадений unique_interests с интересами юзеров, 1-да, 0-нет
# for loop вектора юзеров и индексируем [j] unique_interests, j - индекс темы в вектор подобия текущего юзера
# строки матрицы по числу unique_interests, столбцы юзеры
interest_user_matrix = [[user_interest_vector[j] for user_interest_vector in user_interest_matrix]
                        for j, _ in enumerate(unique_interests)]

print(interest_user_matrix)

# Попарный перебор векторов интересов для измерения cos, cos=1 сонаправлены, cos=0 разнонаправлены
interest_similarites = [[cosine_similarity(user_vector_i, user_vector_j)
                         for user_vector_i in interest_user_matrix]
                        for user_vector_j in interest_user_matrix]


def most_similar_users_to(interest_id):
    similarities = interest_similarites[interest_id]
    pairs = [(unique_interests[other_interest_id], similaraty)
             for other_interest_id, similaraty in enumerate(similarities)
             if interest_id != other_interest_id and similaraty > 0]  # отсев текущего юзера и подобия = 0
    return sorted(pairs, key=lambda similaraty: similaraty, reverse=True)


def item_based_suggetions(user_id, include_current_interests=False):
    suggetions = defaultdict(float)
    user_interest_vector = user_interest_matrix[user_id]
    for interest_id, is_interested in enumerate(user_interest_vector):
        if is_interested == 1:
            simmilar_interests = most_similar_users_to(interest_id)
            for interest, similarity in simmilar_interests:
                # print(interest, similarity, ">>>>>>")
                suggetions[interest] += similarity
                # print(suggetions.items())
    suggetions = sorted(suggetions.items(), key=lambda i: i[1], reverse=True)
    if include_current_interests:
        return suggetions
    else:
        return [(suggetion, weight)
                for suggetion, weight in suggetions if suggetion not in users_interests[user_id]], \
               f"item_based_suggetions for user_id - {user_id}"


print(item_based_suggetions(0))

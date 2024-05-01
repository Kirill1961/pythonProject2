import random
from collections import Counter

# этот documents отображён в виде обработанного текста после tokenizer, до обработки это единый list со строчным ОБ
documents = [['MongoDB', 'data science', 'Spark', 'Postgres', 'pandas', 'NoSQL''Big Data'],
             ['Storm', 'Java', 'pandas', 'MongoDB', 'data science', 'pandas', 'data science'],
             ['C++', 'Scikit-learn', 'regression', 'neural network', 'MongoDB', 'Big Data', 'data science', 'NoSQL Big Data'],
             ['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science'],
             ['Storm', 'regression', 'neural network', 'MongoDB', 'Big Data', 'data science', 'NoSQL Big Data'],
             ['C++', 'Scikit-learn', 'regression', 'neural network', 'Big Data', 'pandas'],
             ['Scikit-learn', 'regression', 'neural network', 'MongoDB', 'Big Data', 'data science', 'NoSQL Big Data'],
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
             ['Python', 'Hadoop', 'numpy', 'NoSQL', 'HBase', 'NoSQL Big Data']]
# TODO documents
# documents = [
#     ['MongoDB', 'data science', 'Spark'],
#     ['Storm', 'Java', 'pandas', 'MongoDB'],
#     ['Java', 'Scikit-learn', 'data science', 'neural network'],
#     ['Scikit-learn', 'data science', 'Spark'],
#     ['Spark', 'Postgres']
# ]

# documents = [
#     ['Spark', 'Spark', 'Spark'],
#     ['Storm', 'Java', 'pandas', 'MongoDB', 'data science'],
#     ['Java', 'Spark', 'data science', 'Spark', 'MongoDB', 'Spark'],
#     ['Scikit-learn', 'data science', 'Spark'],
#     ['Spark', 'Postgres', 'Cassandra', 'Spark', 'Haskel', 'pandas']
# ]


def sample_from(weights):
    # print(weights, "weights")
    total = sum(weights)
    rnd = total * random.random()
    for i, w in enumerate(weights):
        rnd -= w
        if rnd <= 0: return i


# print(sample_from([1, 1, 3]), "sample_from")

K = 4

"""Сохраним в переменные функционал"""
document_topic_counts = [Counter() for _ in documents]  # список пустых ОБ Counter, для вывода распределения topic|doc
# print(document_topic_counts, "document_topic_counts")

topic_word_counts = [Counter() for _ in range(K)]  # список пустых ОБ Counter, для вывода распределения W|topic
# print(topic_word_counts, "topic_word_counts")

topic_counts = [0 for _ in range(K)]  # суммарное число слов назначенное каждой теме
# print(topic_counts, "topic_counts")

documents_lenghts = list(map(len, documents))
# print(list(documents_lenghts), "documents_lenghts")

distinct_word = set(word for document in documents for word in document)
W = len(distinct_word)
# print(list(distinct_word), "distinct_word", "\n")

D = len(documents)


# TODO probability
def p_topic_given_document(topic, d, alpha=0.1):  # P (t | d)
   t =((document_topic_counts[d][topic] + alpha) / (documents_lenghts[d] + K * alpha))

   # if t > 0.5: print(topic, t)
   return ((document_topic_counts[d][topic] + alpha) /
            (documents_lenghts[d] + K * alpha))


def p_word_given_topic(word, topic, beta=0.1):
    return ((topic_word_counts[topic][word] + beta) /
            (topic_counts[topic] + W * beta))


random.seed(0)  # seed - фиксируем случайные назначения тематик в документах по кол-ву W
document_topics = [[random.randrange(K) for word in document] for document in documents]






print(document_topics, "вытаскиваем W из doc's и вместо W ставим № темы, assignment topic for word")
# print("doc", "t|d", "w|t", "numW|t in doc", "        topic")
# TODO topic
for d in range(D):  # индекс для extract doc из doc's
    for word, topic in zip(documents[d], document_topics[d]):  # Назначение каждому W - тематики
        document_topic_counts[d][topic] += 1  # список объектов Counter один для каждого doc, суммируются тематики
        # в док-х, сколько раз тема назначается данному док-ту, D (topic|doc), key-[topic]: val- += 1 кол-во

        topic_word_counts[topic][word] += 1  # список объектов Counter один для каждой темы, суммируются слова в темах,
        # сколько раз слово назначается данной тематике, D (W | topic), key-[word] , value-topic

        topic_counts[topic] += 1  # суммарное число слов назначенное каждой теме, список чисел один д/каждой темы

        # print(d, " ", document_topic_counts[d][topic], "  ", end=" ")  # распределение topic|doc
        # print(topic_word_counts[topic][word], "  ", end=" ")  # распределение W|topic
        # print(topic_counts[topic], "слова  ", end=" ")  # суммарное число слов назначенное каждой теме
        # print("  в теме - ", topic, word)

        # print("\t" * 4, p_word_given_topic(word, topic, beta=0.1))
        # print("\t" * 4, p_topic_given_document(topic, d, alpha=0.1))
# TODO weights
def topic_weight(d, word, k):
    return p_topic_given_document(word, k) * p_topic_given_document(k, d)


def choose_new_topic(d, word):
   return sample_from([topic_weight(d, word, k) for k in range(K)])


for iter in range(1000):
    for d in range(D):
        for i, (word, topic) in enumerate(zip(documents[d], document_topics[d])):
            # print(i, (word, topic))
            document_topic_counts[d][topic] -= 1
            topic_word_counts[topic][word] -= 1
            topic_counts[topic] -= 1
            documents_lenghts[d] -= 1

            new_topic = choose_new_topic(d, word)
            document_topics[d][i] = new_topic

            document_topic_counts[d][new_topic] += 1
            topic_word_counts[new_topic][word] += 1
            topic_counts[new_topic] += 1
            documents_lenghts[d] += 1
# TODO end
print(" тема, слово, count")
for k, word_counts in enumerate(topic_word_counts):
    for word, count in word_counts.most_common():
        if count > 0: print(k, "  ", word, "  ",count)

topic_names = ["statistic", "data base", "NLP", "Big Data"]


for document, topic_counts in zip(documents, document_topic_counts):
    # print(document)
    for topic, count in topic_counts.most_common():
        if count > 0:
            pass
            # print(topic, count, " >>>>>>>>>>>>")
            print((topic_names[topic], count))
    print()

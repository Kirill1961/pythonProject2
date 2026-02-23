from gensim import corpora
from gensim.models import LdaModel
from gensim.utils import simple_preprocess
import random

# TODO 1
# Предположим, у вас есть некоторые текстовые данные
# data = [
#     ["apple", "banana", "banana", "lemon"],
#     ["apple", "banana", "peach"],
#     ["apple", "banana", "banana", "peach"],
#     ["lemon", "orange", "lemon", "lemon"],
# ]

# TODO 2
data_raw = [
    "кот любит молоко",
    "собака любит кость",
    "кот и собака друзья"
]

# TODO Tokenizer
# 1️⃣👎
# data = list(map(lambda x: x.split(' '), data_raw))
# 2️⃣👆
# data = [doc.split(" ") for doc in data_raw]
# 3️⃣🚀
data = [simple_preprocess(doc) for doc in data_raw]


#  TODO 3
d = [
    ["MongoDB", "data science", "Spark", "Postgres", "pandas", "NoSQL" "Big Data"],
    ["Storm", "Java", "pandas", "MongoDB", "data science", "pandas", "data science"],
    [
        "C++",
        "Scikit-learn",
        "regression",
        "neural network",
        "MongoDB",
        "Big Data",
        "data science",
        "NoSQL Big Data",
    ],
    ["statistic", "R", "go", "scipy", "numpy", "MongoDB", "pandas", "data science"],
    [
        "Storm",
        "regression",
        "neural network",
        "MongoDB",
        "Big Data",
        "data science",
        "NoSQL Big Data",
    ],
    ["C++", "Scikit-learn", "regression", "neural network", "Big Data", "pandas"],
    [
        "Scikit-learn",
        "regression",
        "neural network",
        "MongoDB",
        "Big Data",
        "data science",
        "NoSQL Big Data",
    ],
    [
        "statistic",
        "R",
        "go",
        "scipy",
        "numpy",
        "data science",
        "pandas",
        "NoSQL" "Big Data",
    ],
    [
        "Python",
        "Hadoop",
        "numpy",
        "NoSQL",
        "MongoDB",
        "HBase",
        "data science",
        "NoSQL" "Big Data",
    ],
    [
        "Cassandra",
        "machine learning",
        "Haskel",
        "C++",
        "scipy",
        "data science",
        "NoSQL Big Data",
    ],
    ["Python", "Hadoop", "numpy", "NoSQL Big Data", "pandas", "NoSQL Big Data"],
    ["statistic", "Java", "pandas", "MongoDB", "data science"],
    ["numpy", "decision trees", "libsvm", "MongoDB", "probability"],
    [
        "statistic",
        "R",
        "go",
        "scipy",
        "numpy",
        "machine learning",
        "data science",
        "NoSQL Big Data",
    ],
    ["Python", "Hadoop", "numpy", "data science", "MongoDB", "NoSQL" "Big Data"],
    ["HBase", "Storm", "Java", "pandas"],
    [
        "statistic",
        "R",
        "go",
        "scipy",
        "C++",
        "MongoDB",
        "pandas",
        "data science",
        "NoSQL Big Data",
    ],
    ["Spark", "Postgres", "Cassandra", "machine learning", "Haskel", "pandas"],
    ["statistic", "R", "go", "scipy", "HBase", "pandas", "data science"],
    ["Python", "Hadoop", "numpy", "NoSQL", "HBase", "NoSQL Big Data"],
]

# TODO 4
# data_raw = [
#     [
#         "Human machine interface for lab abc computer applications",
#         "A survey of user opinion of computer system response time",
#         "The EPS user interface management system",
#         "System and human system engineering testing of EPS",
#         "Relation of user perceived response time to error measurement",
#         "The generation of random binary unordered trees",
#         "The intersection graph of paths in trees",
#         "Graph minors IV Widths of trees and well quasi ordering",
#         "Graph minors A survey",
#     ]
# ]

# TODO split - Делим слова по пробелам,
#  Создаём документы с разделёными словами
# data = [doc.split(" ") for doc in data_raw[0]]
# print('Docums+terms :\n', data)

# TODO Создание словаря, пять уникальных слов ,
#  Dictionary<5 unique tokens: ['apple', 'banana', 'lemon', 'peach', 'orange']>
dictionary = corpora.Dictionary(data)  # преобразует unique tokens в id (индексы)
print("Dictionary :\n", dictionary, "\n")

# TODO doc2bow все слова преобразует в bag-of-words, (id, frequents)
corpus = [dictionary.doc2bow(text) for text in data]
print("corpus из уникальных слов \n "
      "( idx_term x frequents_term ): \n" , corpus, "\n")

# Обучение модели LDA
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=3)
print("lda_model :\n", lda_model, "\n")

print("lda_model.print_topics : \n ", lda_model.print_topics(), "\n")


# TODO 🚩 Сэмплирование по Variational Bayes 👉 это происходит подкапотом LdaModel
#  концептуально соответствует одному микрошагу, который модель делает во время обучения
# doc = corpus[0]
for idx, _ in enumerate(corpus):
    doc = corpus[idx]
    topic_probabilities = lda_model.get_document_topics(doc, minimum_probability=0.01)
    print(f"Вероятность topics в document № {idx} :\n", topic_probabilities, "\n")

topic_distribution = [probability for _, probability in topic_probabilities]
print("topic_distribution : \n", topic_distribution, "\n")

# TODO Выбор новой темы с учетом текущего распределения тем
new_topic = random.choices(range(lda_model.num_topics), weights=topic_distribution)
print("new_topic : \n", new_topic, "\n")
print("New topic for the document: \n", new_topic, "\n")

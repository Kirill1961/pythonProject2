from gensim import corpora
from gensim.models import LdaModel

# Предположим, у вас есть некоторые текстовые данные
data = [['apple', 'banana', 'banana', 'lemon'],
        ['apple', 'banana', 'peach'],
        ['apple', 'banana', 'banana', 'peach'],
        ['lemon', 'orange', 'lemon', 'lemon']
        ]


d = [['MongoDB', 'data science', 'Spark', 'Postgres', 'pandas', 'NoSQL''Big Data'],
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
             ['Python', 'Hadoop', 'numpy', 'NoSQL', 'HBase', 'NoSQL Big Data'],

        ]
# Создание словаря, пять уникальных слов ,
# Dictionary<5 unique tokens: ['apple', 'banana', 'lemon', 'peach', 'orange']>
dictionary = corpora.Dictionary(data)  # преобразует unique tokens в id (индексы)
print(dictionary, "dictionary")
corpus = [dictionary.doc2bow(text) for text in data]    # doc2bow все слова преобр. в bag-of-words, (id, frequents)
print(corpus, "corpus")
# Обучение модели LDA
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=2)
print(lda_model, "lda_model")
# Сэмплирование по Гиббсу
# Предположим, что мы хотим сгенерировать новую тему для первого документа
doc = corpus[0]
topic_probabilities = lda_model.get_document_topics(doc)
print(topic_probabilities)
topic_distribution = [probability for _, probability in topic_probabilities]
print(topic_distribution)
# Выбор новой темы с учетом текущего распределения тем
import random
new_topic = random.choices(range(lda_model.num_topics), weights=topic_distribution)[0]
print(new_topic, "new_topic")
print("New topic for the document:", new_topic)

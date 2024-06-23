
from functools import reduce
from collections import defaultdict, Counter
import random as rn
import pprint
import glob, re

# # Сгенерировать список слов
set_for_train = " asdf rtyu rtyu poiu poiu poiu poiu poiu asdf asdddd"  #
for_classifier_message = " asdf poiu poiu dfghrtyu rtyu asdfpoiu asdf asdf qwert rewq asdf asdddd asdddd asdddd asdddd "

# input_value = [['a', 'b', 'c', 'w', 's'], ['d', 'b', 'k'], ['a', 'c', 'k'], ['a', 'd', 'f']]


input_value = [['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science'],
               ['MongoDB', 'data science', 'Spark', 'Postgres', 'pandas', 'NoSQL','Big Data'],
               ['Storm', 'Java', 'pandas', 'MongoDB', 'data science', 'pandas', 'data science'],
               ['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science']
               ]


# Токенайзер для стандартного подсчёта слов
def tokenize(messages):
    global all_words
    # for message in [j for i in messages for j in i]:  # для букв
    for message in messages:  # для слов
        message = message.lower()
        all_words = re.findall("[a-z0-9']+", message)
        # print(all_words)
        yield tuple(all_words)






# стандартный подсчёт частоты слов с Counter
def word_count(documents):
    return Counter([word for document in documents for word in tokenize(document)])


#  каждому ОБ присваиваем 1 - одно вхождение, для последующего поподсчёта
def wc_mapper(document):
    # print(document)
    for word in tokenize(document):
        # print(word, 1, "||||||||||||||||||||")
        yield word, 1


# Функция свёртки

# def wc_reducer(word_counts):
#     for word, counts in word_counts:
#         yield word[0]


# t = Counter(list(wc_reducer(wc_mapper(input_value))))
# print(t)

def wc_reducer(word, counts):
    # print(word, counts)
    yield word[0], counts


# Моя дописка Варианта подсчёта с использованием wc_reducer и wc_mapper
def words_count(documents):
    collector = defaultdict(list)
    for document in documents:
        for word, counts in wc_reducer(document):
            collector[word].append(counts)  # Собираем в словаре collector - same keys

    yield collector


# print(list(words_count(input_value)))

#  Мои исполнительные агрегирующие ф-ции: mapp=wc_mapper и rdsr=wc_reducer
mapp = lambda x: [(i, j) for i in x for j in [x.index(i)]]  # для просто LIST
rdsr = lambda y, x: (y, Counter(x))


def map_reduce(inputs, mapper, reducer):  # mapper / reducer - выбранные / с суммированные слова
    collector = defaultdict(list)
    for input in inputs:
        for key, value in mapper(input):
            collector[key].append(value)
    # print([(key, sum(values)) for key, values in collector.items()])
    return [output for key, values in collector.items()
            for output in reducer(key, values)]


# pprint.pprint(map_reduce(input_value, mapp, rdsr))
pprint.pprint(map_reduce(input_value, wc_mapper, wc_reducer))


# Преобразование key и values в key и выход
def partial(reduce_val_using, aggregation_fn):
    for k, v in map_reduce(input_value, wc_mapper, wc_reducer):
        yield reduce_val_using(aggregation_fn, k, v)


# Свёртка значений, key и values закидываем из partial
def reduce_values_using(aggregation_fn, key, values):
    return key, aggregation_fn(values)


# Фу-ция свёртки, в аргументе вид агрегации
def values_reducer(aggregation_fn):
    # for k, v in map_reduce(input_value, wc_mapper, wc_reducer):
    # a = reduce_values_using(aggregation_fn, "key", [1, 1])
    return partial(reduce_values_using, aggregation_fn)
    # yield reduce_values_using(aggregation_fn, k, v)


# Редуктора с разными видами агрегации
sum_reducer = values_reducer(sum)
# max_reducer = values_reducer(max)
# min_reducer = values_reducer(min)
count_distinc_redeucer = values_reducer(lambda values: len((values)))
print(list(sum_reducer), "sum_reducer")
print(list(count_distinc_redeucer), "count_distinc_redeucer ")



def tokenize_word(words):
    for word in words:
        word_pattern = r'\b(?:' + '|'.join(word) + r')\b'
        print(word_pattern, "word_pattern")
tokenize_word(input_value)



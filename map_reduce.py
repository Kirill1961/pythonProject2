from functools import reduce
from collections import defaultdict, Counter
import random as rn
import pprint
# input_value = [['a', 'b', 'c', 'w', 's'], ['d', 'b', 'k'], ['a', 'c', 'k'], ['a', 'd', 'f']]
input_value = [['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science'],
               ['MongoDB', 'data science', 'Spark', 'Postgres', 'pandas', 'NoSQL''Big Data'],
               ['Storm', 'Java', 'pandas', 'MongoDB', 'data science', 'pandas', 'data science'],
               ['statistic', 'R', 'go', 'scipy', 'numpy', 'MongoDB', 'pandas', 'data science']
               ]
# print([j for i in input_value for j in [input_value.index(i)]])
# mapp = lambda x: [(j, i) for i in x for j in [rn.randint(1, 10)]]

# TODO Раздали индексы словам во вложенных списках
#  Функция mapp группирует, сортирует и фильтрует несколько наборов данных.
mapp = lambda x: [(j, i) for i in x for j in [x.index(i)]]  # x - это вложенные списки из input_value
# mapp = list(map(lambda x: [(j, i) for i in x for j in [x.index(i)]], input_value))  # для LIST[LIST]
print(mapp)

# TODO rdsr(Reduce) агрегирует данные для получения желаемого результата.
rdsr = lambda y, x: (y, Counter(x))


def map_reduce(inputs, mapper, reducer):
    print(rdsr)
    collector = defaultdict(list)
    n = 0
    for input in inputs:
        # print(input)
        for key, value in mapper(input):  # mapper - это ф-ция lambda
            # print(key, value)
            collector[key].append(value)  # Создание словаря
            # print(collector)
    return [output for key, values in collector.items()
            for output in reducer(key, values)]


# map_reduce(input_value, mapp, rdsr)
pprint.pprint(map_reduce(input_value, mapp, rdsr))

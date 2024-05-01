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
mapp = lambda x: [(j, i) for i in x for j in [x.index(i)]]  # для просто LIST
# mapp = list(map(lambda x: [(j, i) for i in x for j in [x.index(i)]], input_value))  # для LIST[LIST]
print(mapp)

rdsr = lambda y, x: (y, Counter(x))


def map_reduce(inputs, mapper, reducer):
    print(rdsr)
    collector = defaultdict(list)
    for input in inputs:
        # print(input)
        for key, value in mapper(input):
            # print(key, value)
            collector[key].append(value)
            # print(collector)
    return [output for key, values in collector.items()
            for output in reducer(key, values)]


pprint.pprint(map_reduce(input_value, mapp, rdsr))

import random
from turtle import distance
from collections import  Counter


""" split_data() делит данные (х,у) на обучающую и тестовую выборку,
   --> соединили в кортежи Х и У, получили data(x,y), которые передали в split_data() для
      разбивки на выборки train и test в заданном соотношении test/test_pct и train/1 - test_pct ,
        затем разъединяем с помощью распаковщика zip(* arg)"""

def split_data(data, prob): # prob  число определяющее долю данных для обучения, для теста останется 1 - prob данных
    results = [], [] # results - кортеж из пустых списков
    for row in data:
        results[0 if random.random() < prob else 1].append(row)# индексы кортежа results для заполнения 2х списков data

    return results
# print(split_data([1,0.5,0.8,1.2, 0.13], 0.2), ' split_data')


#  разбивка на обучающую и контрольную выборку

def train_test_split(x, y, test_pct):    # test_pct - процент данных для test
    data = zip(x, y)    # соеденяем в кортеж (x, y) для split_data()
    train, test = split_data(data, 1 - test_pct)     # "1 - test_pct" - кол-во данных для обучения
    print(train, 'тренировочная выборка',test, ' тестовая выборка соответствует заданному % test_pct')
    x_train, y_train = zip(*train)   # в аргументе zip распаковщик " * ", это разъеденение кортежей
    x_test, y_test = zip(*test)     # если в аргументе " * " - zip совершает обратное действие-разъеденяет кортежи
    print(x_train,' x_train', x_test, ' x_test')
    print(y_train, 'y_train',y_test, '  y_test')
    return x_train, x_test, y_train, y_test
train_test_split([2,4,7,8,9], [22,44,77, 88, 99], 0.3)
# print(train_test_split([2,4,7,8,9], [22,44,77, 88, 99], 0.3), ' train_test_split')



# model = SomeKindOfModel ()
# x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.33)
# model.train(x_train, y_train)
# performance = model.test(x_test, y_test)

"""  K-Nearest Neighbors """

def raw_major__vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    print(winner, votes)
    return winner
raw_major__vote(['d','a', 'c','b', 'c', 'a', 'a'])




import math
import glob, re
from collections import defaultdict, Counter
import random
import numpy as np

# # Сгенерировать список слов
set_for_train = " asdf rtyu rtyu poiu poiu poiu poiu poiu asdf asdddd" #
for_classifier_message = " asdf poiu poiu dfghrtyu rtyu asdfpoiu asdf asdf qwert rewq asdf asdddd asdddd asdddd asdddd "

def tokenize(message):
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)
# print(tokenize("asdddd asdf rtyu rtyu poiu poiu"), " tokenize")



# # Входящие строчные делим по пробелу и рандомно маркеруем 0 - спам, 1 - неспам
def labels_for_words(words_for_count):
    # print(words_for_count, " words_for_count")
    words = words_for_count.split(" ")
    w = random.choice([1, 0])
    return  [x_mes for x_mes in zip([x for x in words ], [random.choice([1, 0]) for _ in range(len(words))])]

# print(train_label_message(str))


# # tokenize - Считаем частотность слов
def count_words(training_set):   # # training_set - это train_data
    counts = defaultdict(lambda:[0, 0])  # # из тела lambda в словарь counts  передаём value [0, 0]
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts [word][0 if is_spam else  1] += 1  # # если is_spam == True или False то +1 к value[0} или value[1}
    # print("\t" * 4,counts, " counts counts counts")# [word] - ключ,[0 if is_spam else  1] - индекс
    return counts
print(" ")
# count_words(train_label_message(" asdf rtyu rtyu poiu poiu poiu poiu poiu asdddd"))



# # Этот блок исключён тк его вычисление в вызове words_probablities()
# def spam_nonspam_for_probablities(counts):
#     x_total_spam = sum([x for x,_ in [s for s in counts.values()]])
#     y_non_total_spam = sum([y for _, y in [s for s in counts.values()]])
#     # print(x_total_spam, y_non_total_spam, " total_spam, non_total_spam")
#     return (x_total_spam, y_non_total_spam)

# (spam_nonspam_for_probablities(count_words(labels_for_words
#                                                     (" asdf rtyu rtyu poiu poiu poiu poiu poiu asdddd"))))




def words_probablities(counts, total_spam, total_non_spam, k = 0.5):
    # print(counts.items(), " словарь из токенайзера {word : [spam, non_spam]}")
    # total_spam, total_non_spam = spam_nonspam_for_probablities(count_words(labels_for_words
    #                                                 (for_classifier_message)))
    # print([(w, (spam + k) / (total_spam + 2 * k), (non_spam + k) / (total_non_spam + 2 * k))
    #         for w, (spam, non_spam) in counts.items()], " words_probablities spam, non_spam" )
    # print([(k,v) for k,v in counts.values()], " spam, non_spammmmmmmmmmmmmmmmmmmmm")
    # print("\t" * 3, spam, non_spam, " <<<< >>>>", total_spam, total_non_spam )
    return [(w, (spam + k) / (total_spam + 2 * k), (non_spam + k) / (total_non_spam + 2 * k))
            for w, (spam, non_spam) in counts.items()]  # # возвращаем список кортежей слово с вероятностями спам/неспам


# print(words_probablities(count_words(train_label_message(train_set)),
#                          sum([x for x,_ in [s for s in count_words(train_label_message(train_set)).values()]]),
#                          sum([y for _, y in [s for s in count_words(train_label_message(train_set)).values()]])),
#                             " вероятность появления слова в спам / неспам")

print(" ")

# log_probability , log-вероятность
def spam_probability(word_probs, message): # # word_probs - результат обучения, message - это test_data
    message_words = tokenize(message)
    # print(message_words,  "TOKENIZEEEEEEEEEEEEEEEEEEEEEEEEEE")

    log_prob_if_spam = log_prob_if_not_spam = 0.0  # #log - понимаем как регистрация или запись
    for word, prob_if_spam, prob_if_not_spam in word_probs:
        # print("\t" * 4,word, prob_if_spam, prob_if_not_spam, " word_probs 1 ")
        if word in message_words:  # # если из test_data слово в сообщении то логируем его в переменную
            # print(word,prob_if_spam, prob_if_not_spam, " word_probs 2 ")
            log_prob_if_spam += math.log(prob_if_spam) # # log_proba берём из словаря где key-слово,value-[спам, неспам]
            log_prob_if_not_spam += math.log (prob_if_not_spam)  # # log-вероятности суммируем в переменную в log-форме
        else:
            log_prob_if_spam += math.log(1 - prob_if_spam)  # # если из tokenize слова нет в сообщении
            log_prob_if_not_spam += math.log(1 - prob_if_not_spam) # # то уменьшаем переменную

        # print(log_prob_if_spam, " spam", log_prob_if_not_spam, " not_spam")

    prob_if_spam = math.exp(log_prob_if_spam)  # # math.exp() перевод из log-вероятности обратно в вероятность в %
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    # print(prob_if_spam / (prob_if_spam + prob_if_not_spam), " prob_if_spam / (prob_if_spam + prob_if_not_spam")
    return prob_if_spam / (prob_if_spam + prob_if_not_spam) # # вероятность появления слова в спаме p = n / m

# spam_probability(words_probablities(count_words(labels_for_words(set_for_train)),  # set_for_train тренинговая выборка
#     sum([x for x,_ in [s for s in count_words(labels_for_words(set_for_train)).values()]]),
#     sum([y for _, y in [s for s in count_words(labels_for_words(set_for_train)).values()]])), for_classifier_message)


class NaiveBayesClassifier:
    def __init__(self, k=0.5):

        self.k = k
        self.word_probs = [] # # Список заполняется кортежами из words_probablities

    def train (self, training_set): # # training_set - это train_data
        # print(training_set, " training_setttttt")

        num_spams = len([is_spam for message, is_spam in training_set if is_spam])# # кол-во слов из спама
        num_non_spams = len(training_set) - num_spams # # кол-во слов из неспама

        word_counts = count_words(training_set)  # # словарь {word : [spam, non_spam]]
        # print(word_counts, " Токенайзер p p p p p p p p p p p p p p p p p ")
        # print(num_spams, num_non_spams, " num_spams, num_non_spamsssssssssssssssss")
        self.word_probs = words_probablities(word_counts, num_spams, num_non_spams, self.k)
        # self.word_probs = words_probablities(word_counts, self.k)
        # print(self.word_probs, " self.word_probs 2")

    # def classify(self, message):
    #     self.word_probs = words_probablities(count_words(labels_for_words(for_classifier_message)))
    #     # print(self.word_probs, " self.word_probs 3")
    #     # print(for_classifier_message, " for_classifier_message")
    #     return  spam_probability(self.word_probs, message)

    def classify(self, message):
        # print(message, " message")
        # self.word_probs = words_probablities(count_words(labels_for_words(for_classifier_message)))
        return spam_probability(self.word_probs, message)

# train_classifier = NaiveBayesClassifier()
# train_classifier.train(labels_for_words(set_for_train))


# classifier = NaiveBayesClassifier()
# cl = classifier.classify(for_classifier_message)
# print(cl, " classifier.classify")

bar

# # Самопис, тк не было в учебнике
def split_data(data, prob):   # prob - кол-во данных train в %
    data_train_test = [], [] # кортеж с 2мя списками
    [data_train_test[0 if random.random() < prob else 1].append(i) for i in data]
    train, test = data_train_test[0], data_train_test[1]
    return train, test


path = r"D:\downloads\SPAM Assassian\test3\*"

data = [] # # Список кортежей (текст, метка)


for fn in glob.glob(path):

    is_spam = "ham" not in fn # # если в названии папки встречается "ham" то count_words в списке  [0 ,0] к value[1] +1
    # print("\t" * 7 , is_spam)
    with open(fn, "r") as file:
        for line in file:

            if line.startswith(("Subject")):
                subject = re.sub(r"^Subject:", "", line).strip()
                data.append((subject, is_spam)) # # маркируем сообщения спам/неспам - True/False


random.seed()
train_data, test_data = split_data(data, 0.75) # Получили массивы для обучения и теста
# print("\t" * 2, train_data, " train_dataaaa")
# print("\t" * 2, test_data, " test_dataaaa")

classifier = NaiveBayesClassifier()
classifier.train(train_data) # # если этот метод не запустить, то не будет self.word_probs = [] и дальше не будет данных

# #  subject - это выделенный текст сообщения; classify(subject) - классификация, вероятность спама
classified = [(subject, is_spam, classifier.classify(subject)) # метод classify, получаем триплет (word,bool,prob)
              for subject, is_spam in test_data] # # создаём триплет < текст, спам/неспам, вероятность> на тест данных
print("\t" * 2,classified, " триплет classifieddddddddddddddd")
counts = Counter ((is_spam, spam_probability > 0.5)for _, is_spam, spam_probability in classified)
print(counts, " countsssssssss")

classified.sort(key=lambda  row: row[2]) # # sort 3-му элементу из кортежа
print(classified, " classified.sort t t t t t t t t ")

spammist_hams = [filter(lambda  row: not row[1], classified)][-1:] # # посл значение из фильтра мах вероятность по False
# print([i for i in filter(lambda  row:  not row[1], classified)][-1:],"s s s s s s s s s sspammist_hams фильтр по False")
hammiest_spams = [filter(lambda  row:  row[1], classified)][:] # # первое значение из фильтра min вероятность по True
# print([j for j in filter(lambda  row:  row[1], classified)][:], " h h h h h h h h h hammiest_spams фильтр по True")

# # Определить вероятность спам/неспам для заданного слова, где word_prob - триплет
def p_spam_given_word(word_prob): # # передаём переменную classifier.word_probs в ф-ю p_spam_given_word и сортируем
    word, prob_if_spam, prob_if_not_spam = word_prob
    return  prob_if_spam / (prob_if_spam + prob_if_not_spam)

print(classifier.word_probs, " classifier.word_probs")
words = sorted(classifier.word_probs, key=p_spam_given_word)# # classifier.word_probs - переменная из класса
# print(words, " words s s s s s s s s")
spammist_words = words[-2:] # # два последних
hammiest_words = words [:2] # # два первых

print(spammist_words," спам" ,hammiest_words, " средний спам")

# def drop_final_s(word):
#     return re.sub("s$", "", word)

import math
import glob, re
from collections import defaultdict, Counter
import random
import numpy as np

# Сгенерировать список слов
set_for_train = " asdf rtyu rtyu poiu poiu poiu poiu poiu asdf asdddd"  #
for_classifier_message = " asdf poiu poiu dfghrtyu rtyu asdfpoiu asdf asdf qwert rewq asdf asdddd asdddd asdddd asdddd "


def tokenize(message):
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)


# print(tokenize("asdddd asdf rtyu rtyu poiu poiu"), " tokenize")


# Входящие строчные делим по пробелу и рандомно маркеруем 0 - спам, 1 - неспам
def labels_for_words(words_for_count):
    # print(words_for_count, " words_for_count")
    words = words_for_count.split(" ")
    w = random.choice([1, 0])
    return [
        x_mes
        for x_mes in zip(
            [x for x in words], [random.choice([1, 0]) for _ in range(len(words))]
        )
    ]


# print(train_label_message(str))


# tokenize - Считаем частотность слов
def count_words(training_set):
    counts = defaultdict(
        lambda: [0, 0]
    )  # из тела lambda в словарь counts  передаём value [0, 0]
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][
                0 if is_spam else 1
            ] += 1  # [word] - ключ,[0 if is_spam else  1] - индекс
    # print(counts, " counts counts counts")
    return counts


print(" ")
# count_words(train_label_message(" asdf rtyu rtyu poiu poiu poiu poiu poiu asdddd"))


# Этот блок исключён тк его вычисление в вызове words_probablities()
def spam_nonspam_for_probablities(counts):
    x_total_spam = sum([x for x, _ in [s for s in counts.values()]])
    y_non_total_spam = sum([y for _, y in [s for s in counts.values()]])
    # print(x_total_spam, y_non_total_spam, " total_spam, non_total_spam")
    return (x_total_spam, y_non_total_spam)


# (spam_nonspam_for_probablities(count_words(labels_for_words
#                                                     (" asdf rtyu rtyu poiu poiu poiu poiu poiu asdddd"))))


def words_probablities(counts, total_spam, total_non_spam, k=0.5):
    print(counts.items(), " словарь из токенайзера {word : [spam, non_spam]}")
    # total_spam, total_non_spam = spam_nonspam_for_probablities(count_words(labels_for_words
    #                                                 (for_classifier_message)))
    # print([(w, (spam + k) / (total_spam + 2 * k), (non_spam + k) / (total_non_spam + 2 * k))
    #         for w, (spam, non_spam) in counts.items()], " words_probablities spam, non_spam" )
    print([(k, v) for k, v in counts.values()], " spam, non_spammmmmmmmmmmmmmmmmmmmm")
    # print("\t" * 3, spam, non_spam, " <<<< >>>>", total_spam, total_non_spam )
    return [
        (
            w,
            (spam + k) / (total_spam + 2 * k),
            (non_spam + k) / (total_non_spam + 2 * k),
        )
        for w, (spam, non_spam) in counts.items()
    ]  #


# print(words_probablities(count_words(train_label_message(train_set)),
#                          sum([x for x,_ in [s for s in count_words(train_label_message(train_set)).values()]]),
#                          sum([y for _, y in [s for s in count_words(train_label_message(train_set)).values()]])),
#                             " вероятность появления слова в спам / неспам")

print(" ")


# log_probability , log-вероятность
def spam_probability(word_probs, message):
    message_words = tokenize(message)
    print(message_words, "TOKENIZEEEEEEEEEEEEEEEEEEEEEEEEEE")
    print(" ")
    log_prob_if_spam = log_prob_if_not_spam = 0.0
    for word, prob_if_spam, prob_if_not_spam in word_probs:
        print("\t" * 4, word, prob_if_spam, prob_if_not_spam, " word_probs 1 ")
        if word in message_words:
            # print(word,prob_if_spam, prob_if_not_spam, " word_probs 2 ")
            log_prob_if_spam += math.log(
                prob_if_spam
            )  # log_proba берём из словаря где key-слово,value-[спам, неспам]
            log_prob_if_not_spam += math.log(
                prob_if_not_spam
            )  # log-вероятности суммируем в переменную в log-форме
        else:
            log_prob_if_spam += math.log(1 - prob_if_spam)
            log_prob_if_not_spam += math.log(1 - prob_if_not_spam)
            print(" ")
        # print(log_prob_if_spam, " spam", log_prob_if_not_spam, " not_spam")
        print(" ")
    prob_if_spam = math.exp(
        log_prob_if_spam
    )  # math.exp() перевод из log-вероятности обратно в вероятность в процентах
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    # print(prob_if_spam / (prob_if_spam + prob_if_not_spam), " prob_if_spam / (prob_if_spam + prob_if_not_spam")
    return prob_if_spam / (
        prob_if_spam + prob_if_not_spam
    )  # вероятность появления слова в спаме


# spam_probability(words_probablities(count_words(labels_for_words(set_for_train)),  # set_for_train тренинговая выборка
#     sum([x for x,_ in [s for s in count_words(labels_for_words(set_for_train)).values()]]),
#     sum([y for _, y in [s for s in count_words(labels_for_words(set_for_train)).values()]])), for_classifier_message)


class NaiveBayesClassifier:
    def __init__(self, k=0.5):

        self.k = k
        self.word_probs = []

    def train(self, training_set):
        print(training_set, " training_setttttt")
        print(" ")
        num_spams = len([is_spam for message, is_spam in training_set if is_spam])
        num_non_spams = len(training_set) - num_spams

        word_counts = count_words(training_set)  # Токенайзер
        print(word_counts, " Токенайзер p p p p p p p p p p p p p p p p p ")
        print(num_spams, num_non_spams, " num_spams, num_non_spamsssssssssssssssss")
        self.word_probs = words_probablities(
            word_counts, num_spams, num_non_spams, self.k
        )
        # self.word_probs = words_probablities(word_counts, self.k)
        # print(self.word_probs, " self.word_probs 2")

    # def classify(self, message):
    #     self.word_probs = words_probablities(count_words(labels_for_words(for_classifier_message)))
    #     # print(self.word_probs, " self.word_probs 3")
    #     # print(for_classifier_message, " for_classifier_message")
    #     return  spam_probability(self.word_probs, message)

    def classify(self, message):
        print(message, " >>>>>>>>>>>")
        # self.word_probs = words_probablities(count_words(labels_for_words(for_classifier_message)))
        return spam_probability(self.word_probs, message)


# train_classifier = NaiveBayesClassifier()
# train_classifier.train(labels_for_words(set_for_train))


# classifier = NaiveBayesClassifier()
# cl = classifier.classify(for_classifier_message)
# print(cl, " classifier.classify")


def split_data(data, prob):  # prob - кол-во данных train в %
    data_train_test = [], []  # кортеж с 2мя списками
    [data_train_test[0 if random.random() < prob else 1].append(i) for i in data]
    train, test = data_train_test[0], data_train_test[1]
    return train, test


path = r"D:\downloads\SPAM Assassian\test\*"

data = []  # Словарь кортежей (words : lable)


for fn in glob.glob(path):

    is_spam = "ham" not in fn
    print("\t" * 7, is_spam)
    with open(fn, "r") as file:
        for line in file:

            if line.startswith(("Subject")):
                subject = re.sub(r"^Subject:", "", line).strip()
                data.append((subject, is_spam))
print(data, " data [] [] [] ")
print(" ")
# random.seed(0)
train_data, test_data = split_data(data, 0.75)  # Получили массивы для обучения и теста
print("\t" * 2, train_data, " train_dataaaa")
print("\t" * 2, test_data, " test_dataaaa")
print(" ")
classifier = NaiveBayesClassifier()
classifier.train(train_data)  # метод train

classified = [
    (
        subject,
        is_spam,
        classifier.classify(subject),
    )  # subject - это выделенный текст сообщения
    for subject, is_spam in test_data
]  # метод classify
print(classified, " classifieddddddddddddddd")
# counts = Counter ((is_spam, spam_probability > 0.5)for _, is_spam, spam_probability in classified)

# classified.sort(key=lambda  row: row[2])
# spammist_hams = filter(lambda  row: not row[1], classified)[-5:]
# hammiest_spams = filter(lambda  row:  row[1], classified)[:5]
# def p_spam_given_word(word_prob):
#     word, prob_if_spam, prob_if_not_spam = word_prob
#     return  prob_if_spam / (prob_if_spam + prob_if_not_spam)
# words = sorted(classifier.word_probs, key=p_spam_given_word)
# spammist_words = words[-5:]
# hammiest_words = words [:5]

# def drop_final_s(word):
#     return re.sub("s$", "", word)

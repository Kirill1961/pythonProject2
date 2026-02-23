import math
import re
from collections import defaultdict
import random
import numpy as np

# Сгенерировать список слов
train_set = " asdf rtyu rtyu poiu poiu poiu poiu poiu asdf asdddd" #
for_tokenize_message = " asdf poiu poiu dfghrtyu rtyu asdfpoiu asdf asdf  qwert rewq asdf asdddd asdddd asdddd asdddd "

def tokenize(message):
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)
# print(tokenize("asdddd asdf rtyu rtyu poiu poiu"), " tokenize")



# Входящие строчные делим по пробелу и рандомно маркеруем 0 - спам, 1 - неспам
def train_label_message(words_for_count):
    # print(words_for_count, " words_for_count")
    words = words_for_count.split(" ")
    w = random.choice([1, 0])
    return [x_mes for x_mes in zip([x for x in words], [random.choice([1, 0]) for _ in range(len(words))])]

# print(train_label_message(str))


# Считаем частотность слов
def count_words(training_set):
    counts = defaultdict(lambda: [0, 0])# из тела lambda в словарь counts  передаём value [0, 0]
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1] += 1
    # print(counts, " counts counts counts")
    return counts
print(" ")
# count_words(train_label_message(" asdf rtyu rtyu poiu poiu poiu poiu poiu asdddd"))



# Этот блок исключён тк его вычисление в вызове words_probablities()
def spam_nonspam_for_probablities(counts):
    x_total_spam = sum([x for x,_ in [s for s in counts.values()]])
    y_non_total_spam = sum([y for _, y in [s for s in counts.values()]])
    # print(x_total_spam, y_non_total_spam, " total_spam, non_total_spam")
    return (x_total_spam, y_non_total_spam)

# (total_spam_for_words_probablities(count_words(train_label_message
#                                                     (" asdf rtyu rtyu poiu poiu poiu poiu poiu asdddd"))))




def words_probablities(counts, total_spam, total_non_spam, k = 0.5):
    print(counts.items(), " в списках кол-во встречающихся слов в спаме и в неспаме, 1е - спам, 2е - не спам")
    print(" ")
    return [(w, (spam + k) / (total_spam + 2 * k), (non_spam + k) / (total_non_spam + 2 * k))
            for w, (spam, non_spam) in counts.items()]


# print(words_probablities(count_words(train_label_message(train_set)),
#                          sum([x for x,_ in [s for s in count_words(train_label_message(train_set)).values()]]),
#                          sum([y for _, y in [s for s in count_words(train_label_message(train_set)).values()]])),
#                             " вероятность появления слова в спам / неспам")

print(" ")

# log_probability , log-вероятность
def spam_probability(word_probs, message):
    message_words = tokenize(message)
    print(message_words, " message_words-текст для контроля спам / неспам")
    print(" ")
    log_prob_if_spam = log_prob_if_not_spam = 0.0
    for word, prob_if_spam, prob_if_not_spam in word_probs:
        if word in message_words:
            print(word,prob_if_spam, prob_if_not_spam, " word_probs")
            log_prob_if_spam += math.log(prob_if_spam) # log_proba берём из словаря где key-слово,value-[спам, неспам]
            log_prob_if_not_spam += math.log (prob_if_not_spam)  # log-вероятности суммируем в переменную в log-форме
        else:
            log_prob_if_spam += math.log(1 - prob_if_spam)
            log_prob_if_not_spam += math.log(1 - prob_if_not_spam)
            print(" ")
        print(log_prob_if_spam, " spam", log_prob_if_not_spam, " not_spam")
        print(" ")
    prob_if_spam = math.exp(log_prob_if_spam) # math.exp() перевод из log-вероятности обратно в вероятность в процентах
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    print(prob_if_spam / (prob_if_spam + prob_if_not_spam), " ")
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)# вероятность появления слова в спаме

# spam_probability(words_probablities(count_words(train_label_message(train_set)),# train_set тренинговая выборка
#         sum([x for x,_ in [s for s in count_words(train_label_message(train_set)).values()]]),
#         sum([y for _, y in [s for s in count_words(train_label_message(train_set)).values()]])), for_tokenize_message)

class NaiveBayesClassifier:
    def __init__(self, k=0.5):
        self.k = k
        self.word_probs = []

    def train (self, training_set, k = 5):
        num_spams = len([is_spam for message, is_spam in training_set if is_spam])
        num_non_spams = len(training_set) - num_spams
        word_counts = count_words(training_set)
        self.word_probs = words_probablities(word_counts, num_spams, num_non_spams, self.k)

    def classify(self, message):
        return  spam_probability(self.word_probs, message)

t_s = NaiveBayesClassifier()
# t_s.train(train_label_message(train_set))
print(t_s.classify(for_tokenize_message), "TRANSFORM on Git")
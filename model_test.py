import glob, re
import random
from collections import Counter

# path = r"D:\downloads\SPAM Assassian\ee_k.txt"



""" Проверка работы доставки фа-лов из папки test """

path = r"D:\downloads\SPAM Assassian\test\*"
data = [path]

for fn in glob.glob(path):
    print(fn)
    is_spam = "ham" not in fn

    # print(is_spam)
    with open(fn, "r") as file:
        for line in file:
            # print(line)
            if line.startswith(("Subject")):
                subject = re.sub(r"^Subject:", "", line).strip()
                data.append((subject, is_spam))
print(data)







# def split_data(data, prob):
#     data_train_test = [], []
#     [data_train_test[0 if random.random() < prob else 1].append(i) for i in (" ".join(data).split())]
#     train, test = data_train_test[0], data_train_test[1]
#     return train, test
#
# for fn in glob.glob(path):
#     # print(fn)
#     is_spam = "ham" not in fn
#     # print(is_spam)
#     with open(fn, "r") as file:
#         for line in file:
#             # print(line)
#             if line.startswith(("Subject")):
#                 subject = re.sub(r"^Subject:", "", line).strip()
#                 data.append((subject, is_spam))
# random.seed(0)
# train_data, test_data = split_data(data, 0.75)
# print(train_data, test_data, " >>>>>>>>>>>>>>")
# classifier = NaiveBayesClassifier()
# classifier.train(train_data)
# classified = [(subject, is_spam, classifier.classify(subject))for subject, is_spam in test_data]
# counts = Counter ((is_spam, spam_probability > 0.5)for _, is_spam, spam_probability in classified)
# classified.sort(key=lambda  row: row[2])
# spammist_hams = filter(lambda  row: not row[1], classified)[-5:]
# hammiest_spams = filter(lambda  row: not row[1], classified)[:5]
# def p_spam_given_word(word_prob):
#     word, prob_if_spam, prob_if_not_spam = word_prob
#     return  prob_if_spam / (prob_if_spam + prob_if_not_spam)
# words = sorted(classifier.word_probs, key=p_spam_given_word)
# spammist_words = words[-5:]
# hammiest_words = words [:5]
#
# def drop_final_s(word):
#     return re.sub("s$", "", word)
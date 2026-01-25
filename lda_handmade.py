import random
from collections import defaultdict


docs = [
    ["кот", "любит", "молоко"],
    ["собака", "любит", "кость"],
    ["кот", "собака", "друзья"]
]

K = 2  # число тем


# TODO Инициализация (самый грязный, но важный шаг)

# z[d][i] — тема i-го слова в d-м документе
z = []

for doc in docs:
    z.append([random.randint(0, K-1) for _ in doc])

# Счётчики (СЕРДЦЕ LDA)
ndk = defaultdict(int)   # сколько слов темы k в документе d
nkw = defaultdict(int)   # сколько раз слово w в теме k
nk  = defaultdict(int)   # всего слов в теме k


for d, doc in enumerate(docs):
    for i, word in enumerate(doc):
        topic = z[d][i]
        ndk[(d, topic)] += 1
        nkw[(topic, word)] += 1
        nk[topic] += 1

# ОДИН шаг Gibbs sampling (ключевой момент)
alpha = 0.1
beta = 0.1
V = len(set(w for doc in docs for w in doc))

# Убираем старую тему
old_topic = z[d][i]
word = docs[d][i]

ndk[(d, old_topic)] -= 1
nkw[(old_topic, word)] -= 1
nk[old_topic] -= 1

# Считаем вероятности тем (САМОЕ ГЛАВНОЕ)
probs = []

for k in range(K):
    p_topic_doc = ndk[(d, k)] + alpha
    p_word_topic = (nkw[(k, word)] + beta) / (nk[k] + V * beta)
    probs.append(p_topic_doc * p_word_topic)


# СЭМПЛИРУЕМ новую тему
new_topic = random.choices(range(K), weights=probs)[0]
z[d][i] = new_topic

# Возвращаем счётчики назад
ndk[(d, new_topic)] += 1
nkw[(new_topic, word)] += 1
nk[new_topic] += 1

print(ndk, '\n')
print(nkw, '\n')
print(nk)


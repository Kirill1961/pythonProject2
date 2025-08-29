from dtreeviz import dtreeviz
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import make_blobs
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import mutual_info_classif
from sklearn.metrics import classification_report
from sklearn.tree import export_text
import numpy as np


# print(dir(dtreeviz))

RANDOM_SEED = 0

# TODO Генерация двух признаков распределённых по трём классам
X, y = make_blobs(n_samples=1000, centers=[(0, 3), (3, 3), (3, 0)],
                   n_features=2, random_state=RANDOM_SEED,
                   cluster_std=(0.9, 0.9, 0.9),)


# TODO Взаимная Информация
print('\n', 'Взаимная Информация, по количеству признаков : ', '\n', mutual_info_classif(X, y), '\n')

# TODO Псстроение scatter с seaborn, только через преобразование в df
df = pd.DataFrame(X, columns=['X_0', 'X_1'])
df['target'] = y  # добавляем в df целевую переменную

# print(df[['X_0', 'X_1']], df['target'])

clf_tree = DecisionTreeClassifier(criterion='gini', max_depth=7, random_state=0).fit(X, y)

# TODO cross_validation вывод accuracy
for d in range(1, 20):
    model = DecisionTreeClassifier(max_depth=d, criterion='gini')
    scores = cross_val_score(model, X, y, cv=5)
    print(f"depth={d}, mean accuracy={scores.mean():.3f}")

# TODO Визуализвция Дерева
plot_tree(clf_tree)
plt.show()

# TODO cross_validation вывод scores (для каждого фолда) и accuracy
for d in range(1, 20):
    model = DecisionTreeClassifier(max_depth=d, criterion='gini')
    scores = cross_val_score(model, X, y, cv=5)
    print(f"depth={d}, scores={scores}, mean accuracy={scores.mean():.3f}")


# TODO cross_validation, Сравнение DecisionTreeClassifier и LogisticRegression
models = {
    'Tree depth=3': DecisionTreeClassifier(max_depth=3, random_state=0),
    'LogisticRegression': LogisticRegression()
}

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5)
    print(f"{name}: scores={scores}, mean accuracy={scores.mean():.3f}")



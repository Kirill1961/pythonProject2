from dtreeviz import dtreeviz
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import make_blobs
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.tree import export_text
import numpy as np


# print(dir(dtreeviz))

RANDOM_SEED = 0

# TODO Генерация двух прихнаков распределённых по трём классам
X, y =  make_blobs(n_samples=10, centers=[(0, 3), (3, 3), (3, 0)],
                   n_features=2, random_state=RANDOM_SEED,
                   cluster_std=(0.9, 0.9, 0.9),)


# TODO Псстроение scatter с seaborn, только через преобразование в df
df = pd.DataFrame(X, columns=['X_0', 'X_1'])
df['target'] = y  # добавляем в df целевую переменную

print(df[['X_0', 'X_1']], df['target'])

clf_tree = DecisionTreeClassifier(criterion='gini', max_depth=7, random_state=0).fit(X, y)


# TODO Визуализвция Дерева
plot_tree(clf_tree)
# plt.show()

# y = y.astype(int)
print(X.shape)
print(type(y))

print("X type:", type(X), "shape:", X.shape)
print("y type:", type(y), "shape:", y.shape)
print("y dtype:", y.dtype)
print("Unique classes:", np.unique(y))

# X_ = df[['X_0', 'X_1']]
# y_ = df['target']
#
# viz = dtreeviz(clf_tree, X_, y_,
#                target_name='target',
#                feature_names=['X_0', 'X_1'],
#                class_names=["0", "1", "2"])
#
# viz.view()  # в Jupyter или сохранение в файл

viz = dtreeviz(clf_tree,
               df[['X_0', 'X_1']],  # <-- DataFrame с названиями колонок
               df['target'],        # <-- Series
               target_name='target',
               feature_names=['X_0', 'X_1'],
               class_names=["0", "1", "2"])
viz.view()

from dtreeviz import model as dtreeviz_model
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import make_blobs
import dtreeviz as dtv
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.tree import export_text
import numpy as np


# print(dir(dtreeviz))

RANDOM_SEED = 0

# TODO Генерация двух признаков распределённых по трём классам
X, y = make_blobs(n_samples=100, centers=[(0, 3), (3, 3), (3, 0)],
                   n_features=2, random_state=RANDOM_SEED,
                   cluster_std=(0.9, 0.9, 0.9),)


# TODO Псстроение scatter с seaborn, только через преобразование в df
df = pd.DataFrame(X.astype(int), columns=['X_0', 'X_1'])
df['target'] = y  # добавляем в df целевую переменную

# print(df[['X_0', 'X_1']], df['target'])

clf_tree = DecisionTreeClassifier(criterion='gini', max_depth=15, random_state=0).fit(X, y)


# TODO Визуализвция Дерева
# plot_tree(clf_tree)
# plt.show()


# print(X.shape)
# print(type(y))

print("X type:", type(X), "shape:", X.shape)
print("y type:", type(y), "shape:", y.shape)
print("y dtype:", y.dtype)
print("Unique classes:", np.unique(y))

X_ = df[['X_0', 'X_1']]
y_ = df['target']


print("X_ type:", type(X_), "shape:", X_.shape)
print("y_ type:", type(y_), "shape:", y_.shape)
print("y_ dtype:", y_.dtype)
print("Unique classes:", np.unique(y_))

# print(X_)
# viz = dtreeviz_model(clf_tree, X, y,
#                target_name='target',
#                feature_names=['X_0', 'X_1'],
#                class_names=["0", "1", "2"])
#
# viz.view()         # визуализация дерева
# viz.leaf_sizes()   # размерности листьев
viz = dtreeviz_model(clf_tree,
               df[['X_0', 'X_1']],  # <-- DataFrame с названиями колонок
               df['target'].astype(int),        # <-- Series
               target_name='target',
               feature_names=['X_0', 'X_1'],
               class_names=["0", "1", "2"])

# print(viz.view()  )       # визуализация дерева
# print(viz.leaf_sizes() )  # размерности листьев

# # Выделим интересующий экземпляр по индексу
# viz.highlight_instance(3)



# Возьмём 4-ю строку из X (индекс 3)
sample_point = df.loc[2, ['X_0', 'X_1']].tolist()

# print(sample_point)

# TODO Отрисовка  пространства признаков с учётом распределения по классам и диаграммы листьев
viz.ctree_feature_space()
viz.leaf_sizes()
plt.show()
# viz.ctree_feature_space(features=sample_point)
# viz.ctree_feature_space(features=df.loc[0, ['X_0', 'X_1']].tolist())

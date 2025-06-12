from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import make_blobs
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.tree import export_text

RANDOM_SEED = 0

# TODO Генерация двух прихнаков распределённых по трём классам
X, y =  make_blobs(n_samples=50, centers=[(0, 3), (3, 3), (3, 0)],
                   n_features=2, random_state=RANDOM_SEED,
                   cluster_std=(0.9, 0.9, 0.9),)

# TODO Псстроение scatter с seaborn, только через преобразование в df
df = pd.DataFrame(X, columns=['X_0', 'X_1'])
df['target'] = y  # добавляем в df целевую переменную

# print(df)

sns.scatterplot(data=df, x='X_0', y='X_1', hue='target', palette='deep')
# plt.show()

# TODO Псстроение scatter с plt
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='Set1')
# plt.show()

clf_tree = DecisionTreeClassifier(criterion='gini', max_depth=7, random_state=0).fit(X, y)
# clf_tree.fit(X, y)


# TODO Визуализвция Дерева
plot_tree(clf_tree)
# plt.show()

# TODO Важность признаков - Feature Importance
#  Работает только с df из pfndas
feature_importance = clf_tree.feature_importances_
print(feature_importance)

feature_importance = pd.Series(feature_importance, index=df.columns[:-1]).sort_values(ascending=False)
print(feature_importance)

# TODO Текстовое дерево с фильтрацией по глубине
tree_text = export_text(clf_tree,
                        feature_names=['X_0', 'X_1'],
                        max_depth=2)  # Смотрим два уровня
print(tree_text)

# TODO Походим по дереву руками — доступ к структуре дерева через tree_
tree = clf_tree.tree_

print("Количество узлов:", tree.node_count)
print("Левый ребёнок узла 0:", tree.children_left[0])
print("Порог на узле 0:", tree.threshold[0])
print("Признак на узле 0:", tree.feature[0])
print("Правый ребёнок узла 0:", tree.children_right[0])
print("Порог на узле 1:", tree.threshold[1])
print("Признак на узле 1:", tree.feature[1])
print("Правый ребёнок узла 1:", tree.children_right[1])
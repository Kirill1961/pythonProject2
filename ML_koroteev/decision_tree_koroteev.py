from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import make_blobs
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


RANDOM_SEED = 0

# TODO Генерация двух прихнаков распределённых по трём классам
X, y =  make_blobs(n_samples=50, centers=[(0, 3), (3, 3), (3, 0)],
                   n_features=2, random_state=RANDOM_SEED,
                   cluster_std=(0.9, 0.9, 0.9),)

# TODO Псстроение scatter с seaborn, только через преобразование в df
df = pd.DataFrame(X, columns=['X1', 'X2'])
df['target'] = y  # добавляем в df целевую переменную

sns.scatterplot(data=df, x='X1', y='X2', hue='target', palette='deep')
# plt.show()

# TODO Псстроение scatter с plt
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='Set1')
# plt.show()

clf_tree = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=0).fit(X, y)
clf_tree.fit(X, y)


plot_tree(clf_tree)
plt.show()
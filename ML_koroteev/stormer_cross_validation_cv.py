from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.datasets import make_blobs


RANDOM_SEED = 0

# TODO Генерация двух прихнаков распределённых по трём классам
X, y = make_blobs(n_samples=1000, centers=[(0, 3), (3, 3), (3, 0)],
                   n_features=2, random_state=RANDOM_SEED,
                   cluster_std=(0.9, 0.9, 0.9),)

clf_tree = DecisionTreeClassifier(criterion='gini', max_depth=7, random_state=0)
clf_tree.fit(X, y)


models = {
    "Decision Tree": DecisionTreeClassifier(max_depth=3),
    "Logistic Regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVC": SVC()
}


# TODO scores.mean - Это среднее всех обобщёных оценок: accuracy, R² и т.п.
#  По умолчанию cross_val_score(..., scoring=None)
#  - для классификации: считает accuracy
#  - для регрессии: считает R² (коэффициент детерминации)
for name, model in models.items():
    scores = cross_val_score(model, X, y, scoring='accuracy', cv=5)
    print(f"{name}: mean accuracy = {scores.mean():.3f}, all scores = {scores}")

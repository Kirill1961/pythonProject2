import pandas as pd
import numpy as np
import re
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV

X, y = load_iris(return_X_y=True, as_frame=True)

print(X.shape, y.shape)

rdf = RandomForestClassifier(n_estimators=100, n_jobs=4, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=24, stratify=y)

rdf.fit(X_train, y_train)

y_pred = rdf.predict(X_test)
y_score = rdf.predict_proba(X_test)



print('Количество деревьев : \n', len(rdf.estimators_))

# TODO  Если predict_proba(X_test) используем DF и получаем список/list деревьев 👉 с вероятностью 1-го класса 👈
est_df = [est.predict_proba(X_test) for est in rdf.estimators_]

# print(est_df)

# TODO Если predict_proba(X_test.values) объекты в чистом виде,
#  получаем ndarray-матрицу деревьев 👉 с вероятностью 1-го класса 👈
est_ar = np.hstack([est.predict_proba(X_test.values)[:, 1] for est in rdf.estimators_])

print(est_ar)
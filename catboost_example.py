import numpy as np
import pandas as pd

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from catboost import CatBoostClassifier

X, y = fetch_openml(
    name="adult",
    version=2,
    as_frame=True,
    return_X_y=True
)

# target в бинарный вид
y = (y == ">50K").astype(int)

print(X.info())

# print(X.dtypes)

cat_features = X.select_dtypes(include="object").columns.tolist()
print(cat_features)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = CatBoostClassifier(
    iterations=200,
    depth=6,
    learning_rate=0.1,
    loss_function="Logloss",
    eval_metric="Accuracy",

    # ключевое для нашей темы
    cat_features=cat_features,

    # чтобы было видно обучение
    verbose=50,

    # фиксируем random seed (перестановки!)
    random_seed=42
)

model.fit(
    X_train,
    y_train,
    eval_set=(X_test, y_test)
)

y_pred = model.predict(X_test)
accuracy_score(y_test, y_pred)

importances = pd.Series(
    model.get_feature_importance(),
    index=X.columns
).sort_values(ascending=False)

importances.head(10)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV, cross_val_predict
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.datasets import fetch_openml
import pandas as pd


# Загрузка данных
data = fetch_openml(name='titanic', version=1, as_frame=True)
X = data.data[['pclass', 'age', 'sex']]
y = data.target

# Определение предобработки
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), ['age']),
        ('cat', OneHotEncoder(), ['pclass', 'sex'])
    ]
)

# Определение пайплайна
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])

# Подбор гиперпараметров
param_grid = {
    'classifier__C': [0.1, 1.0, 10.0]
}

# GridSearchCV
grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X, y)

# Лучшие параметры и оценка
print("Лучшие параметры:", grid_search.best_params_)
print("Лучший результат (accuracy):", grid_search.best_score_)


# TODO cross_val_predict - возвращает предсказания модели для каждого объекта, сделанные в процессе кросс-валидации.
# Данные
df = pd.DataFrame({
    "x1": [1, 2, 3, 4, 5],
    "y": [2, 4, 6, 8, 10]
})

X = df[["x1"]]
y = df["y"]

# Предсказания по кросс-валидации
preds = cross_val_predict(LinearRegression(), X, y, cv=5)

# Проверяем размеры и сами предсказания
print(len(preds), "==", X.shape[0])  # >>> 5 == 5
print(preds)    # >>> [ 2.  4.  6.  8. 10.]

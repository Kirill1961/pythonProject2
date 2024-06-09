from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.datasets import fetch_openml

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

from sklearn.preprocessing import OrdinalEncoder, TargetEncoder
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer

# TODO OrdinalEncoder - Векторное Кодирование Порядковых признаков
df = pd.DataFrame({
    "col1": ["high", "low", "medium"],
    "col2": ['two', 'three', 'one'],
    "col3": ['Male', 'Female', 'Male']
})

enc = OrdinalEncoder()
X_cat = enc.fit_transform(df[['col1']])

print(X_cat)

#  TODO Разделение на cat_feat и num_feat
#   * Стандартизация -  num_feat
#   * OneHotEncoder (OHE) - cat_feat

df1 = pd.DataFrame({
    'age': [25, 32, 47, 51],
    'gender': ['male', 'female', 'female', 'male'],
    'salary': [50000, 60000, 80000, 90000],
    'city': ['NY', 'LA', 'NY', 'SF']
})

# Указываем, какие колонки куда идут
num_features = ['age', 'salary']
cat_features = ['gender', 'city']

# TODO sparse_output=False - параметр убирает Разрежение матрицы
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),  # стандартизация числовых
        ('cat', OneHotEncoder(sparse_output=False), cat_features)  # OHE для категориальных
    ]
)

# Применяем трансформации
X_processed = preprocessor.fit_transform(df1)

print(X_processed)  # если Вернёт sparse matrix

# TODO если OHE вернёт sparse matrix
# print(X_processed.toarray())

X = pd.DataFrame({
    "Sex": ["M", "F", "M"],
    "Housing": ["own", "rent", "own"]
})

cat_pipe = make_pipeline(
    SimpleImputer(strategy="most_frequent"),
    OneHotEncoder(handle_unknown="ignore")
)

ct = ColumnTransformer([
    ("cat", cat_pipe, ["Sex", "Housing"])
], remainder="passthrough")

X_trans = ct.fit_transform(X)
print(ct.get_feature_names_out(), '\n')


# TODO TargetEncoder - кодирует global target mean
#  global target mean используется в XGBoost

df = pd.DataFrame({'col1': ['A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B'],
                    'col2': [1, 0, 0, 1, 1, 1, 0, 0, 1, 1]})
X = np.array(df.col1).reshape(-1, 1)
y = np.array(df.col2)

enc = TargetEncoder(cv=5)
print(enc.fit_transform(X, y), '\n')


# TODO Если df маленький, уменьшаем число фолдов cv=3
df1 = pd.DataFrame({'col1': ['A', 'A', 'B', 'A', 'B'],
                    'col2': [1, 0, 0, 1, 1]})
X1 = np.array(df1['col1']).reshape(-1, 1)
y1 = np.array(df1['col2'])

enc1 = TargetEncoder(cv=3)
print(enc1.fit_transform(X1, y1), '\n')

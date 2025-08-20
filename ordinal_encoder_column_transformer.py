from sklearn.preprocessing import OrdinalEncoder
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# TODO OrdinalEncoder - Кодирование Порядковых признаков
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

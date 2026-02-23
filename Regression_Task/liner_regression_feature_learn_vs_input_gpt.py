from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Пример данных
data = pd.DataFrame(
    {
        "numeric_feature": [0.5, 2.3, 2.9, 3.0],
        "categorical_feature": ["a", "b", "a", "b"],
    }
)

# Обучающие данные
X_train = data
y_train = np.random.rand(len(data))

# Предобработка
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["numeric_feature"]),
        ("cat", OneHotEncoder(), ["categorical_feature"]),
    ]
)

# Создание пайплайна
pipeline = Pipeline(
    steps=[("preprocessor", preprocessor), ("model", LinearRegression())]
)

# Обучение модели
pipeline.fit(X_train, y_train)

# Новые данные с теми же признаками
new_data = pd.DataFrame(
    {"numeric_feature": [1.5, 3.5], "categorical_feature": ["a", "b"]}
)

# Предсказание
predictions = pipeline.predict(new_data)
print(predictions)

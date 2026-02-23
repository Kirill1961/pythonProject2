import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Пример: создадим DataFrame с одним признаком
# df = pd.DataFrame({'feature_1': [10, 20, 30, 40, 50], 'feature_2': [1, 2, 3, 4, 5], 'target': [15, 25, 35, 45, 55]}, )

np.random.seed(0)
df = pd.DataFrame({'feature_1': np.random.random(100),
                   'feature_2': (np.random.random(100)),
                   'target': (np.random.binomial(1, 0.7, size=100))} )

# TODO Отделяем Целевую от DF
X = df.drop('target', axis=1)
y = df['target']

# TODO Делим на train и test
#  * stratify - если применяем то Целевая Y должна иметь более 2х классов
X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# TODO Центрируем
scaler = StandardScaler()
X_train_scal = scaler.fit_transform(X_train)  # Обучение
X_test_scal = scaler.transform(X_test)  # Проверяем переводные коэфф.



# Преобразуем обратно в DataFrame
scaled_df = pd.DataFrame(X_train_scal, columns=['feature_1', 'feature_2'])

# TODO fit_transform - возвращает nampy.ndarray
#  Поэтому срезы массива
print(X_train_scal[:, 1][:10])



# Код для визуализации распределения
fig, (axes1, axes2) = plt.subplots(1, 2, figsize=(7, 5))
sns.histplot(X_train_scal[:, 1], ax=axes1, kde=True)
sns.histplot(scaled_df['feature_2'], ax=axes2, kde=True)
plt.title('Распределение после '
          'StandardScaler')
# plt.xlabel('Значения')
# plt.ylabel('Плотность')
plt.show()

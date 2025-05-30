import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Пример: создадим DataFrame с одним признаком
df = pd.DataFrame({'feature': [10, 20, 30, 40, 50]})

# Применим StandardScaler
scaler = StandardScaler()
scaled = scaler.fit_transform(df)

# Преобразуем обратно в DataFrame
scaled_df = pd.DataFrame(scaled, columns=['feature_scaled'])

# Код для визуализации распределения
fig, (axes1, axes2) = plt.subplots(1, 2, figsize=(7, 5))
sns.histplot(df['feature'], ax=axes1, kde=True)
sns.histplot(scaled_df['feature_scaled'], ax=axes2, kde=True)
plt.title('Распределение после StandardScaler')
# plt.xlabel('Значения')
# plt.ylabel('Плотность')
plt.show()

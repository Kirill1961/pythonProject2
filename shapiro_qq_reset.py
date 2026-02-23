import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro
from statsmodels.graphics.gofplots import qqplot
import numpy as np
import matplotlib.pyplot as plt
# import statsmodels.api as sm
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.diagnostic import linear_reset
import seaborn as sns



# TODO Проверка на линейность остатков по QQ-plot

# Пример данных
data = np.random.normal(loc=0, scale=1, size=100)

# Тест Шапиро
stat, p = shapiro(data)
print(f"Shapiro-Wilk stat={stat:.3f}, p-value={p:.3f}")

# Визуализация
sns.histplot(data, kde=True)
plt.title("Гистограмма")
plt.show()

qqplot(data, line='s')
plt.title("Q-Q plot")
plt.show()

# TODO Проверка на линейность остатков по scatterplot теста Шапиро
#  scatterplot строим в координатах Х - предсказания, У - остатки

# Примерные данные
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 3 * x + np.random.normal(0, 3, size=100)
df = pd.DataFrame({'x': x, 'y': y})

# Обучаем модель
model = ols('y ~ x', data=df).fit()

# Остатки и предсказания
residuals = model.resid
predicted = model.fittedvalues

# Scatterplot остатков
plt.scatter(predicted, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Предсказанные значения')
plt.ylabel('Остатки')
plt.title('Scatterplot остатков')
plt.show()


# TODO RESET-тест — единственный формальный способ прямо протестировать линейность в модели OLS.
#  Все остальные — косвенные признаки, которые указывают на необходимость усложнить модель
#  (например, добавить полиномы или использовать нелинейную регрессию).



# Загружаем пример данных
df = sns.load_dataset('mpg').dropna()
df = df.rename(columns={'horsepower': 'hp', 'weight': 'wt', 'mpg': 'mpg'})

print(df.info())

# Строим модель линейной регрессии
model = ols('mpg ~ hp + wt', data=df).fit()

# TODO Параметры
#  power - Степень, до которой берутся степени предсказанных значений ŷ
#  use_f - Логический параметр: использовать ли F-тест (True) или χ²-тест (False).
#   * Для небольших выборок обычно выбирают F.

# Выполняем RESET-тест (по умолчанию добавляется степень 2)
reset_result = linear_reset(model, power=2, use_f=True)

print(reset_result)

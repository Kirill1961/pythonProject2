import pandas as pd
# import patsy
# from patsy import dmatrices
from patsy.highlevel import dmatrices  # highlevel - явный импорт

# TODO patsy — это библиотека Python, которая:
#  * преобразует формулы в стиле R ('y ~ x1 + x2 + x1:x2')
#  * в матрицы признаков (X) и целевые значения (y)
#  * для моделей из statsmodels, scikit-learn, xgboost, и других

df = pd.DataFrame({
    'Segmentation': ['A', 'B', 'A', 'C', 'B', 'D'],
    'Age': [25, 34, 22, 45, 31, 28],
    'Spending_Score': ['High', 'Low', 'Average', 'High', 'Average', 'Low']
})

# y, X = patsy.dmatrices('Segmentation ~ Age + Spending_Score', data=df, return_type='dataframe')
y_, X_ = dmatrices('Segmentation ~ Age + Spending_Score', data=df, return_type='dataframe')

# print(patsy.__version__)
# print(dir(patsy))

print('y (endog); Каждая строка — one-hot представление класса Segmentation.')

print(y_, '\n')

print('X (exog); Колонка Intercept добавляется автоматически')
print('Spending_Score закодирован как dummy-переменные (одна опущена — здесь Low как базовая')

print(X_)
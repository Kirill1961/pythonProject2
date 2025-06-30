
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate


data = pd.read_csv('D:\Eduson_data\diamonds1.csv')


__doc__ = '''Добавление Полиномов исходных признаков 2-й, 
            3-й степени + попарное перемножение + log признаков'''


X, Y = datasets.fetch_california_housing(as_frame=True, return_X_y=True)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,  train_size=0.9, random_state=42)


# TODO min / max Целевой для MSE - интерпретации
print(Y_train.min(), Y_train.max())


scaler = StandardScaler()
scaler.fit(X, Y)
X_train_sc= pd.DataFrame(scaler.transform(X_train), columns=scaler.get_feature_names_out())
X_test_sc = pd.DataFrame(scaler.transform( X_test), columns=scaler.get_feature_names_out())


X_train_ext = X_train_sc.copy()  # Копия для ЕХРТ
X_test_ext = X_test_sc.copy()  # Копия для ЕХРТ


num_col = X_train_ext.shape[1]  # Число циклов по количеству признаков


# TODO Инициализация дополнительных DF для cube и log
X_train_cube = pd.DataFrame()
X_train_log = pd.DataFrame()
X_test_cube = pd.DataFrame()
X_test_log = pd.DataFrame()


for i in range(num_col):
  column = X_train_sc.columns[i]  # Имена столбцов из исходного DF


  X_train_cube[f'{column}^3'] = X_train_sc[column] ** 3
  X_test_cube[f'{column}^3'] = X_test_sc[column] ** 3
  X_train_log[f'{column}_log'] = np.log(10 + X_train_sc[f'{column}'])
  X_test_log[f'{column}_log'] = np.log(10 + X_test_sc[f'{column}'])


# TODO Сначала degree=2 для train
train_poly2 = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly2 = train_poly2.fit_transform(X_train_ext)
print(X_train_poly2.shape)


# TODO Затем degree=2 для test
test_poly2 = PolynomialFeatures(degree=2, include_bias=False)
X_test_poly2 = test_poly2.fit_transform(X_test_ext)
print(X_train_poly2.shape)


print(X_train_cube.shape)
print(X_train_log.shape)
print(X_test_cube.shape)
print(X_test_log.shape)


# TODO Объединить X_train_poly2 + X_train_cube + X_train_log
X_train_combined = np.hstack([X_train_poly2, X_train_cube, X_train_log])


# TODO То же самое с train
X_test_combined = np.hstack([X_test_poly2, X_test_cube, X_test_log])


print(X_train_combined.shape)
print(X_test_combined.shape)







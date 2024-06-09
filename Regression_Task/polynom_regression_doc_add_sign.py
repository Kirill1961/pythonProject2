import numpy as np
from sklearn.preprocessing import PolynomialFeatures
X = np.arange(6).reshape(3, 2)
print(X)
poly = PolynomialFeatures(2)
add_signs = poly.fit_transform(X)
print(add_signs, "Добавление признаков полином 2-й степени")  # Добавление признаков
"""    array([[ 1.,  0.,  1.,  0.,  0.,  1.],
           [ 1.,  2.,  3.,  4.,  6.,  9.],
           [ 1.,  4.,  5., 16., 20., 25.]])"""
poly = PolynomialFeatures(interaction_only=True)
add_signs_next = poly.fit_transform(X)  # Добавление признаков 2, надо разобраться с interaction_only=True
print(add_signs_next, "Добавление признаков , надо разобраться с interaction_only=True")
"""    array([[ 1.,  0.,  1.,  0.],
           [ 1.,  2.,  3.,  6.],
           [ 1.,  4.,  5., 20.]])"""
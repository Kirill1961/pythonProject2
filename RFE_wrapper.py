from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

'''
* RFE перебирает разные комбинации признаков.

* На каждом шаге обучает модель (LogisticRegression) на подмножестве признаков.

* Оценивает качество модели и удаляет наименее важные признаки.

* Повторяет до тех пор, пока не останется нужное число признаков.
'''

# Загружаем данные
X, y = load_iris(return_X_y=True)

# Модель, которую "обернём"
model = LogisticRegression(max_iter=1000)

# Обёртка — передаём модель внутрь RFE
selector = RFE(estimator=model, n_features_to_select=2)

# Запускаем отбор признаков
selector = selector.fit(X, y)

# Выводим, какие признаки выбраны
print('True — признак выбран, False — нет :', '\n', f'{selector.support_}', '\n')  # True — признак выбран, False — нет
print('1 — выбран, 2 и выше — не выбран :', '\n', f'{selector.ranking_}')  # 1 — выбран, 2 и выше — не выбран

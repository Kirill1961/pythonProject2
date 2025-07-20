from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Загружаем датасет
iris = load_iris()
X = iris.data              # признаки (4 признака)
y = iris.target            # целевая переменная (0, 1, 2)

# Делим на обучающую и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

# Обучаем модель мультиномиальной логистической регрессии
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train, y_train)

# Предсказания
y_pred = model.predict(X_test)

# Оценка результатов
print("Отчёт по классификации:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# --- 1. Истинная функция ---
def true_function(x):
    return np.sin(2 * np.pi * x)

# --- 2. Генерация данных ---
np.random.seed(42)
n_train = 15
n_test = 100
x_test = np.linspace(0, 1, n_test).reshape(-1, 1)
y_true = true_function(x_test)

# --- 3. Тренировка моделей на разных сэмплах ---
def fit_and_predict(model, n_trials=50):
    preds = []
    for _ in range(n_trials):
        x_train = np.random.rand(n_train, 1)
        y_train = true_function(x_train) + np.random.normal(scale=0.3, size=x_train.shape)
        model.fit(x_train, y_train.ravel())
        preds.append(model.predict(x_test))
    return np.array(preds)

# Линейная модель (высокий bias)
lin_model = LinearRegression()
preds_lin = fit_and_predict(lin_model)

# Полином 10-й степени (высокий variance)
poly_model = make_pipeline(PolynomialFeatures(10), LinearRegression())
preds_poly = fit_and_predict(poly_model)

# --- 4. Визуализация ---
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

for ax, preds, title in zip(axs, [preds_lin, preds_poly], ["Linear regression", "10th degree polynomial"]):
    ax.plot(x_test, y_true, "k--", label="True function")
    ax.plot(x_test, preds.mean(axis=0), "r", label="Mean prediction")
    ax.fill_between(x_test.ravel(),
                    preds.mean(axis=0) - preds.std(axis=0),
                    preds.mean(axis=0) + preds.std(axis=0),
                    color="r", alpha=0.2, label="Variance")
    ax.set_title(title)
    ax.legend()

plt.show()

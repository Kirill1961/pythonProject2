import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import norm


def measure(n):
    "Measurement model, return two coupled measurements."
    m1 = np.random.normal(size=n)
    m2 = np.random.normal(scale=0.5, size=n)

    return m1+m2, m1-m2
m1, m2 = measure(2000)
xmin = m1.min()
xmax = m1.max()
ymin = m2.min()
ymax = m2.max()

print(xmax, xmin)
print(ymax, ymin)

# Выполните оценку плотности ядра по данным
X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])
values = np.vstack([m1, m2])
kernel = stats.gaussian_kde(values)
Z = np.reshape(kernel(positions).T, X.shape)

# Постройте график результатов

fig, ax = plt.subplots()
ax.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r,
          extent=[xmin, xmax, ymin, ymax])
ax.plot(m1, m2, 'k.', markersize=2)
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
# plt.show()


# TODO Генератор dataset
mu, sigma = 5, 2  # Среднее и стандартное отклонение
data_int = np.round(norm.rvs(loc=mu, scale=sigma, size=20)).astype(int)

print(data_int[:10])


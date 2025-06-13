import pandas as pd
import seaborn as sns

from scipy import stats

# anova model from formula
from statsmodels.formula.api import ols

# anova table from ols model
from statsmodels.stats.anova import anova_lm

# for qqplot
import statsmodels.api as sm

# tukey test
from statsmodels.stats.multicomp import pairwise_tukeyhsd

from statsmodels.graphics.gofplots import qqplot

# TODO index_col=0 - Убрали лишнюю колонку с индексами
data = pd.read_csv("D:\Eduson_data\Customer Segmentation.csv", index_col=0)
print(data.head())

data.info()

# удаляем наблюдения с пропущенными значениями
data = data[data.Graduated.isna() != True]

sns.boxplot(data=data, x="Segmentation", y="Age", hue="Graduated")

# one-way anova
one_way = ols("Age ~ Segmentation", data).fit()
anova_lm(one_way)

# qq-plot, проверяем нормальность остатков
sm.qqplot(one_way.resid, line="s")

# разделяем данные по сегментам, чтобы провести тест Левена
groups = []
for group_id, group in data.groupby(["Segmentation"]):
    groups.append(group.Age)

# тест Левена
stats.bartlett(*groups)

# апостериорный анализ
print(pairwise_tukeyhsd(endog=data.Age, groups=data.Segmentation, alpha=0.05))

# two-way anova
two_way = ols("Age ~ Segmentation + Graduated + Segmentation:Graduated", data).fit()
anova_lm(two_way)

# qq-plot, проверяем нормальность остатков
sm.qqplot(two_way.resid, line="s")

# разделяем данные по сегментам и образованию, чтобы провести тест Левена
groups = []
for group_id, group in data.groupby(["Segmentation", "Graduated"]):
    groups.append(group.Age)

# тест Левена
stats.bartlett(*groups)

# апостериорный анализ
data["combination"] = data.Segmentation + "/" + data.Graduated
print(
    pairwise_tukeyhsd(
        endog=data.Age.astype("float"), groups=data.combination, alpha=0.05
    )
)

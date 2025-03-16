import seaborn as sns
import matplotlib.pyplot as plt

# TODO  Выводит список доступных датасетов
print(sns.get_dataset_names())


# TODO Загрузка данных из dataset
data = sns.load_dataset("tips")

print(data)

# TODO Построение boxplot
fig, ax = plt.subplots(figsize=(3, 3))  # Least size

# Построение boxplot
sns.boxplot(x="day", y="total_bill", data=data)

# Отображение графика
plt.show()
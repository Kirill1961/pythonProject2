import csv
from ydata_profiling import ProfileReport
# from pandas_profiling import ProfileReport
import numpy as np
import pandas as pd
print(pd.__version__)

# TODO Читаем файл heart.csv по указанному пути
puth = 'D:\Eduson_data\heart.csv'

# df = pd.read_csv(puth)
# print(df.head(5))


df = pd.DataFrame(
    np.random.rand(4, 3),
    columns=['a', 'b', 'c']
)

profile = ProfileReport(df, title='Pandas ProfileReport')
profile
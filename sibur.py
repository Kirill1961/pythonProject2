import numpy as np
import pandas as pd

data = pd.read_csv('D:\Eduson_data\sample_submission.csv')

print(data.head())

dtm = pd.to_datetime(['2020-04-01', '2020-05-01'])

print(dtm[0])
import pandas as pd
import umap
import umap.plot

from numba.core.errors import NumbaWarning
import warnings


# TODO отключение предупреждения Numba - НЕ работает
warnings.filterwarnings("ignore", category=NumbaWarning)


# Used to get the data
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Some plotting libraries
import matplotlib.pyplot as plt

# from bokeh.plotting import show, save, output_notebook, output_file
# from bokeh.resources import INLINE
# output_notebook(resources=INLINE)


dataset = fetch_20newsgroups(subset='all',
                             shuffle=True, random_state=42)

print(dataset.target_names)

print(f'{len(dataset.data)} documents')
print(f'{len(dataset.target_names)} categories')

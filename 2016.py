import pandas as pd
from sklearn.manifold import TSNE
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('max_columns', None)
tahun = "tenPn13aggloSINGLE"
nama = tahun + '.csv'
nama2 = tahun + 'Py.csv'
df = pd.read_csv(nama)
desc = df.describe()
for i in range(len(df['clusters'].unique())):
    desc2 = df.loc[df['clusters'] == i]
    res = desc2.describe()
    desc = desc.append(res)
desc.to_csv(nama2)

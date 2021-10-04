import pandas as pd
from sklearn.manifold import TSNE
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

pd.set_option('max_columns', None)
tahun = "tenPn13Kmeans"
nama = tahun + '.csv'
nama2 = tahun + 'Py.csv'
df = pd.read_csv(nama)
cats = [c for c in df.columns if df[c].dtypes == 'object']
for col in cats:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))

df['Illness_Severity'] = -1 * (df['Illness_Severity'] - 2)
le = LabelEncoder()
df.Stay_Days = le.fit_transform(df.Stay_Days.astype(str))
le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
desc = df.describe()
for i in range(len(df['clusters'].unique())):
    desc2 = df.loc[df['clusters'] == i]
    res = desc2.describe()
    desc = desc.append(res)
desc.to_csv(nama2)

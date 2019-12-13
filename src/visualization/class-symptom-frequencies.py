import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

DATA_PATH = os.path.join('..','..','data','processed')
FIGURES_PATH = os.path.join('..','..','reports','figures')

df = pd.read_csv(os.path.join(DATA_PATH,'class-symptom-frequency.csv'), index_col=0)

'''
fig = plt.figure()
ax = fig.add_subplot(111)
sns.heatmap(df,ax=ax)
sns.despine(offset=10)
'''


print df.corr()
g = sns.clustermap(df.corr().fillna(0), mask= df.corr().isna(), cmap="bone_r")
plt.savefig(os.path.join(FIGURES_PATH,'class-symptom-clustering.png'),
	dpi=400,bbox_inches="tight")
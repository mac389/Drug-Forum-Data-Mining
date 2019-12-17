import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

DATA_PATH = os.path.join('..','..','data','processed')
FIGURES_PATH = os.path.join('..','..','reports','figures')
df = pd.read_csv(os.path.join(DATA_PATH,'class-class-frequency.csv'), index_col=0)

print df 

'''
print df.corr()
g = sns.clustermap(df.corr().fillna(0), mask= df.corr().isna(), cmap="bone_r")
plt.savefig(os.path.join(FIGURES_PATH,'class-class-clustering.png'),
	dpi=400,bbox_inches="tight")
'''

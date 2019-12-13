import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

DATA_PATH = os.path.join('..','..','data','processed')
FIGURES_PATH = os.path.join('..','..','reports','figures')
df = pd.read_csv(os.path.join(DATA_PATH,'cprobs-pvalues.csv'))

classes = df[df['source']='dd',['prior','marginal','conditional_probability']]
print classes
'''
xcorr = df[''
print df 
print df.corr()
g = sns.clustermap(df.corr().fillna(0), mask= df.corr().isna(), cmap="bone_r")
plt.savefig(os.path.join(FIGURES_PATH,'class-class-cprob-clustering.png'),
	dpi=400,bbox_inches="tight")
	'''
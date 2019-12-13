import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

DATA_PATH = os.path.join('..','..','data','processed')
FIGURES_PATH = os.path.join('..','..','reports','figures')
df = pd.read_csv(os.path.join(DATA_PATH,'cprobs-pvalues.csv'))

classes = df[df['source']=='dd'][['prior','marginal','conditional_probability']]
cprobs = classes.pivot(index='marginal', columns='prior', values='conditional_probability')


g = sns.clustermap(cprobs.fillna(0), mask= cprobs.isna(), cmap="bone_r")
plt.savefig(os.path.join(FIGURES_PATH,'class-class-cprob-clustering.png'),
	dpi=400,bbox_inches="tight")

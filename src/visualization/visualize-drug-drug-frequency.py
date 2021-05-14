import os

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

from collections import Counter 

#df = pd.read_csv(os.path.join('..','..','data','processed','drug-drug-frequency.csv'),index_col=0)
df = pd.read_csv(os.path.join('..','..','data','processed','significant_drug_drug_combinations_after_bh.csv'),
	header=0, index_col=0)

df['should accept'] = df['should accept'].astype(bool)

df[['prior', 'conditional']] = df['name'].str.split('|', 1, expand=True)
grid = df[df['should accept']][['prior','conditional','conditional_probability']]
grid = grid.dropna(subset=['conditional_probability'])
print(grid.sort_values(by='conditional',ascending=False).tail(10))

grid.to_csv(os.path.join(os.path.join('..','..','data','processed','significant_drug_drug_combinations_after_bh-forcytscape.csv')))

grid = df[df['should accept']].pivot(index='prior',columns='conditional',values='conditional_probability')
#print df[df['should accept']].sort(by='conditional_probability',ascending=False)
fig = plt.figure()
ax = fig.add_subplot(111)
ax = sns.heatmap(grid,annot=False, cmap = "bone_r", mask=grid.isnull())
sns.despine(offset=10)
plt.tight_layout()
plt.savefig(os.path.join('..','..','reports','figures','drug-drug-frequency-bh.png'),dpi=400)

import os 
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt 


DATA_PATH = os.path.join('..','..','data','processed')
FIGURES_PATH = os.path.join('..','..','reports','figures')

df = pd.read_csv(os.path.join(DATA_PATH,'cprobs-drugs-acc.csv'),index_col=0)

x =  df[(df['bayes factor']>10)&(df['prior occurence']>30)&(df['marginal occurence']>30)]

#x[x['source']=='ss'].to_csv(os.path.join(DATA_PATH,'ss-significant.csv'),index=False)

print x[x['source']=='sd']
#print x['source'].value_counts()


#sd_df = x[x['source']=='sd'].pivot(index='prior', columns='marginal', values='conditional_probability')
#print sd_df

'''
fig = plt.figure()
ax = fig.add_subplot(111)
cbar_ax = fig.add_axes([.905, .3, .05, .3])
cg = sns.clustermap(sd_df.fillna(0), cmap=plt.cm.bone_r)
cg.ax_row_dendrogram.set_ylim([0,0])
cg.ax_col_dendrogram.set_xlim([0,0])

#plt.tight_layout()
#plt.show()
plt.savefig(os.path.join(FIGURES_PATH,'dd-heatmap.png'),dpi=400,bbox_inches="tight")
'''
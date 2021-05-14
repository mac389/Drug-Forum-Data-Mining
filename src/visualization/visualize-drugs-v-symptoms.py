import os, json 

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np 


#df = pd.DataFrame.from_dict(json.load(open(os.path.join('..','..','data','interim','drugs_symptoms_with_ontology.json'),'r'))
#		,orient='index')


df =pd.read_csv(os.path.join('..','..','data','interim','significant_drug_symptom_combinations_after_bh.csv'), index_col=0)
print(df)
print(df.columns)

df['should accept'] = df['should accept'].astype(bool)

df[['prior', 'conditional']] = df['name'].str.split('|', 1, expand=True)
grid = df[df['adjusted_p_value']>0.95][['prior','conditional','conditional_probability']]
grid = grid.dropna(subset=['conditional_probability'])
#print(grid.sort_values(by='conditional',ascending=False).head(10))
grid = grid.pivot(index='prior',columns='conditional',values='conditional_probability')

#xsns.heatmap(df.corr(method='spearman'),annot=False,cmap="bone_r")
#g = sns.clustermap(df.transpose().corr(method='spearman').fillna(0),annot=False, cmap = "bone_r")
g = sns.clustermap(grid.fillna(0), cmap="bone_r")
g.ax_row_dendrogram.set_visible(False)
g.ax_col_dendrogram.set_visible(False)
g.ax_cbar.set_visible(False)
g.ax_heatmap.xaxis.tick_top() # x axis on top
g.ax_heatmap.xaxis.set_label_position('top')
g.ax_heatmap.set_xticklabels(g.ax_heatmap.get_xticklabels(), rotation=90)
g.ax_heatmap.yaxis.tick_left()
g.ax_heatmap.yaxis.set_label_position('left')
g.ax_heatmap.set_xlabel("")
g.ax_heatmap.set_ylabel("")

#plt.tight_layout()
#plt.show()
g.savefig(os.path.join('..','..','reports','figures','drug-clustermap-bh-2.png'),
	bbox_inches='tight')
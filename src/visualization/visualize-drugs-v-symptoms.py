import os, json 

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np 

from awesome_print import ap 

df = pd.DataFrame.from_dict(json.load(open(os.path.join('..','..','data','interim','drugs_symptoms_with_ontology.json'),'r'))
		,orient='index')

df = np.log(df+1)

#xsns.heatmap(df.corr(method='spearman'),annot=False,cmap="bone_r")
g = sns.clustermap(df.transpose().corr(method='spearman').fillna(0),annot=False, cmap = "bone_r")
plt.tight_layout()
#plt.show()
g.savefig(os.path.join('..','..','reports','figures','drug-clustermap.png'))
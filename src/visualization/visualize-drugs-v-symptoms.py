import os, json 

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np 

from awesome_print import ap 

df = pd.DataFrame.from_dict(json.load(open(os.path.join('..','..','data','interim','drugs_symptoms_with_ontology.json'),'r'))
		,orient='index')

df = np.log(df+1)
g = sns.clustermap(df,annot=False, cmap = "bone_r")
plt.tight_layout()
g.savefig(os.path.join('..','..','reports','figures','drug-symptom-clustermap.png'))
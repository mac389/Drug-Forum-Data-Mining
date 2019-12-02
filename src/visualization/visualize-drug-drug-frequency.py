import os

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

from collections import Counter 

df = pd.read_csv(os.path.join('..','..','data','processed','drug-drug-frequency.csv'),index_col=0)


g = sns.clustermap(df,annot=False, cmap = "bone_r")
g.savefig(os.path.join('..','..','reports','figures','drug-drug-frequency.png'),dpi=400)

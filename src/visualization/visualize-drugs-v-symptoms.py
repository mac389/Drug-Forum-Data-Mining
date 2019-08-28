import os 

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

from awesome_print import ap 

df = pd.read_csv(os.path.join('..','..','data','processed','drugs-v-symptoms.csv'), index_col=0)

sns.heatmap(df.fillna(0),annot=False, cmap = "bone_r")
plt.tight_layout()
plt.show()
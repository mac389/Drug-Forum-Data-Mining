import os 

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

df = pd.read_csv(os.path.join('.','symptomc-class-prevalence-by-drug.csv'))
df_zeroed = df.fillna(0)

sns.heatmap(df_zeroed, annot=True, fmt="d", cmap='viridis')
plt.show()
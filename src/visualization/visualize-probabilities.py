import os

import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DATA_PATH = os.path.join('..','..','data','processed')

fig = plt.figure()
ax = fig.add_subplot(111)

df = pd.read_csv(os.path.join(DATA_PATH,'drug-drug-frequency-pvalues.csv'),index_col=0)
sns.distplot(df['conditional_probability'])
plt.show()
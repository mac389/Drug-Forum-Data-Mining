import json, os 

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 

DATA_PATH = os.path.join('..','..','data','processed')
df = pd.read_json(os.path.join(DATA_PATH,'bayes_factors.json'),orient='columns')
df.replace("null",np.nan,inplace=True)

lst_for = [(col,row,df.loc[col,row]) for col in df.columns.values for row in df.index.values if df.loc[col,row]>6]
with open(os.path.join(DATA_PATH,'bayes-factor-for-alternative.txt'),'w') as fout:
	for line in lst_for:
		fout.write(str(line)+'\n')


lst_against = [(col,row,df.loc[col,row]) for col in df.columns.values for row in df.index.values if df.loc[col,row]<.1]
with open(os.path.join(DATA_PATH,'bayes-factor-against-alternative.txt'),'w') as fout:
	for line in lst_against:
			fout.write(str(line)+'\n')


'''
fig = plt.figure()
ax = fig.add_subplot(111)
sns.heatmap(df, mask=df.to_numpy()<6)
plt.show()
'''
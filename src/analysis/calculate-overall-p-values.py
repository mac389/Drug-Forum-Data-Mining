import os 

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

from scipy.stats import rankdata

DATA_PATH = os.path.join('..','..','data','processed')

filenames = ['symptom-symptom-frequency', 
			 'drug-symptom-frequency',
			 'drug-drug-frequency',
			 'symptom-drug-frequency'] #drug symptoms repeated because p(s|e) neq p(e|s)
 
dfs = [pd.read_csv(os.path.join(DATA_PATH,"%s-pvalues.csv"%filename)) for filename in filenames]
dfs[0]['source'] = "symptom-symptom"
dfs[1]['source'] = "drug-effect"
dfs[2]['source'] = "drug-drug"
dfs[3]['source'] = "effect-drug"

fdr = 0.05
df = pd.concat(dfs)
df.drop(df.columns[0],axis=1,inplace=True)
#df['p_value'] /= 100.

df.sort_values(by='p_value',inplace=True, ascending=True)
df['rank'] = df['p_value'].rank()
print('Calculating CM')
cm = sum(1/i for i in range(1,len(df['rank'])))
print('Calculated')
df['bh_threshold'] = df['rank']/(len(df['rank'])*cm)*fdr
df['should accept'] = df['p_value']<df['bh_threshold']
print(df.head(14)) 
print(df['should accept'].describe())
#nothing is significant because the number of statements are so large. 
#df.to_csv(os.path.join(DATA_PATH,'knowledge-base-as-df.csv'),index=False)
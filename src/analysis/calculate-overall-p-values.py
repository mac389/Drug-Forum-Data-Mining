import os 

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

from statsmodels.stats.multitest import fdrcorrection

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
df['bh_threshold'] = df['rank']/len(df['rank'])*fdr
#sns.scatterplot(data=df['p_value'])
#plt.show()


'''
def fdr(p_vals):
    from scipy.stats import rankdata
    ranked_p_values = rankdata(p_vals)
    fdr = p_vals * len(p_vals) / ranked_p_values
    fdr[fdr > 1] = 1
    return fdr

df['adjusted_p_value'] = fdr(df['p_value'])
print df['adjusted_p_value'].describe()
'''
'''
reject, adjusted_p_value = fdrcorrection(df['p_value'], method='negcorr', alpha=0.05)
df['adjusted_p_value'] = adjusted_p_value
df['should reject'] = reject
'''
print df.head(14) #everything is significant because the number of statements are so large. 
#print df['should reject'].describe()
df.to_csv(os.path.join(DATA_PATH,'knowledge-base-as-df.csv'),index=False)
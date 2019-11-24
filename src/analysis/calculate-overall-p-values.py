import os 

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

from statsmodels.stats.multitest import fdrcorrection

DATA_PATH = os.path.join('..','..','data','interim')

filenames = ['significant_symptom_symptom_combinations_after_bh.csv', 
			'significant_drug_effect_combinations_after_bh.csv',
			'significant_effect_drug_combinations_after_bh.csv']


dfs = [pd.read_csv(os.path.join(DATA_PATH,filename)) for filename in filenames]
dfs[0]['source'] = "symptom-symptoms"
dfs[1]['source'] = "drug-effect"
dfs[2]['source'] = "effect-drug"

df = pd.concat(dfs)
df = df.drop(df.columns[[0,-2,-3]], axis=1)
df.sort_values(by='p_value',inplace=True)

sns.scatterplot(data=df['p_value'])
plt.show()


'''
reject, adjusted_p_value = fdrcorrection(df['p_value'], method='negcorr', alpha=0.05)
df['adjusted_p_value'] = adjusted_p_value
df['should reject'] = reject
print df['should reject'].describe()
'''

#df['fdr'] = df['p_value']/

'''
def fdr(p_vals):

    from scipy.stats import rankdata
    ranked_p_values = rankdata(p_vals)
    fdr = p_vals * len(p_vals) / ranked_p_values
    fdr[fdr > 1] = 1

    return fdr
'''
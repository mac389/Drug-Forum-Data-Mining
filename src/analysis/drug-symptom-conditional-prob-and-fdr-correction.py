import json, os, itertools 

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

from statsmodels.stats.multitest import fdrcorrection
from awesome_print import ap
from scipy.stats import percentileofscore 
from tqdm import tqdm 
from sklearn.utils import resample

df = pd.read_csv(os.path.join('..','..','data','processed','drug-symptom-frequency.csv'),index_col=0)

#df = df.transpose()


def from_occurences_to_conditional_probs(df):
	baseline_probabilities = df.sum(axis=1)/(df.sum(axis=1).sum())
	#print baseline_probabilities
	overall_sum = df.sum().sum()

	conditional_prob_df = df.copy(deep=True)
	conditional_prob_df /= overall_sum
	conditional_prob_df = conditional_prob_df.divide(baseline_probabilities, axis=0)

	return conditional_prob_df


original_pdf = from_occurences_to_conditional_probs(df)


'''
#baseline_chance = df.freq.replace(0,np.nan).mean()/df.freq.sum()

P(effect | drug) = P(effect + drug)/P(drug)

df has (rows x columns) as (drugs,symptoms)

p(drug) => sum over symptoms [not perfect, overcounts]

'''

'''
Create conditional probability DataFrame, formatted as p(effect | drug)

'''



#ap( baseline_probabilities.tolist())
#What to do with baseline probability of zero? (Here setting it to one, just to push through)
'''
Only write Problog goals for statistically significant co-occurrences, adjusted for FDR

'''

#convert matrix to long form
#exclude diagonal
#exclude nonzero entries

data = [("%s|%s"%(col,row),original_pdf.loc[row,col]) 
								 for row in original_pdf.index 
								  for col in original_pdf.columns
								  if row != col]


long_cdf = pd.DataFrame(data,columns=['name','conditional_probability'])
long_cdf = long_cdf[(~long_cdf['conditional_probability'].isna()) & (long_cdf['conditional_probability']!=0)]
long_cdf['percentile'] = long_cdf['conditional_probability'].rank(pct=True)

n = 20
x = []
for _ in tqdm(range(n),'bootstrapping'):
	x += [from_occurences_to_conditional_probs(resample(df)).to_numpy()]

dist = pd.DataFrame(list(itertools.chain.from_iterable(x)))
dist.dropna(inplace=True)
sns.set(color_codes=True)
dist = dist.to_numpy().ravel()


#sns.distplot(dist,hist=False)
#plt.show()

long_cdf['p_value'] = 0.01*long_cdf['conditional_probability'].apply(lambda x: percentileofscore(dist,x))
long_cdf.to_csv(os.path.join('..','..','data','interim','significant_effect_drug_combinations_after_bh.csv'))

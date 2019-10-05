import json, os, itertools 

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

from statsmodels.stats.multitest import fdrcorrection
from awesome_print import ap
from scipy.stats import percentileofscore 
from tqdm import tqdm 

df = pd.read_csv(os.path.join('..','..','data','processed','drug-symptom-frequency.csv'),index_col=0)

'''
#Take overall change of occurrence as average 
#Have to use the accurate numbers, go with this for time now
#baseline_chance = df.freq.replace(0,np.nan).mean()/df.freq.sum()

P(effect | drug) = P(effect + drug)/P(drug)

df has (rows x columns) as (drugs,symptoms)

p(drug) => sum over symptoms [not perfect, overcounts]

'''

baseline_probabilities = df.sum(axis=1)/(df.sum(axis=1).sum())
overall_sum = df.sum().sum()

'''
Create conditional probability DataFrame, formatted as p(effect | drug)

'''

conditional_prob_df = df.copy(deep=True)
conditional_prob_df /= overall_sum
conditional_prob_df = conditional_prob_df.divide(baseline_probabilities, axis=0)

#ap( baseline_probabilities.tolist())
#What to do with baseline probability of zero? (Here setting it to one, just to push through)
'''
Only write Problog goals for statistically significant co-occurrences, adjusted for FDR

'''

#convert matrix to long form
#exclude diagonal
#exclude nonzero entries


data = [("%s|%s"%(row,col),conditional_prob_df.loc[row,col]) 
								 for row in conditional_prob_df.index 
								  for col in conditional_prob_df.columns
								  if row != col]


long_cdf = pd.DataFrame(data,columns=['name','conditional_probability'])
long_cdf = long_cdf[(~long_cdf['conditional_probability'].isna()) & (long_cdf['conditional_probability']!=0)]
long_cdf['percentile'] = long_cdf['conditional_probability'].rank(pct=True)

n = 20
x = []
for _ in tqdm(range(n),'bootstrapping'):
	x += [long_cdf.sample(frac=1).as_matrix(columns=['conditional_probability']).ravel()]

dist = pd.DataFrame(list(itertools.chain.from_iterable(x)))
dist.dropna(inplace=True)


long_cdf['p_value'] = long_cdf['conditional_probability'].apply(lambda x: percentileofscore(x,dist.to_numpy()))
'''
dist.hist(bins=100)
plt.show()
'''
#build distribution


reject, adjusted_p_value = fdrcorrection(long_cdf['p_value'], alpha=0.05)
long_cdf['adjusted_p_value'] = adjusted_p_value
long_cdf['should accept'] = reject
long_cdf.to_csv(os.path.join('..','..','data','interim','significant_drug_symptom_combinations_after_bh.csv'))
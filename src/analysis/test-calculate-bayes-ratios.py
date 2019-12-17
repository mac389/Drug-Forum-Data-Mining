import os, itertools 

import pandas as pd 
import numpy as np 

from tqdm import tqdm 
from sklearn.utils import resample


DATA_PATH = os.path.join('..','..','data','processed')

filenames = ['symptom-symptom-frequency', 
			 'class-symptom-frequency',
			 'class-class-frequency',
			 'symptom-class-frequency'] #class symptoms repeated because p(s|e) neq p(e|s)
 

ss = pd.read_csv(os.path.join(DATA_PATH,'symptom-symptom-frequency.csv'),index_col=0)
ds = pd.read_csv(os.path.join(DATA_PATH,'drug-symptom-frequency.csv'),index_col=0)
dd = pd.read_csv(os.path.join(DATA_PATH,'drug-drug-frequency.csv'),index_col=0)
sd = pd.read_csv(os.path.join(DATA_PATH,'drug-symptom-frequency.csv'),index_col=0).transpose()

df = pd.read_csv(os.path.join(DATA_PATH,'cprobs-drugs.csv'), index_col=0)


#Example for p(vasoactive | integumentary) 9.687189e-07

prior = 'infectious'
marginal = 'emotion'

df = df[(df['prior']!=df['marginal'])]
#print df.loc[(df.prior==prior)&(df.marginal==marginal),'conditional_probability']

'''
Bayes Ratio = p(D|H1)/p(D|H2)

BF = p(vasoactive|integumentary)*p(integumentary)/[p(vasoactive|A)p(A) + ...]

'''

'''
numerator =  df.loc[(df.prior==prior)&(df.marginal==marginal),'conditional_probability'].values / df.loc[(df.prior==marginal),'prior_probability'].head(1).values
marginals =  df.loc[df.prior==prior,'marginal'].values
denominator = 1

for marginal in tqdm(marginals,'Marginals'):
	if marginal != 'emotion':
		denominator -= df.loc[(df.prior==prior)&(df.marginal==marginal),'conditional_probability'].values[0] * df.loc[(df.prior==marginal),'prior_probability'].head(1).values[0]
'''

df['bayes factor'] = df['conditional_probability']/df['prior_probability']

'''
for prior in tqdm(df.prior.unique()):
	for marginal in tqdm(df.marginal.unique()):
		numerator = df.loc[(df.prior==prior)&(df.marginal==marginal),'conditional_probability'].head(1)
		denominator = df.loc[df.prior==prior,'prior_probability'].head(1)
		BF = numerator.values/denominator.values
		df.loc[(df.prior==prior)&(df.marginal==marginal),'bayes factor'] = BF
'''
df.to_csv(os.path.join(DATA_PATH,'crpobs-bayes-factor-drugs.csv'))
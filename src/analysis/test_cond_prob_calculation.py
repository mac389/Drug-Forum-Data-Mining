import os 

import numpy as np 
import pandas as pd

DATA_PATH = os.path.join('..','..','data','processed')
df = pd.read_csv(os.path.join(DATA_PATH,'drug-symptom-frequency.csv'), index_col=0)

ss = pd.read_csv(os.path.join(DATA_PATH,'drug-drug-frequency.csv'), index_col=0)

dd = pd.read_csv(os.path.join(DATA_PATH,'symptom-symptom-frequency.csv'), index_col=0)
#print dd['emotion'].max()/float(dd.max(axis=1).sum())
#print df['cobalt'].nonzero()

def from_occurences_to_conditional_probs(df, mode='symmetric'):
	'''
	rows contain variable conditioning on p(col | row)
	p (col | row) = p(col,row)/p(row)
	'''

	if mode == 'symmetric': # drug-drug or symptom-symptom
		b = df.max(axis=1) 
		b /= b.sum() # this represents p(b)

		overall_sum = np.diag(df.to_numpy()).sum() #this is the denominator for p(a & b)

	elif mode == 'cross':
		b = df.sum(axis=1)/(df.sum(axis=1).sum())
		overall_sum = df.sum().sum()

	conditional_prob_df = df.copy(deep=True)
	conditional_prob_df /= overall_sum # the quotient is p(a & b)
	conditional_prob_df = conditional_prob_df.divide(b, axis=0) # this is p(a & b)/p(b)

	return conditional_prob_df

x = from_occurences_to_conditional_probs(ss)
df1 = x.stack().rename_axis(('other','prior')).reset_index(name='probability')

#print (df1[df1['prior']=='emotion']['probability'].to_numpy()*np.diag(ss.to_numpy())/np.diag(ss.to_numpy()).sum())

#Test law of probability
term = 'acetaminophen'
cobalt = x[term].dropna()
marginals = ss.max(axis=1)
marginals /= marginals.sum()
print marginals
lop = 0
for label in cobalt.index:
	if label != term:
		lop += cobalt[label]*marginals[label]
print lop
print marginals[term]

'''
df3 = df1[df1['prior']=='emotion'].copy(deep=True)
freq = ss.max(axis=1)/ss.max(axis=1).sum()
df3['marginals']= freq[df3['other'].values].values

print (df3['marginals']*df3['probability']).sum()
'''
'''
P(A | B) = P(A,B)/P(B)

'''
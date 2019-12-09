import os, itertools 

import pandas as pd 
import numpy as np 

from tqdm import tqdm 
from sklearn.utils import resample


DATA_PATH = os.path.join('..','..','data','processed')

filenames = ['symptom-symptom-frequency', 
			 'drug-symptom-frequency',
			 'drug-drug-frequency',
			 'symptom-drug-frequency'] #drug symptoms repeated because p(s|e) neq p(e|s)
 

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

ds_count = 0
for filename in tqdm(filenames,'Each File'): 
	if filename == 'symptom-drug-frequency':
		df = pd.read_csv(os.path.join(DATA_PATH,'drug-symptom-frequency.csv'),index_col=0)
		df = df.transpose()
	else:
		df = pd.read_csv(os.path.join(DATA_PATH,'%s.csv'%filename),index_col=0)

	dfx = df.copy(deep=True)
	mode = 'symmetric' if ('drug' not in filename and 'symptom' not in filename) else 'cross'
	dfx = from_occurences_to_conditional_probs(df, mode=mode)
	data = [("%s|%s"%(col,row),dfx.loc[row,col]) 
				for row in dfx.index for col in dfx.columns if row != col]


	p_values = pd.DataFrame(data,columns=['name','conditional_probability'])
	p_values = p_values[(~p_values['conditional_probability'].isna()) & (p_values['conditional_probability']!=0)]
	p_values['percentile'] = p_values['conditional_probability'].rank(pct=True)

	n = 1000 #number of times to resample
	x = []
	for _ in tqdm(range(n),'bootstrapping'):
		x += [from_occurences_to_conditional_probs(resample(df), mode=mode).to_numpy()]

	dist = pd.DataFrame(list(itertools.chain.from_iterable(x)))
	dist.dropna(inplace=True)
	dist = dist.to_numpy().ravel()

	p_values['p_value'] = p_values['conditional_probability'].apply(lambda x: (p_values['conditional_probability']>=x).sum())
	p_values['p_value'] /= float(len(p_values['p_value']))
	#pval = sum(s >= s0)/N

	p_values.to_csv(os.path.join(DATA_PATH,'%s-pvalues.csv'%(filename)))
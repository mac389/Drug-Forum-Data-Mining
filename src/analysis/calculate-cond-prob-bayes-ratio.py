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

drugs = dd.index.unique().tolist()
symptoms = ss.index.unique().tolist()
print (len(drugs)+len(symptoms))**2
def from_occurences_to_conditional_probs(arrs):
	'''
	rows contain variable conditioning on p(col | row)
	p (col | row) = p(col,row)/p(row)
	'''
	ans = {key:pd.DataFrame(0,index=value.index,columns=value.columns) 
			for key,value in arrs.items()}
	exceptions = []
	for prior, marginal in tqdm(itertools.product(drugs+symptoms,repeat=2),'Arr'):
		#calculate conditional probability the inefficient way

		#P(prior,marginal)/P(marginal)

		#print 'Marginal %s, Prior %s'%(marginal,prior)

		if prior != marginal:
			if prior in drugs:
				if marginal in drugs: #Drug-Drug
					p__a_and_b = dd.loc[prior,marginal]
					p__b = float(dd.loc[marginal,:].sum())
					switch = 'dd'	
				elif marginal in symptoms: #Drug-Symptom
					p__a_and_b = ds.loc[prior,marginal]
					p__b = float(ds.loc[:,marginal].sum())
					switch = 'ds'
			elif prior in symptoms:
				if marginal in drugs: #Symptom-Drug
					p__a_and_b = sd.loc[prior,marginal]
					p__b = float(sd.loc[:,marginal].sum())
					switch = 'sd'
				elif marginal in symptoms: #Symptom-Symptom
					switch = 'ss'
					p__a_and_b = ss.loc[marginal,prior]
					p__b = float(ss.loc[marginal,:].sum())
		
			conditional_probability = p__a_and_b/p__b if p__b > 0 else np.nan
			

			'''
			print '----------'
			print conditional_probability
			print p__a_and_b,prior,marginal
			print p__b,marginal
			print '===========\n'
			'''

			ans[switch].loc[prior,marginal] = conditional_probability

	return ans,exceptions

#Initial conditional probability
arr =  {'ds':ds,'dd':dd,'sd':sd,'ss':ss}
cprobs,_ = from_occurences_to_conditional_probs(arr)

data = pd.DataFrame([[row,col,df.loc[row,col],source] 
		for source,df in cprobs.items()
		for row in df.index for col in df.columns], 
		columns=['prior','marginal','conditional_probability','source'])

data = data.dropna()
ss_sum = float(ss.sum().sum())
dd_sum = float(dd.sum().sum())

def unconditional_probability(name):
	if name in dd.index:
		return dd.loc[name,:].sum()/dd_sum
	elif name in ss.index:
		return ss.loc[name,:].sum()/ss_sum

def occurs(name):
	if name in dd.index:
		return dd.loc[name,:].sum()
	elif name in ss.index:
		return ss.loc[name,:].sum()
	else:
		return np.nan

prior_occurs = data['prior'].value_counts()
marginal_occurs = data['marginal'].value_counts()
data['prior_probability'] = data['prior'].apply(unconditional_probability)
data['marginal_probability'] = data['marginal'].apply(unconditional_probability)
data['prior occurence'] = data['prior'].apply(occurs)
data['marginal occurence'] = data['marginal'].apply(occurs)
data['bayes factor'] = data['conditional_probability']/data['prior_probability']
#data['bayes factor'] *= (data['prior occurence'] - data['marginal occurence']).abs().divide(data['prior occurence'])
data.sort_values(by='bayes factor',ascending=False, inplace=True)

'''
data['percentile'] = data['conditional_probability'].rank(pct=True)
data['p_value'] = data['conditional_probability'].apply(lambda x: (data['conditional_probability']>=x).sum())
data['p_value'] /= float(len(data['p_value']))

data['bh_thresh'] = data['conditional_probability'].rank()
data['bh_thresh'] *= fdr 
data['bh_thresh'] /= len(data)

data['bayes ratio'] = [row['conditional_probability']/unconditional_probability(row['prior']) for _,row in data.iterrows()]
data.sort_values(by='p_value',ascending=True, inplace=True)
'''
#print data
#pval = sum(s >= s0)/N
data.to_csv(os.path.join(DATA_PATH,'cprobs-drugs-acc.csv'))


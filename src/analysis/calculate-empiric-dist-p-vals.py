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
ds = pd.read_csv(os.path.join(DATA_PATH,'class-symptom-frequency.csv'),index_col=0)
dd = pd.read_csv(os.path.join(DATA_PATH,'class-class-frequency.csv'),index_col=0)
sd = pd.read_csv(os.path.join(DATA_PATH,'symptom-class-frequency.csv'),index_col=0)

def from_occurences_to_conditional_probs(arrs):

	dd_diag = np.diag(arrs['dd']).sum().astype(float)
	ss_diag = np.diag(arrs['ss']).sum().astype(float)

	drugs = arrs['dd'].index.unique().tolist()
	symptoms = arrs['ss'].index.unique().tolist()
	'''
	rows contain variable conditioning on p(col | row)
	p (col | row) = p(col,row)/p(row)
	'''
	ans = {key:pd.DataFrame(0,index=value.index,columns=value.columns) 
			for key,value in arrs.items()}
	exceptions = []
	for prior, marginal in itertools.product(drugs+symptoms,repeat=2):
		#calculate conditional probability the inefficient way

		#P(prior,marginal)/P(marginal)

		#print 'Marginal %s, Prior %s'%(marginal,prior)

		if prior != marginal:
			if prior in drugs:
				if marginal in drugs: #Drug-Drug
					p__a_and_b = arrs['dd'].loc[marginal,prior]/(dd_diag*dd_diag)
					p__b = arrs['dd'].loc[marginal,marginal]/dd_diag
					#unconditional_probability[prior] = dd.loc[prior][prior]/(dd_diag)
					switch = 'dd'	
				elif marginal in symptoms: #Drug-Symptom
					p__a_and_b = arrs['sd'].loc[marginal,prior]/(dd_diag*ss_diag)
					p__b = arrs['ss'].loc[marginal,marginal]/ss_diag
					switch = 'sd'
				else:
					exceptions += [(marginal,'marginal not in drugs or symptoms')]
					switch='error'
			elif prior in symptoms:
				if marginal in drugs: #Symptom-Drug
					p__a_and_b = arrs['ds'].loc[marginal,prior]/(dd_diag*ss_diag)
					p__b = ans['dd'].loc[marginal,marginal]/dd_diag
					switch = 'ds'
				elif marginal in symptoms: #Symptom-Symptom
					switch = 'ss'
					p__a_and_b = arrs['ss'].loc[marginal,prior]/(ss_diag*ss_diag)
					p__b = arrs['ss'].loc[marginal,marginal]/ss_diag
				else:
					exceptions += [(marginal,'marginal not in drugs or symptoms')]
			else:
				exceptions += [(prior,'prior not in drugs or symptoms')]
		
			conditional_probability = p__a_and_b/p__b if p__b > 0 else np.nan

			ans[switch][prior][marginal] = conditional_probability

	return ans,exceptions

#Initial conditional probability
arr =  {'ds':ds,'dd':dd,'sd':sd,'ss':ss}
cprobs,_ = from_occurences_to_conditional_probs(arr)
data = pd.DataFrame([[col,row,df.loc[row,col],source] 
		for source,df in cprobs.items()
		for row in df.index for col in df.columns], 
		columns=['prior','marginal','conditional_probability','source'])

data = data.dropna()

def unconditional_probability(name):
	if name in dd.index:
		return dd.loc[name,name]/np.diag(dd).sum().astype(float)
	elif name in ss.index:
		return ss.loc[name,name]/np.diag(ss).sum().astype(float)

all_exceptions = []
n = 2
x = [] 
for _ in tqdm(range(n),'bootstrapping'):

	'''
	ss1 = pd.DataFrame(resample(ss.to_numpy()),index=ss.index,columns=ss.columns)
	dd1 = pd.DataFrame(resample(dd.to_numpy()),index=dd.index,columns=dd.columns)
	ds1 = pd.DataFrame(resample(ds.to_numpy()),index=ds.index,columns=ds.columns)
	sd1 = pd.DataFrame(resample(sd.to_numpy()),index=sd.index,columns=sd.columns)
	'''

	ss1 = ss.sample(frac=1).transpose().sample(frac=1)
	dd1 = dd.sample(frac=1).transpose().sample(frac=1)
	sd1 = sd.sample(frac=1).transpose().sample(frac=1)
	ds1 = ds.sample(frac=1).transpose().sample(frac=1)

	arrs,exceptions = from_occurences_to_conditional_probs({'ds':ds1,'dd':dd1,'sd':sd1,'ss':ss1})
 	x += [arr.to_numpy().flatten() for arr in arrs.values()]
 	all_exceptions += exceptions

x = np.concatenate(x)
x = x[~np.isnan(x)]

all_exceptions = list(itertools.chain.from_iterable(all_exceptions))
if len(all_exceptions) > 0:
	print all_exceptions
else:
	print 'No exceptions'

fdr = 0.05
data['percentile'] = data['conditional_probability'].rank(pct=True)
data['p_value'] = data['conditional_probability'].apply(lambda x: (data['conditional_probability']>=x).sum())
data['p_value'] /= float(len(data['p_value']))

data['bh_thresh'] = data['conditional_probability'].rank()
data['bh_thresh'] *= fdr 
data['bh_thresh'] /= len(data)

data['bayes ratio'] = [row['conditional_probability']/unconditional_probability(row['prior']) for _,row in data.iterrows()]
data.sort_values(by='bayes ratio',ascending=False, inplace=True)
print data
#pval = sum(s >= s0)/N
data.to_csv(os.path.join(DATA_PATH,'cprobs-pvalues.csv'%(filename)))


import os 

import pandas as pd 

DATA_PATH = os.path.join('..','..','data','processed')

filenames = ['symptom-symptom-frequency', 
			 'drug-symptom-frequency',
			 'drug-drug-frequency',
			 'symptom-drug-frequency'] #drug symptoms repeated because p(s|e) neq p(e|s)
 

def from_occurences_to_conditional_probs(df):
	baseline_probabilities = df.sum(axis=1)/(df.sum(axis=1).sum())
	#print baseline_probabilities
	overall_sum = df.sum().sum()

	conditional_prob_df = df.copy(deep=True)
	conditional_prob_df /= overall_sum
	conditional_prob_df = conditional_prob_df.divide(baseline_probabilities, axis=0)

	return conditional_prob_df

ds_count = 0
for filename in filenames: 
	if filename == 'symptom-drug-frequency':
		ds_count += 1
		df = pd.read_csv(os.path.join(DATA_PATH,'drug-symptom-frequency.csv'),index_col=0)
		df = df.transpose()
	else:
		df = pd.read_csv(os.path.join(DATA_PATH,'%s.csv'%filename),index_col=0)

	
	data = [("%s|%s"%(col,row),df.loc[row,col]) 
				for row in df.index 
				for col in df.columns
				if row != col]


	p_values = pd.DataFrame(data,columns=['name','conditional_probability'])
	 = p_values[(~p_values['conditional_probability'].isna()) & (p_values['conditisonal_probability']!=0)]
	p_values['percentile'] = p_values['conditional_probability'].rank(pct=True)

	n = 1000 #number of times to resample
	x = []
	for _ in tqdm(range(n),'bootstrapping'):
		x += [from_occurences_to_conditional_probs(resample(df)).to_numpy()]

	dist = pd.DataFrame(list(itertools.chain.from_iterable(x)))
	dist.dropna(inplace=True)
	sns.set(color_codes=True)
	dist = dist.to_numpy().ravel()

	p_values['p_value'] = p_values['conditional_probability'].apply(lambda x: p_values.loc[p_values['conditional_probability']>=x]['conditional_probability'].sum())
	p_values['p_value'] /= float(len(p_values['p_value']))
	#pval = sum(s >= s0)/N

	p_values.to_csv(os.path.join(DATA_PATH,'%-pvalues.csv'%(filename)))
import os

import pandas as pd 

DATA_PATH = os.path.join('..','..','data','processed')


signatures = {'symptom-drug':'effect_substance',
	'drug-drug':'substance_substance',
	'drug-symptom':'substance_effect',
	'symptom-symptom':'effect_effect'}

def make_function(aRow, source):
	prob = aRow['conditional_probability']
	s1,s2 = aRow['name'].split('|')
	s1 = s1.replace(' ','_').lower()
	s2 = s2.replace(' ','_').lower()
	head = signatures[source]

	return """%.04f::%s(%s,%s)."""%(prob,head,s1,s2)

with open(os.path.join('..','..','data','processed','kb.txt'),'w') as fout:
	for filename in os.listdir(DATA_PATH):
		if filename.endswith('-pvalues.csv'):
			source,_ = filename.split('-frequency-pvalues.csv')
			df = pd.read_csv(os.path.join(DATA_PATH,filename))
			for _,row in df[df['p_value']<0.01].iterrows():
				print>>fout,make_function(row,source)

		#print>>fout, coingestants%(row['conditional_probability'],one.replace(' ','_'),two.replace(' ','_'))



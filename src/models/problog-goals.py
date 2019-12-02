import os

import pandas as pd 

DATA_PATH = os.path.join('..','..','data','processed')
df = pd.read_csv(os.path.join(DATA_PATH,'knowledge-base-as-df.csv'))
coingestants = """%.04f::comanifests(1,%s,%s)."""

signatures = {'effect-drug':'effect_substance',
	'drug-drug':'substance_substance',
	'drug-effect':'substance_effect',
	'effect-effect':'substance_substance',
	'symptom-symptom':'effect_effect'}

def make_function(aRow):
	prob = aRow['p_value']
	s1,s2 = aRow['name'].split('|')
	head = signatures[aRow['source']]

	return """%.04f::%s(X,%s,%s)."""%(prob,head,s1,s2)


with open(os.path.join('..','..','data','processed','symptom-symptom--kb.txt'),'w') as fout:
	for _,row in df[df['p_value']<0.05].iterrows():
		print make_function(row)

		#print>>fout, coingestants%(row['conditional_probability'],one.replace(' ','_'),two.replace(' ','_'))

	print>>fout,'%%%%%%%%%%%%%%%%%%'


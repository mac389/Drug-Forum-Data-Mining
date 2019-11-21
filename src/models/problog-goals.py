
import os

import pandas as pd 


DATA_PATH = os.path.join('..','..','data')
df = pd.read_csv(os.path.join(DATA_PATH,'processed','significant_symptom_symptom_combinations_after_bh.csv'), index_col=0)

for_goals = df[df['should accept'] == True]

coingestants = """%.04f::comanifests(1,%s,%s)."""

with open(os.path.join('..','..','data','processed','symptom-symptom--kb.txt'),'w') as fout:
	for _,row in for_goals.iterrows():
		one,two = row['name'].split('|') #DataFrame stores P(one | two)

		print>>fout, coingestants%(row['conditional_probability'],one.replace(' ','_'),two.replace(' ','_'))

	print>>fout,'%%%%%%%%%%%%%%%%%%'


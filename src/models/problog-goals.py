
import os

import pandas as pd 


DATA_PATH = os.path.join('..','..','data')
df = pd.read_csv(os.path.join(DATA_PATH,'processed','significant_drug_drug_combinations_after_bh.csv'), index_col=0)

for_goals = df[df['should accept'] == True]

coingestants = """%.04f::ingested(1,%s,%s)."""

with open(os.path.join('..','..','data','processed','for-problog.txt'),'w') as fout:
	for _,row in for_goals.iterrows():
		one,two = row['name'].split('|') #DataFrame stores P(one | two)

		print>>fout, coingestants%(row['conditional_probability'],one,two)

	print>>fout,'%%%%%%%%%%%%%%%%%%'

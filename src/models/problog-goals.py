
import os

import pandas as pd 


df = pd.read_csv(os.path.join(DATA_PATH,'processed','significan_drug_drug_combinations_after_bh'), index_col=0)

for_goals = df[df['should accept'] == True]

coingestants = """%.04f::also_ingested(X,%s) :-
				person(X),
				substance_ingested(X,%s)"""

with open(os.path.join('..','..','data','processed','for-problog.txt'),'w') as fout:
	for row in  for_goals.index
		for col in for_goals.columns:
			
			

	print>>fout,'%%%%%%%%%%%%%%%%%%'
'''

coingestants = """%.04f::also_ingested(X,%s) :-
                    person(X),
                    substance_ingested(X,%s)"""


import os, json, itertools 

from collections import defaultdict
from tqdm import tqdm 

import pandas as pd 

DATA_PATH = os.path.join('..','..','data')

db = json.load(open(os.path.join(DATA_PATH,'lycaeum-forum-processed-has-drug-names.json'),'r'))

spelling_ontology = json.load(open(os.path.join(DATA_PATH,'processed','spelling-ontology.json'),'r'))
list_of_drugs = spelling_ontology.keys()


df = pd.DataFrame(0,index=spelling_ontology.values(),columns=spelling_ontology.values())

for drug_one,drug_two in tqdm(itertools.combinations(spelling_ontology.keys(),2),"building index"):
	print drug_two,drug_one,'llll'
	for title,entry in db.items():
		if (drug_one in entry['text'] or drug_one in entry['drugs']) and (drug_two in entry['text'] or drug_two in entry['drugs']):
			df.loc[drug_one,drug_two] = 1 

'''
df = pd.DataFrame.from_dict(drug_index,orient='index')
df = df.astype(bool).astype(int)
'''

df.to_csv(os.path.join(DATA_PATH,'interim','drug-drug-frequency.csv'))
print df 
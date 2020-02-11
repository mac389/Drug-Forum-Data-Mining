import json, os

import pandas as pd 

from tqdm import tqdm 

DATA_PATH = os.path.join('..','..','data')

#convert nested json into an array that is more MongoDB friendly

db  = json.load(open(os.path.join(DATA_PATH,'processed','bayes_factors.json'),'r'))
df = pd.read_csv(os.path.join(DATA_PATH,'processed','drugs-v-symptoms.csv'),index_col=0)
symptoms = df.columns.tolist()
drugs = df.index.tolist()

taxonomy = json.load(open(os.path.join(DATA_PATH,'processed','drug-name-hierarchy.json'),'r'))
taxonomy_trans_table = {drug_name:drug_class for drug_class in taxonomy 
										for drug_name in taxonomy[drug_class].keys()}
		

'''
Annotations
  1. Type (substance or effect)
  2. Class 

'''

db2 = []
for key, value in tqdm(db.items()):
	for second,ratio in db[key].items():
		db2 += [{'prior':key,
				 'conditional':second,
				 'bayes ratio':ratio,
				 'prior_type': 'substance' if key in taxonomy_trans_table else 'symptom',
				 'conditional_type': 'substance' if second in taxonomy_trans_table else 'symptom',
				 'prior_class': taxonomy_trans_table[key] if key in taxonomy_trans_table else key,
				 'conditional_class':taxonomy_trans_table[second] if second in taxonomy_trans_table else key}]

json.dump(db2,open(os.path.join(DATA_PATH,'bayes-for-mongo.json'),'w'))
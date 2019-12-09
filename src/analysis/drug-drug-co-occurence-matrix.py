import os, json, itertools 

from collections import defaultdict
from tqdm import tqdm 

import pandas as pd 

DATA_PATH = os.path.join('..','..','data')

db = json.load(open(os.path.join(DATA_PATH,'processed','lycaeum-forum-processed-has-drug-names.json'),'r'))
spelling_ontology = json.load(open(os.path.join(DATA_PATH,'processed','spelling-ontology.json'),'r'))

not_standardized_drug_names = spelling_ontology.keys()
standardized_drug_names = list(set(spelling_ontology.values()))

#Build index of posts that mention a drug
#more efficient than brute forcing searching 2.5 million combinations

drug_index = defaultdict(list)

df = pd.DataFrame(0,index=standardized_drug_names,columns=standardized_drug_names)

for not_standardized_drug_name in tqdm(not_standardized_drug_names,"building index"):
	for title,entry in db.items():
		if not_standardized_drug_name in entry['text'] or not_standardized_drug_name in entry['drugs']:
			drug_index[spelling_ontology[not_standardized_drug_name]] += [title]


for standardized_drug_name in tqdm(standardized_drug_names,'populating diagonal'):
	if standardized_drug_name == 'thymiquinone':
		print drug_index[standardized_drug_name], set(drug_index[standardized_drug_name])
	df.loc[standardized_drug_name,standardized_drug_name] = len(drug_index[standardized_drug_name])

for drug_one,drug_two in tqdm(list(itertools.combinations(standardized_drug_names,2))
		,"counting co-occurrences"):
	intersection = set(drug_index[drug_one]) & set(drug_index[drug_two])
	if len(intersection) > 0:
		df.loc[drug_one,drug_two] = len(intersection) 
		df.loc[drug_two,drug_one] = len(intersection) 
	#itertools.combinations doesn't always stay in upper or lower triangle

df.to_csv(os.path.join(DATA_PATH,'processed','drug-drug-frequency.csv'))
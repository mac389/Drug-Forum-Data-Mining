import os, json, itertools 

from collections import defaultdict
from tqdm import tqdm 

import pandas as pd 

DATA_PATH = os.path.join('..','..','data')

db = json.load(open(os.path.join(DATA_PATH,'processed','lycaeum-forum-processed-has-drug-names.json'),'r'))
spelling_ontology = json.load(open(os.path.join(DATA_PATH,'processed','spelling-ontology.json'),'r'))
list_of_drugs = spelling_ontology.keys()

#Build index of posts that mention a drug
#more efficient than brute forcing searching 2.5 million combinations

drug_index = defaultdict(list)

for drug in tqdm(spelling_ontology.keys(),"building index"):
  for title,entry in db.items():
    if drug in entry['text'] or drug in entry['drugs']:
      drug_index[spelling_ontology[drug]] += [title]

df = pd.DataFrame(0,index=spelling_ontology.values(),columns=spelling_ontology.values())

for drug_one,drug_two in tqdm(list(itertools.combinations(spelling_ontology.keys(),2))
		,"counting co-occurrences"):
	intersection = set(drug_index[drug_one]) & set(drug_index[drug_two])
	df.loc[spelling_ontology[drug_one],spelling_ontology[drug_two]] = len(intersection) 
	df.loc[spelling_ontology[drug_one],spelling_ontology[drug_two]] = len(intersection) 
	#itertools.combinations doesn't always stay in upper or lower triangle

df.to_csv(os.path.join(DATA_PATH,'processed','drug-drug-frequency.csv'))
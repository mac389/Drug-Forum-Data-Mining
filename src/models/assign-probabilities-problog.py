import json, itertools, os  

import pandas as pd

from awesome_print import ap
from tqdm import tqdm
from collections import defaultdict


DATA_PATH = os.path.join('..','..','data')
spelling_ontology = json.load(open(os.path.join(DATA_PATH,'processed','spelling-ontology.json'),'r'))
symptoms = open(os.path.join(DATA_PATH,'processed','putative-standardized-symptoms.txt'),'r').read().splitlines()
db = json.load(open(os.path.join(DATA_PATH,'lycaeum-forum-processed-has-drug-names.json'),'r'))

list_of_drugs = spelling_ontology.keys()
drugs_mentioned_in_posts = list(set(list(itertools.chain.from_iterable([entry['drugs'] for entry in db.values()]))))
drugs_symptoms = {drug:defaultdict(int) for drug in spelling_ontology.values()}
#Build index of all symptoms
drug_index = defaultdict(list)

for drug in tqdm(spelling_ontology.keys(),"building index"):
  for title,entry in db.items():
    if drug in entry['text']:
      drug_index[spelling_ontology[drug]] += [title]

for drug in tqdm(spelling_ontology.keys(),"Drugs"):
	posts = drug_index[spelling_ontology[drug]]
	drugs_symptoms[spelling_ontology[drug]] = defaultdict(int)
	for symptom in tqdm(symptoms,"Symptom"):
		drugs_symptoms[spelling_ontology[drug]][symptom] = sum([1 if symptom in db[post]['text'] else 0 for post in posts])

json.dump(drugs_symptoms,open(os.path.join(DATA_PATH,'interim','drugs_symptoms_with_ontology.json'),'w'))
 
import os, json, itertools 

from collections import defaultdict
from tqdm import tqdm 
from awesome_print import ap 

import pandas as pd 

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple,dict)):
            for j in flatten(i):
                yield j
        else:
            yield i

DATA_PATH = os.path.join('..','..','data')

db = json.load(open(os.path.join(DATA_PATH,'processed','lycaeum-forum-processed-has-drug-names.json'),'r'))

symptom_ontology = json.load(open(os.path.join(DATA_PATH,'processed','symptom-ontology.json'),'r'))
symptom_index = defaultdict(list)
drug_index = defaultdict(list)

symptom_ontology_lookup_table = {key:list(flatten(symptom_ontology[key]))for key in symptom_ontology.keys()}
symptoms = {value:key for key in symptom_ontology_lookup_table for value in symptom_ontology_lookup_table[key]}

#reverse symptom directory to create nonstandard -> standard lookup table 

standardized_symptom_names = list(set(symptoms.values()))

spelling_ontology = json.load(open(os.path.join(DATA_PATH,'processed','spelling-ontology.json'),'r'))

not_standardized_drug_names = spelling_ontology.keys()
standardized_drug_names = list(set(spelling_ontology.values()))


df = pd.DataFrame(0,index=standardized_drug_names,columns=standardized_symptom_names)


for not_standardized_drug_name in tqdm(not_standardized_drug_names,"building drug index"):
  for title,entry in db.items():
    if not_standardized_drug_name in entry['text'] or not_standardized_drug_name in entry['drugs']:
      drug_index[spelling_ontology[not_standardized_drug_name]] += [title]

for nonstandard,standard in tqdm(symptoms.items(),"building symptom index"):
  for title,entry in db.items():
    if nonstandard in entry['text'] or nonstandard in entry['drugs']:
      symptom_index[standard] += [title]


cases = [(drug,symptom) for drug in standardized_drug_names for symptom in standardized_symptom_names]

for drug,symptom in tqdm(cases,'building matrix'):
  if (len(drug_index[drug]) > 0) and (len(symptom_index[symptom])) > 0:
    intersection = set(drug_index[drug]) & set(symptom_index[symptom])
    if len(intersection) > 0:
      df.loc[drug,symptom] = len(intersection)


df.to_csv(os.path.join(DATA_PATH,'processed','drug-symptom-frequency.csv'))
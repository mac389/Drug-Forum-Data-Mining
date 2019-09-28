import os, json 

from collections import defaultdict
from tqdm import tqdm 

import pandas as pd 

DATA_PATH = os.path.join('..','..','data')

db = json.load(open(os.path.join(DATA_PATH,'lycaeum-forum-processed-has-drug-names.json'),'r'))

symptoms = open(os.path.join(DATA_PATH,'processed','putative-standardized-symptoms.txt'),'r').read().splitlines()

symptom_index = defaultdict(list)

for symptom in tqdm(symptoms,"building index"):
  for title,entry in db.items():
    if symptom in entry['text'] or symptom in entry['drugs']:
      symptom_index[spelling_ontology[symptom]] += [title]

df = pd.DataFrame.from_dict(drug_index,orient='index')
df = df.astype(bool).astype(int)

df.to_csv(os.path.join(DATA_PATH,'interim','symptom-symptom-frequency.csv'))
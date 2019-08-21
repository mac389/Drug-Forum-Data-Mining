import json, itertools 

import pandas as pd

from awesome_print import ap
from tqdm import tqdm
from collections import defaultdict

db = json.load(open('./db.json','r'))

symptoms = open('./standardized-symptoms','r').read().splitlines()

list_of_drugs = list(set(list(itertools.chain.from_iterable([entry['drugs'] for entry in db.values()]))))

drugs_symptoms = {drug:defaultdict(int) for drug in list_of_drugs}
#Build index of all symptoms
drug_index = defaultdict(list)

for drug in tqdm(list_of_drugs,"Drug"):
  for title,entry in db.items():
    if drug in entry['drugs']:
      drug_index[drug] += [title]

for drug in tqdm(list_of_drugs,"Drugs"):
  posts = drug_index[drug]
  for symptom in tqdm(symptoms,"Symptom"):
    drugs_symptoms[drug][symptom] = sum([1 if symptoms in db[post]['text'] else 0 for post in posts])

ap(drugs_symptoms)

json.dump(drug_symptoms,open('./drugs_symptoms.json','w'))
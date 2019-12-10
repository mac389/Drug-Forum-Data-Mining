import json, os

import pandas as pd

DATA_PATH = os.path.join('..','..','data','processed')
df = pd.read_csv(os.path.join(DATA_PATH,'drug-drug-frequency.csv'))
drug_ontology = json.load(open(os.path.join(DATA_PATH,'drug-name-hierarchy.json'),'r'))


#Reformat drug taxonomy to be in "class:[all members]"

drug_taxonomy = {key:list(value.keys()) for key,value in drug_ontology.items()}
print(drug_taxonomy)

df = pd.DataFrame([sum() for one,two in itertools.product()],



	columns=drug_taxonomy.keys(),index=drug_taxonomy.keys())
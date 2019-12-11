import json, os, itertools

import pandas as pd
import numpy as np 


from tqdm import tqdm 
DATA_PATH = os.path.join('..','..','data','processed')
ds = pd.read_csv(os.path.join(DATA_PATH,'drug-symptom-frequency.csv'), index_col=0)
drug_ontology = json.load(open(os.path.join(DATA_PATH,'drug-name-hierarchy.json'),'r'))

def invert(d):
    return dict( (v,k) for k in d for v in d[k] )


#Reformat drug taxonomy to be in "class:[all members]"
drug_taxonomy = {key:list(value.keys()) for key,value in drug_ontology.items()}

reverse_drug_taxonomy = invert(drug_taxonomy)


df = pd.DataFrame(np.zeros((len(drug_taxonomy),len(drug_taxonomy))),
	columns=drug_taxonomy.keys(),index=drug_taxonomy.keys())

print len(dd)**2
for one,two in tqdm(itertools.product(dd.index,repeat=2)):
	df.loc[reverse_drug_taxonomy[one],reverse_drug_taxonomy[two]] += dd.loc[one,two]

df.to_csv(os.path.join(DATA_PATH,'class-symptom-frequency.csv'))
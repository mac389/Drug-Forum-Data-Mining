import os, json 

import pubchempy as pcp 

from awesome_print import ap
from tqdm import tqdm 


DATA_PATH = os.path.join('..','..','data')
standardized_drugs = json.load(open(os.path.join(DATA_PATH,'processed','spelling-ontology.json'),'r'))
standardized_drug_names = list(set(standardized_drugs.values()))

name_to_cid = {}
for name in tqdm(standardized_drug_names, 'finding cids'):
	name_to_cid[name] =  pcp.get_cids(name, 'name', 'substance', list_return='flat')

print len(standardized_drug_names), 'nonzero ->',sum(map(bool,name_to_cid.values()))
json.dump(name_to_cid,open(os.path.join(DATA_PATH,'processed','drug-names-to-cid.json'),'w'))


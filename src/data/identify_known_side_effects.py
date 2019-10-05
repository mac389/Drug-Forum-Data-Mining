import os, json, itertools 

import pandas as pd 

from awesome_print import ap 
from tqdm import tqdm 

DATA_PATH = os.path.join('..','..','data')

drugs_cids = json.load(open(os.path.join(DATA_PATH,'processed','drug-names-to-cid.json'),'r'))

reported_side_effects = pd.read_csv(os.path.join(DATA_PATH,'external','SIDER4','indications.tsv'),sep='\t')

print reported_side_effects.head(2)

all_drugs = 0
drugs_c_cids = 0
drugs_c_cids_and_fx = 0
for drug in tqdm(drugs_cids,'Drugs'):
	if drugs_cids[drug]:
		if any([len(reported_side_effects.loc[reported_side_effects['pubchem_id']==cid]) > 0
					for cid in drugs_cids[drug]]):
			for cid in drugs_cids[drug]:
				pass
			drugs_c_cids_and_fx += 1
		drugs_c_cids += 1
	all_drugs += 1

print all_drugs
print drugs_c_cids
print drugs_c_cids_and_fx
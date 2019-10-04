import os, json, itertools 

import pandas as pd 

from awesome_print import ap 
from tqdm import tqdm 

DATA_PATH = os.path.join('..','..','data')

drugs_cids = json.load(open(os.path.join(DATA_PATH,'processed','drug-names-to-cid.json'),'r'))

reported_side_effects = pd.read_csv(os.path.join(DATA_PATH,'external','SIDER4','indications.tsv'),sep='\t')

print reported_side_effects.head(2)

for drug in tqdm(drugs_cids,'Drugs'):
	 if drugs_cids[drug]:
	 	print 

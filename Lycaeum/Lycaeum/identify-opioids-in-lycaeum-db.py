import json, itertools 

from pprint import pprint 
from tqdm import tqdm 
from collections import Counter 

import pubchempy as pcp 
import libchebipy as chebi
import drugstandards as standardizer
import pandas as pd 

'''
 TODO:
  1. Convert JSON to MongoDB so can update it
  2. 

'''

db = json.load(open('lycaeum-forum-processed-has-drug-names.json','r'))

df = pd.read_json

drugs = [db[entry]['drugs'] for entry in db.keys()]


unique_drugs = list(set(itertools.chain.from_iterable(drugs)))
#623

for drug in unique_drugs:
	print "%s:%s"%(drug,standardizer.standardize([drug],thresh=0.95))

records = []

'''
for compound in tqdm(unique_drugs[:5],'Looking up in PubChem'):
	records += [pcp.get_compounds(compound,'name')]

for i,record in enumerate(tqdm(records,'Cross-referencing in ChEBI')):
  if record:
    print unique_drugs[i], standardizer.standardize(unique_drugs[i])
    entity = record[0]
    print chebi.search(unique_drugs[i],True)
print '%d out of %d have PubChem records'%(len([x for x in records if x]),len(records))
'''
#How many of those are in PubChem?

#frequency of mention
#tally = dict(Counter(itertools.chain.from_iterable(drugs)))
#pprint(sorted(tally.items(), key = lambda x:x[1], reverse=True))

#also libchempy

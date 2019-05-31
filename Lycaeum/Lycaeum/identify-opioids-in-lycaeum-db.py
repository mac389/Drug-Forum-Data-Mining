import json, itertools 

from pprint import pprint 
from tqdm import tqdm 
from collections import Counter 

import pubchempy as pcp 
import libchebipy as chebi

db = json.load(open('lycaeum-forum-processed-has-drug-names.json','r'))

drugs = [db[entry]['drugs'] for entry in db.keys()]

unique_drugs = list(set(itertools.chain.from_iterable(drugs)))
#623

records = []


for compound in tqdm(unique_drugs[:5],'Looking up in PubChem'):
	records += [pcp.get_compounds(compound,'name')]

print '%d out of %d have PubChem records'%(len([x for x in records if x]),len(records))
#How many of those are in PubChem?

#frequency of mention
tally = dict(Counter(itertools.chain.from_iterable(drugs)))
pprint(sorted(tally.items(), key = lambda x:x[1], reverse=True))

#also libchempy
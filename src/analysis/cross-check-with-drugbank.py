import os, requests, json  

import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

from tqdm import tqdm
from collections import defaultdict

DATA_PATH = os.path.join('..','..','data','processed')
FIGURES_PATH = os.path.join('..','..','reports','figures')

df = pd.read_csv(os.path.join(DATA_PATH,'cprobs-drugs-acc.csv'),index_col=0)

x =  df[(df['bayes factor']>10)&(df['prior occurence']>30)&(df['marginal occurence']>30)]


'''
drugs = x.loc[x['source']=='dd'][['prior','marginal']]
drugs = drugs['prior'].tolist() + drugs['marginal'].tolist()
drugs += x.loc[x['source']=='ds','prior'].tolist()
drugs += x.loc[x['source']=='sd','marginal'].tolist()

#2896, unique == 152

def get_id(name):
	url = "https://rxnav.nlm.nih.gov/REST/rxcui.json?name=%s"

	try:
		r = requests.get(url%name)
	except:
		pass

	if 'rxnormId' in r.json()['idGroup']:
		return r.json()['idGroup']['rxnormId'][0]
	else:
		return np.nan
	#{u'idGroup': {u'rxnormId': [u'153165'], u'name': u'lipitor'}}

drugs = pd.DataFrame(0,index=list(set(drugs)),columns=['RxNormID'])
#columns = inferred rxn, known rxn


for drug in tqdm(drugs.index,'drugs'):
	drugs.loc[drug,'RxNormID'] = get_id(drug)

drugs.to_csv(os.path.join(DATA_PATH,'drug-bank-check.csv'))
'''

drugs = pd.read_csv(os.path.join(DATA_PATH,'drug-bank-check.csv'), index_col=0)

in_usp = drugs.dropna()

#in_usp.to_csv(os.path.join(DATA_PATH,'in_usp.csv'))
#print in_usp

'''
url = "https://api.fda.gov/drug/event.json?search=(receivedate:[20040101+TO+20191213])+AND+patient.drug.medicationname=%s&count=patient.drug.drugindication.exact"
rxn_url = 'https://api.fda.gov/drug/event.json?search=receivedate:[20040101+TO+20191213]+AND+patient.drug.medicationname=%s&count=patient.reaction.reactionmeddrapt.exact'

indications = defaultdict(list)
for drug in tqdm(in_usp.index):
	r = requests.get(url%drug)
	rx = requests.get(rxn_url%drug)
	if 'results' in r.json():
		indications[drug] += [item['term'] for item in r.json()['results']] 
	else:
		print r.json(),drug

	if 'results' in rx.json():
		indications[drug] += [item['term'] for item in rx.json()['results']]
	else:
		print 'no adverse rxn',drug

json.dump(indications,open(os.path.join(DATA_PATH,'fda-indications.json'),'w'))
'''

db = json.load(open(os.path.join(DATA_PATH,'fda-indications.json'),'r'))
rels = x[x.source.isin(['ds','sd'])]

counter = 0
for drug in in_usp.index:
	if drug in db:
		from_fda = [x.lower() for x in db[drug]]
		from_lycaeum = rels.loc[(rels['prior']==drug) | (rels['marginal']==drug),'marginal'].tolist() + rels.loc[(rels['prior']==drug)|(rels['marginal']==drug),'prior'].tolist()
		
		#from_lycaeum = [item for item in from_lycaeum if item not in drugs]

		'''
		print '-------------------'
		print from_lycaeum

		print from_fda
		print drug
		print '-------------------'	
		'''

		if from_lycaeum: 
			tcounter += 1	
print counter
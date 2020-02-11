import json, os
import pandas as pd 

DATA_PATH = os.path.join('..','..','data','processed')

#convert nested json into an array that is more MongoDB friendly

db  = json.load(open(os.path.join(DATA_PATH,'bayes_factors.json'),'r'))
df = pd.read_csv(os.path.join(DATA_PATH,'drugs-v-symptoms.csv'),index_col=0)
symptoms = df.columns.tolist()
drugs = df.index.tolist()

taxonomy = json.load(open(os.path.join(DATA_PATH,'..','interim','drug_taxonomy.json'),'r'))
print(taxonomy)

'''
Annotations
  1. Type (substance or effect)
  2. Class 

'''



'''
db2 = []
for key, value in db.items():
	for second,ratio in db[key].items():
		db2 += [{'prior':key,
				 'conditional':second,
				 'bayes ratio':ratio,
				 'prior_type':,
				 'conditional_type':,
				 'prior_class':,
				 'conditional_class':}]





json.dump(db2,open(os.path.join(DATA_PATH,'bayes-for-mongo.json'),'w')
'''
import os, json, itertools 

from collections import defaultdict
from tqdm import tqdm 
from awesome_print import ap 

import pandas as pd 

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple,dict)):
            for j in flatten(i):
                yield j
        else:
            yield i

DATA_PATH = os.path.join('..','..','data')

db = json.load(open(os.path.join(DATA_PATH,'processed','lycaeum-forum-processed-has-drug-names.json'),'r'))

ontology = json.load(open(os.path.join(DATA_PATH,'processed','symptom-ontology.json'),'r'))
symptom_index = defaultdict(list)


ontology_lookup_table = {key:list(flatten(ontology[key]))for key in ontology.keys()}
symptoms = {value:key for key in ontology_lookup_table for value in ontology_lookup_table[key]}

#reverse symptom directory to create nonstandard -> standard lookup table 

standardized_symptom_names = symptoms.values()
df = pd.DataFrame(0,index=standardized_symptom_names,columns=standardized_symptom_names)

for nonstandard,standard in tqdm(symptoms.items(),"building index"):
  for title,entry in db.items():
    if nonstandard in entry['text'] or nonstandard in entry['drugs']:
      symptom_index[standard] += [title]


for standard in tqdm(standardized_symptom_names,'populating diagonal'):
	df.loc[standard,standard] = len(symptom_index[standard])

for s_one,s_two in tqdm(list(itertools.combinations(standardized_symptom_names,2))
		,"counting co-occurrences"):
	intersection = set(symptom_index[s_one]) & set(symptom_index[s_two])
	if len(intersection) > 0:
		df.loc[s_one,s_two] = len(intersection) 
		df.loc[s_two,s_one] = len(intersection) 
	#itertools.combinations doesn't always stay in upper or lower triangle

df.to_csv(os.path.join(DATA_PATH,'processed','symptom-symptom-frequency-frequency.csv'))
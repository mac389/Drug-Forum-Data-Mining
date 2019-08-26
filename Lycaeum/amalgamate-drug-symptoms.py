import json, os, itertools 

import pandas as pd 
import numpy as np 

from awesome_print import ap 
from tqdm import tqdm 

ontology = json.load(open(os.path.join('..','classification-standardized-symptoms.json'),'r'))
drugs_symptoms = json.load(open(os.path.join('.','Lycaeum','drugs_symptoms.json'),'r'))

#group symptoms

def flatten(alist):
	ans = []
	for item in alist:
		if isinstance(item,str):
			ans += [item]
		elif isinstance(item,dict):
			ans += item.values()
	return list(itertools.chain.from_iterable(ans))


classes = ontology.keys()
drugs = drugs_symptoms.keys()

arr = np.zeros((len(drugs),len(classes)))

class_symptoms = {key:flatten(value) for key,value in ontology.iteritems()}
ap(class_symptoms)
'''
for i, drug in enumerate(tqdm(drugs,'Drugs')):
	for j,classe in enumerate(tqdm(classes,'Class')):
		arr[i,j] =  lclasses[classe] drugs_symptoms[drugs]
'''
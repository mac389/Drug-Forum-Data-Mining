import json, os, itertools 

import pandas as pd 
import numpy as np 

#from awesomeprint import ap 
from tqdm import tqdm 
from collections import Counter

ontology = json.load(open(os.path.join('..','classification-standardized-symptoms.json'),'r'))
drugs_symptoms = json.load(open(os.path.join('.','Lycaeum','drugs_symptoms.json'),'r'))

#group symptoms

def flatten(alist):
  ans = []
  for item in alist:
    if isinstance(item,str) or isinstance(item,unicode):
      ans += [item]
    elif isinstance(item,dict):
      ans += item.values()[0]
  return ans


classes = ontology.keys()
drugs = drugs_symptoms.keys()

arr = np.zeros((len(drugs),len(classes)))

class_symptoms = {key:set(flatten(value)) for key,value in ontology.iteritems()}
#ap(class_symptoms)


for i, drug in enumerate(tqdm(drugs,'Drugs')):
	for j,classe in enumerate(tqdm(classes,'Class')):
		arr[i,j] =  len(class_symptoms[classe] & set(drugs_symptoms[drug].keys()))

df = pd.DataFrame(arr,columns = classes, index=drugs)


print len(class_symptoms['emotion'] & set(drugs_symptoms['gum'].keys()))

df.to_csv(os.path.join('.','frequency-of-symptoms.csv'))
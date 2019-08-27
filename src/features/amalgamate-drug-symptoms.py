import json, os, itertools 

import pandas as pd 
import numpy as np 

#from awesomeprint import ap 
from tqdm import tqdm 
from collections import Counter
from awesome_print import ap

ontology = json.load(open(os.path.join('.','ontology.json'),'r'))
drugs_symptoms = json.load(open(os.path.join('.','drugs_symptoms.json'),'r'))

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

arr = np.zeros((len(drugs),len(classes)),dtype=int)

class_symptoms = {key:set(flatten(value)) for key,value in ontology.iteritems()}
#ap(class_symptoms)

for i, drug in enumerate(tqdm(drugs,'Drugs')):
  for j,classe in enumerate(tqdm(classes,'Class')):
    #Count nonero symptoms
    symptoms = {symptom for symptom,count in drugs_symptoms[drug].items() if count > 0}
    arr[i,j] =  len(class_symptoms[classe] & symptoms)


df = pd.DataFrame(arr,columns = classes, index=drugs)
df.to_csv('./frequency-of-symptoms.csv')
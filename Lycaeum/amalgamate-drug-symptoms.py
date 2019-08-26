import json, os, itertools 

import pandas as pd 
import numpy as np 

from awesome_print import ap 
from tqdm import tqdm 

ontology = json.load(open(os.path.join('..','classification-standardized-symptoms.json'),'r'))
drugs_symptoms = json.load(open(os.path.join('.','Lycaeum','drugs_symptoms.json'),'r'))

#group symptoms

classes = ontology.keys()
drugs = drugs_symptoms.keys()

arr = np.zeros((drugs,classes))

class_symptoms = {classe: for classe in classes}

for i, drug in enumerate(tqdm(drugs,'Drugs')):
	for j,classe in enumerate(tqdm(classes,'Class')):
		arr[i,j] =  lclasses[classe] drugs_symptoms[drugs]
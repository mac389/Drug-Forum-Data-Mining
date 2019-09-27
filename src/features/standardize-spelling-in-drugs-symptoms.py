import os, json 

import pandas as pd

from awesome_print import ap 

DATA_PATH = os.path.join('..','..','data')

spelling_ontology = json.load(open(os.path.join(DATA_PATH,'processed','spelling-ontology.json'),'r'))
df = pd.read_csv(os.path.join(DATA_PATH,'processed','drugs-v-symptoms.csv'), index_col=0)

#Combine rows in data frame based on index


#First rename index column based on spelling ontology
df = df.rename(index=spelling_ontology)
df = df.groupby(df.index).sum()

print df 
ap(spelling_ontology)
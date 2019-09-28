import json, os, itertools 

import pandas as pd
import numpy as np 


df = pd.DataFrame.from_dict(json.load(open(os.path.join('..','..','data','interim','drugs_symptoms_with_ontology.json'),'r'))
		,orient='index')

'''
df = pd.read_csv('./cofrequencies.csv')
df.columns = ['d1','d2','freq']
'''
#Take overall change of occurrence as average 
#Have to use the accurate numbers, go with this for time now
#baseline_chance = df.freq.replace(0,np.nan).mean()/df.freq.sum()


'''
P(effect | drug) = P(effect + drug)/P(drug)

df has (rows x columns) as (drugs,symptoms)

p(drug) => sum over symptoms [not perfect, overcounts]

'''

baseline_probabilities = df.sum(axis=1)/df.sum(axis=1).sum()

overall_sum = df.sum().sum()


coingestants = """%.04f::also_ingested(X,%s) :-
                    person(X),
                    substance_ingested(X,%s)"""


'''
Create conditional probability DataFrame, formatted as p(effect | drug)

'''


conditional_prob_df = df.copy(deep=True)
conditional_prob_df /= overall_sum
conditional_prob_df /= baseline_probabilities

print baseline_probabilities[baseline_probabilities==0]
'''
with open(os.path.join('..','..','data','processed','for-problog.txt'),'w') as fout:
	for symptom in df.columns:
		for drug in df.index:
			p_drug_and_effect = df.loc[drug,symptom]/float(overall_sum)
			conditional_probability = p_drug_and_effect/baseline_probabilities.loc[drug]

			print>>fout,effects%(conditional_probability,symptom,drug)

	print>>fout,'%%%%%%%%%%%%%%%%%%'
'''
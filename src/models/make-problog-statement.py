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

effects = """%.04f::has_effect(X,%s) :-
				person(X),
				substance_ingested(X,%s)"""

with open(os.path.join('..','..','data','processed','for-problog.txt'),'w') as fout:
	for symptom in df.columns:
		for drug in df.index:
			p_drug_and_effect = df.loc[drug,symptom]/float(overall_sum)
			conditional_probability = p_drug_and_effect/baseline_probabilities.loc[drug]

			print>>fout,effects%(conditional_probability,symptom,drug)

	print>>fout,'%%%%%%%%%%%%%%%%%%'

	for drug_one in df.index:
		for drug_two in df.index:
			#Conditional probabilities are not symmetric!
			p_one_and_two
'''
for drug_one,drug_two in itertools.combinations(df.index,2):
	print drug_one,drug_two

  scaling_factor = df[df['d1']==drug]['freq'].sum()
  df.loc[df.d1==drug,'scaling factor'] = scaling_factor


df['probability'] = df['freq']/df['scaling factor']
df[df.probability==0] = baseline_chance



with open('./for-problog.txt','w') as fout:
  for d1 in df['d1'].unique():
    for d2 in df.loc[df.d1==d1,'d2']: 
      p = df.loc[(df.d1 == d1) & (df.d2 == d2)]['probability'].values[0]
      print>>fout,coingestants%(p,d2,d1)
      print>>fout,'\n'

'''

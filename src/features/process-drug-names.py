import os 

drug_names = open(os.path.join('..','..','data','processed','drug_names'),'r').read().splitlines()

with open(os.path.join('..','..','data','processed','unique_drug_names'),'w') as fout:
	for drug in set(drug_names):
		print>>fout,drug
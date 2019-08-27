from pprint import pprint

drug_names = open('deduplicated_drug_names','r').read().splitlines()
'''
#Remove middle dash
drug_names = [drug.replace('-',' ') if drug.replace('-','').isalpha() else drug for drug in drug_names]
with open('deduplicated-curated-drug-names','w') as fid:
	for drug in drug_names:
		print>>fid,drug
'''
drug_names = list(set(open('deduplicated-curated-drug-names','r').read().splitlines()))
with open('deduplicated-curated-drug-names','w') as fid:
	for drug in drug_names:
		print>>fid,drug
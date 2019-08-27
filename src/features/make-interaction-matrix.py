import numpy as np 
import matplotlib.pyplot as plt 
import json, math

drug_names = list(set(open('drug_names','r').read().splitlines()))
with open('deduplicated_drug_names','w') as fid:
	for drug in drug_names:
		print>>fid,drug

drug_names = open('deduplicated-curated-drug-names','r').read().splitlines()
text = [item['drugs'] for item in json.load(open('lycaeum-forum-processed-has-drug-names.json','r')).itervalues()]
interaction_matrix = np.zeros((len(drug_names),len(drug_names)))

#interaction_matrix = np.zeros((50,50))
row_idx,col_idx = np.tril_indices(len(drug_names)) #includes diagonal 
length = len(zip(row_idx,col_idx))
for k,(i,j) in enumerate(zip(row_idx,col_idx)):
	interaction_matrix[i,j] = sum([drug_names[i] in experience and drug_names[j] in experience 
									for experience in text]) 
	if k%1000 == 0:
		print k/float(length)

interaction_matrix = interaction_matrix + interaction_matrix.T
#np.save('small-interaction_matrix-2015-11-13.npy',interaction_matrix)
np.save('interaction_matrix-2015-11-28-w-deduped-curated-drug-names.npy',interaction_matrix)
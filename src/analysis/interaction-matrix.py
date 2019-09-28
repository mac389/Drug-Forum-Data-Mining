import json
import numpy as np 
import Graphics as artist
import matplotlib.pyplot as plt 
from matplotlib import rcParams

rcParams['text.usetex'] = True
#data = np.load('interaction_matrix-2015-11-28-2.npy')
data = np.load('interaction_matrix-2015-11-28-w-deduped-curated-drug-names.npy')
#Should make this name a parameter
drug_names = open('deduplicated-curated-drug-names','r').read().splitlines()

data += data.T
data[np.diag_indices_from(data)] /= 2

percentile = 99
cutoff = np.percentile(data.ravel(),percentile).astype(int)
#95th percentile corresponds to 6 mentions
print cutoff

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(np.tril(data).ravel(),color='k',bins=np.logspace(0,6,np.sqrt(len(drug_names))),log=True,histtype='step')
ax.axvline(x=cutoff,linewidth=1.5,color='r',linestyle='--')
ax.axvline(x=6,linewidth=1.5,color='r',linestyle='--')
ax.set_xscale('log')
ax.set_xlabel(artist.format('No. of comentions'))
ax.set_ylabel(artist.format('Count'))
artist.adjust_spines(ax)
plt.savefig('histogram-interaction-matrix-curated-drug-names')

percentiles = [95,99]
cutoff = {str(percentile):np.percentile(data.ravel(),percentile).astype(int)
				for percentile in percentiles}

significant_drug_comentions = {}
for percentile in percentiles:
	significant_drug_comentions[str(percentile)] = {}
	for i in xrange(len(drug_names)):
		significant_drug_comentions[str(percentile)][drug_names[i]] = {}
		for j in xrange(len(drug_names)):
			if data[i,j] > cutoff[str(percentile)]:
				significant_drug_comentions[str(percentile)][drug_names[i]][drug_names[j]] = data[i,j]

json.dump(significant_drug_comentions,open('significant_drug_comentions-curated-drug-names.json','w'))
row_idx,col_idx = np.tril_indices(len(drug_names),k=-1) #no diagonal 
with open('highly-mentioned-drugs-gt-99-curated-drug-names','w') as fid:
	for i,j in zip(row_idx,col_idx):
		if data[i,j] > cutoff['99']:
			print>>fid,'%s \t %s \t %d'%(drug_names[i],drug_names[j],data[i,j])
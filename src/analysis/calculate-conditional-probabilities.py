import os, itertools, json 

import numpy as np 
import pandas as pd

from tqdm import tqdm
from collections import defaultdict
from pprint import pprint 

DATA_PATH = os.path.join('..','..','data','processed')

ss = pd.read_csv(os.path.join(DATA_PATH,'symptom-symptom-frequency.csv'),index_col=0)
ds = pd.read_csv(os.path.join(DATA_PATH,'drug-symptom-frequency.csv'),index_col=0)
dd = pd.read_csv(os.path.join(DATA_PATH,'drug-drug-frequency.csv'),index_col=0)

drugs = dd.index.unique().tolist()
symptoms = ss.index.unique().tolist()

dd_diag = np.diag(dd).sum().astype(float)
ss_diag = np.diag(ss).sum().astype(float)

exceptions = [] 
conditional_probability = defaultdict(dict)
unconditional_probability = {}
for prior, marginal in tqdm(list(itertools.product(drugs+symptoms,repeat=2))):
	#calculate conditional probability the inefficient way

	#P(prior,marginal)/P(marginal)

	if prior in drugs:
		if marginal in drugs: #Drug-Drug
			p__a_and_b = dd.loc[prior][marginal]/(dd_diag*dd_diag)
			p__b = dd.loc[marginal,marginal]/dd_diag

			if prior == marginal:
				unconditional_probability[prior] = dd.loc[prior][prior]/(dd_diag)

		elif marginal in symptoms: #Drug-Symptom
			p__a_and_b = ds.loc[prior][marginal]/(dd_diag*ss_diag)
			p__b = ss.loc[marginal,marginal]/ss_diag
		else:
			exceptions += [(marginal,'marginal not in drugs or symptoms')]

	elif prior in symptoms:
		if marginal in drugs: #Symptom-Drug
			p__a_and_b = ds.loc[marginal][prior]/(dd_diag*ss_diag)
			p__b = dd.loc[marginal,marginal]/dd_diag
		elif marginal in symptoms: #Symptom-Symptom
			p__a_and_b = ss.loc[prior][marginal]/(ss.loc[prior,prior]*ss.loc[marginal,marginal])
			p__b = ss.loc[marginal,marginal]/ss_diag

			if prior == marginal:
				unconditional_probability[prior] = ss.loc[prior][prior]/(ss_diag)
		else:
			exceptions += [(marginal,'marginal not in drugs or symptoms')]
	else:
		exceptions += [(prior,'prior not in drugs or symptoms')]
	
	conditional_probability[prior][marginal] = p__a_and_b/p__b

print(exceptions)
json.dump(conditional_probability,open(os.path.join(DATA_PATH,'maually-calculated-conditional-probabilities.json'),'w'))
json.dump(unconditional_probability,open(os.path.join(DATA_PATH,'maually-calculated-unconditional-probabilities.json'),'w'))
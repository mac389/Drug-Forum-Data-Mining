import os, itertools, json 

import numpy as np 
import pandas as pd

from tqdm import tqdm
from collections import defaultdict
from pprint import pprint 

DATA_PATH = os.path.join('..','..','data','processed')

conditional_probabilities = json.load(open(os.path.join(DATA_PATH,'maually-calculated-conditional-probabilities.json')))
unconditional_probabilities = json.load(open(os.path.join(DATA_PATH,'maually-calculated-unconditional-probabilities.json')))

bayes_factors = defaultdict(dict)

for prior in tqdm(conditional_probabilities):
	for marginal in conditional_probabilities[prior]:
		if unconditional_probabilities[prior] > 0:
			bayes_factors[prior][marginal] = conditional_probabilities[prior][marginal]/unconditional_probabilities[prior]
		else:
			bayes_factors[prior][marginal] = np.nan

json.dump(bayes_factors,open(os.path.join(DATA_PATH,'bayes_factors.json'),'w'))

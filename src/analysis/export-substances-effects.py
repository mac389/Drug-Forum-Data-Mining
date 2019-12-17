import os
import pandas as pd 

from tabulate import tabulate
from pprint import pprint

DATA_PATH = os.path.join('..','..','data','processed')

df = pd.read_csv(os.path.join(DATA_PATH,'drug-symptom-frequency.csv'), index_col=0)

print tabulate(df.index.to_numpy().reshape((-1,4)),tablefmt='latex')
import os 

import pandas as pd


DATA_PATH = os.path.join('..','..','data','processed')
ss = pd.read_csv(os.path.join(DATA_PATH,'drug-drug-frequency.csv'), index_col=0)

thymiquinone = ss['thymiquinone']

print ss['thymiquinone']['thymiquinone']

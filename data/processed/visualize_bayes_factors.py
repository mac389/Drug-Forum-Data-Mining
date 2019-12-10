import json, os 

import pandas as pd

DATA_PATH = os.path.join('..','..','data','processed')
js = json.load(open(os.path.join(DATA_PATH,'bayes_factors.json'))

#df = pd.read_json(json.load(open(os.path.join('./bayes_factors.json','r')))
print(js)
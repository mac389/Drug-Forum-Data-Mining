import os, itertools 

import pandas as pd 
import numpy as np 

from tqdm import tqdm 
from sklearn.utils import resample


DATA_PATH = os.path.join('..','..','data','processed')

filenames = ['symptom-symptom-frequency', 
			 'class-symptom-frequency',
			 'class-class-frequency',
			 'symptom-class-frequency'] #class symptoms repeated because p(s|e) neq p(e|s)
 

ss = pd.read_csv(os.path.join(DATA_PATH,'symptom-symptom-frequency.csv'),index_col=0)
ds = pd.read_csv(os.path.join(DATA_PATH,'drug-symptom-frequency.csv'),index_col=0)
dd = pd.read_csv(os.path.join(DATA_PATH,'drug-drug-frequency.csv'),index_col=0)
sd = pd.read_csv(os.path.join(DATA_PATH,'drug-symptom-frequency.csv'),index_col=0).transpose()

print dd.loc['monovinyl','chlorine']/float(dd.loc[:,'chlorine'].sum())
print dd.loc['monovinyl',:].sum()
'''
ss_diag = np.diag(ss).sum().astype(float)
print df.loc[(df.prior=='immunologic')&(df.marginal=='emotion'),'conditional_probability'].values
a= ss.loc['immunologic','emotion']/float(ss.loc['immunologic','immunologic'].sum()*ss.loc['emotion','emotion'].sum())
b= ss.loc['emotion','emotion']/float(ss.loc['emotion',:].sum())


conditional_probability = ss.loc['immunologic','emotion']/float(ss.loc['emotion','emotion'])
print conditional_probability
#print a/b
#print a/b/(ss.loc['immunologic','immunologic']/ss_diag)


'''
import pandas as pd
import numpy as np 

df = pd.read_csv('./cofrequencies.csv')
df.columns = ['d1','d2','freq']

#Take overall change of occurrence as average 
#Have to use the accurate numbers, go with this for time now
baseline_chance = df.freq.replace(0,np.nan).mean()/df.freq.sum()

df['scaling factor'] = np.nan

for drug in df['d1'].unique():
  scaling_factor = df[df['d1']==drug]['freq'].sum()
  df.loc[df.d1==drug,'scaling factor'] = scaling_factor


df['probability'] = df['freq']/df['scaling factor']
df[df.probability==0] = baseline_chance

coingestants = """%.02f::also_ingested(X,%s) :-
                    person(X),
                    substance_ingested(X,%s)"""

with open('./for-problog.txt','w') as fout:
  for d1 in df['d1'].unique():
    for d2 in df.loc[df.d1==d1,'d2']: 
      p = df.loc[(df.d1 == d1) & (df.d2 == d2)]['probability'].values[0]
      print>>fout,coingestants%(p,d2,d1)
      print>>fout,'\n'

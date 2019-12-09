import os 
import pandas as pd

DATA_PATH = os.path.join('..','..','data','processed')

df = pd.read_csv(os.path.join(DATA_PATH,'knowledge-base-as-df.csv',index_col=0))

print(df)


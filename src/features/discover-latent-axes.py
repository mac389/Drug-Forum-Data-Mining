import os

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

from collections import Counter 
from sklearn.preprocessing import StandardScaler


df = pd.read_csv(os.path.join('..','..','data','processed','drug-drug-frequency.csv'),index_col=0)



import json 

from awesome_print import ap 
from tqdm import tqdm 

db = json.load(open('./dictionary-for-symptoms.json','rb'))

x = list(set(db.values()))
ap(x)
print len(x)

with open('./putative-standardized-symptoms.txt','wb') as fout:
	for entry in tqdm(x,'writing to file'):
		print>>fout,entry
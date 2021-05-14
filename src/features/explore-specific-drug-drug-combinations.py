import os, json

from pymongo import MongoClient

client = MongoClient()
db = client['lycaeum']
collection = db['records']

drugs = ['doxorubicin','thioridazine']
drugs = ["pyridine","salvia"]
selector = lambda drugs: f'{{$all:[{",".join(drugs)}]}}'
# go into the text field 
print(selector(drugs))

return_options = {"_id":0,"text":1}
together = list(collection.find({"text":{"$all":drugs}},return_options))
d1 = list(collection.find({"text":{"$in":[drugs[0]]}},return_options))
d2 = list(collection.find({"text":{"$in":[drugs[1]]}},return_options))

print(len(d1))
print(len(d2))
print(len(together))

print(' '.join(' '.join(item['text']) for item in together))
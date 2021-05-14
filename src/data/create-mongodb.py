import os, json

from pymongo import MongoClient

corpus = json.load(open(os.path.join('..','..','data','processed','lycaeum-forum-processed-has-drug-names.json')))
cargo = [{**{'title':key},**payload} for key,payload in corpus.items()]

client = MongoClient()
db = client['lycaeum']
collection = db['records']

collection.insert_many(cargo)

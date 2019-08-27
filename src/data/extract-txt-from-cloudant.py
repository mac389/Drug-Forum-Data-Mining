import couchdb, json, datetime

from time import time 
from awesome_print import ap 

timestamp = datetime.datetime.fromtimestamp(time()).strftime('%Y-%m-%d')
credentials = json.load(open('credentials.json'))

couch = couchdb.Server("https://yid.cloudant.com/")
couch.resource.credentials = (credentials['username'],credentials['password'])

with open('snapshot-%s'%timestamp,'w') as outfile:
	counter = 0 
	for id in couch['erowid']:
		if counter%100==0:
			ap(counter)
		record = couch['erowid'][id]
		print>>outfile,record['text'].strip().encode('utf-8')
		counter += 1 
		
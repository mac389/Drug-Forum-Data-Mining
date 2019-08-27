import couchdb, json

credentials = json.load(open('credentials.json'))

couch = couchdb.Server("https://yid.cloudant.com/")
couch.resource.credentials = (credentials['username'],credentials['password'])

field = 'drugs'

all_drug_names = []
counter = 0
for id in couch['erowid']:
	record = couch['erowid'][id]
	drug_names = record[field]
	for drug_name in drug_names:
		if '(' and ')' in drug_name:
			all_drug_names += [drug_name[0:drug_name.find('(')], drug_name[drug_name.find('(')+1:drug_name.find(')')].lower()]
			counter += 1
			if counter%100==0:
				print counter
		else:
			all_drug_names += [drug_name.lower()]
			counter +=1
			if counter%100==0:
				print counter

with open('drug_names','w') as f:
	for drug_name in all_drug_names:
		print>>f,drug_name
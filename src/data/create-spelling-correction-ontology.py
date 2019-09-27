import json, os, itertools

from awesome_print import ap

DATA_PATH = os.path.join('..','..','data')
nascent_ontology = json.load(open(os.path.join(DATA_PATH,'processed',
			'manually-curated-substance-mentions-drugs-only.json'),'r')) 

d = {}
for entry in nascent_ontology.values():
	for key, values in entry.items():
		for value in values:
			d[value] = key

'''
  Nascent ontology has the structure
  class : {standardized name:[names that actually occurred]}

  This module creates from that dictionary a flat dictionary that maps the names that actually occurred
  to the standard name

'''

json.dump(d,open(os.path.join(DATA_PATH,'processed','spelling-ontology.json'),'w'))
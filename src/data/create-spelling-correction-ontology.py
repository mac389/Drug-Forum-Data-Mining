import json, os

from awesome_print import ap

DATA_PATH = os.path.join('..','..','data')
nascent_ontology = json.load(open(os.path.join(DATA_PATH,'processed',
			'manually-curated-substance-mentions-drugs-only.json'),'r')) 



ap(nascent_ontology)
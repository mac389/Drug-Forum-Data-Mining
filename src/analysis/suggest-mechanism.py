import csv

import pandas as pd
import libchebipy as chebi

from bioservices import KEGG
from bioservices import OmniPath

from pprint import pprint 
o = OmniPath()

df = pd.read_csv('./combinations-for-second-paper.tsv', delim_whitespace=True, header=None, 
	names=['Substance 1','Substance 2','Co-occurences'])

unique_drug_names = list(set(df['Substance 1'].tolist() + df['Substance 2'].tolist()))

db = {}

#standardize "names"
import drugstandards as standardizer

'''
with open('./drug-names-for-ontology.csv','w') as fout:
	writer = csv.writer(fout)
	for drug in unique_drug_names:
		writer.writerow([drug])
'''

'''
for drug in unique_drug_names:
	if all([item is None for item in standardizer.standardize([drug],thresh=0.95)]):
		db[drug] = {}
	#print "%s:%s"%(drug,standardizer.standardize([drug],thresh=0.95))

print db.keys()
'''


one = 2679
two = 16236

#predict interaction 

substances = {'ethanol':{'CHEBI ID':16236}, 'amphetamine':{'CHEBI ID':2679}}
#relate substance to chebi entity
for substance in substances:

	substances[substance]['CHEBI record'] = chebi.ChebiEntity('CHEBI:%d'%(substances[substance]['CHEBI ID']))
	kegg_accession_number = [item.get_accession_number() for item in substances[substance]['CHEBI record'].get_database_accessions()
							if item.get_type()=='KEGG COMPOUND accession']
	substances[substance]['KEGG accession number'] = kegg_accession_number

#extract chebi properties
for substance in substances: 
	for outgoing in substances[substance]['CHEBI record'].get_outgoings():
		target = chebi.ChebiEntity(outgoing.get_target_chebi_id())
		print('\t' + outgoing.get_type() + '\t' + target.get_name())

'''
#cross-reference with kegg pathway
request = REST.kegg_find('drug','amphetamine')
print request.read()
'''

s = KEGG()
x = s.find("drug",'amphetamine')

pprint(o.get_interactions(['P14416','O75899']))

#create map from list of proteins


'''
	has_role	adrenergic uptake inhibitor
	has_role	dopamine uptake inhibitor
	has_role	sympathomimetic agent
	has_role	dopaminergic agent
	has_role	adrenergic agent
	has_role	bronchodilator agent


	has_role	polar solvent
	has_role	NMDA receptor antagonist
	has_role	protein kinase C agonist
'''


'''
	#Seems to matter less
	for incoming in substances[substance]['CHEBI record'].get_incomings():
		source = chebi.ChebiEntity(incoming.get_target_chebi_id())
		#print '\t' + source.get_name() + '\t' +incoming.get_type()
'''

#Combine roles


'''
#get KEGG accession number
kegg_accession_number = [item.get_accession_number() for item in x.get_database_accessions()
							if item.get_type()=='KEGG COMPOUND accession']

#What KEGG pathways does this compound play in?
from Bio.KEGG import REST
'''

'''
{"lsd":"lysergic acid diethylamide",
"lsa": "lysergic acid amide",
"ginseng": "ginseng",
"sage": "salvia",
"psilocybe": 
"glue":
"stramonium":
"mmda":
"ephedra":
"police":
"burning":
"cannabis":
"willow":
"pcp":
"haze":
"amt":
"lotus":
"jah":
"crack":
"inoxia":
"toluene":
"vicodin":
"kush":
"opiods":
"harmaline":
"psilocin":
"amanita":
"dpt":
"silver":
"yopo":
"ecstacy":
"ayahuasca":
"alchohol":
"oxygen":
"gbl":
"patch":
"nutmeg":
"hcl":
"poppy":
"cigar":
"freebase":
"mda":
"lavender":
"pulse":
"mde":
"pma":
"explosion":
"kratom":
"cactus":
"sativa":
"snuff":
"vicks":
"mandrake":
"mojo":
"tma":
"venom":
"mate":
"passion":
"cubensis":
"maoi":
"ointment":
"red":
"lobelia":
"brugmansia":
"hash":
"iboga":
"rum":
"thujone":
"chamomile":
"sassafras":
"ayahausca":
"kanna":
"sinica":
"zacatechichi":
"ibogaine":
"piracetam":
"belladonna":
"catnip":
"aura":
"mullein":
"lecithin":
"glory":
"nitrous":
"calamus":
"peyote":
"butane":
"guard":
"divinorum":
"pod":
"ether":
"paint":
"beer":
"grapefruit":
"spike":
"det":
"khat":
"bufotenine":
"torch":
"skullcap":
"hawaiian":
"nucifera":
"pharmahuasca":
"dipt":
"cacao":
"ginkgo":
"opium":
"valerian":
"mescaline":
"psilocybin":
"don":
"tfmpp":
"nelumbo":
"mcpp":
"cabrerana":
"tank":
"opioids":
"kava":
"bzp":
"percocet":
"oxide":
"cannabinoids":
"dmt":
"coca":
"mdma":
"adderall":
"tyrosine":
"yoga":
"dill":
"mugwort":
"n2o":
"wormwood":
"mbdb":
"spp":
"ginger":
"calea":
"dxo":
"ecstasy":
"dxm":
"guarana":
"syrian":
"yerba":
"spice":
"datura":
"absinthe":
"migraine":
"acacia":
"salvia":
"suboxone":
"harmine":
"damiana":
"bufotenin":
"phalaris":
"pain":
"blotter":
"diplopterys":
"coleus":
"mimosa":
"semilanceata":
"henbane":
"garlic":
"maca":
"lemon":
"tobacco":
"cebil":
"doi":
"dom":
"dob":
"doc":
"belladona":
"gaba":
"wine":}
'''

#standardized_names = 

#drugs.add_drug_mapping({"MULTI-VITAMIN":"VITAMIN"})
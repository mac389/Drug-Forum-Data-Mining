import pandas as pd
import csv
import libchebipy as chebi


df = pd.read_csv('./combinations-for-second-paper.tsv', delim_whitespace=True, header=None, 
	names=['Substance 1','Substance 2','Co-occurences'])

unique_drug_names = list(set(df['Substance 1'].tolist() + df['Substance 2'].tolist()))

db = {}

#standardize "names":
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

#Say we have to CHEBI IDs, just to work out the rest of the algorithm

one = 2679
two = 16236

#predict interaction 

x =  chebi.ChebiEntity('CHEBI:%d'%one)
x.get_outgoings()

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
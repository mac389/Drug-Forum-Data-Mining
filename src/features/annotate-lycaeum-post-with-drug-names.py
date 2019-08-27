import os, json
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
#Move files (takes to long in bash)

starting_dir = './forums-denuded'
lmtzr = WordNetLemmatizer()
drug_names = set(open('drug_names','r').read().splitlines())
stopwords = set(open('stopwords.txt','r').read().splitlines())
lycaeum = {}
counter = 0 
number_of_files = len(os.listdir(starting_dir))
for filename in os.listdir(starting_dir):
	txt = word_tokenize(' '.join(open(os.path.join(starting_dir,filename),'r').read().splitlines()).decode('utf-8').encode('ascii','ignore').lower())
	txt = {lmtzr.lemmatize(token) for token in txt if token.isalnum()} - stopwords
	
	#Figure out what drugs are mentioned, if any 
	drug_name_in_this_txt =  drug_names & txt
	if len(drug_name_in_this_txt) == 0:
		counter += 1

	lycaeum[filename.strip()] = {}
	lycaeum[filename.strip()]['text'] = list(txt)
	lycaeum[filename.strip()]['drugs'] = list(drug_name_in_this_txt)

print counter,number_of_files,counter/float(number_of_files)
json.dump(lycaeum,open('lycaeum-forum-processed-has-drug-names.json','w'))
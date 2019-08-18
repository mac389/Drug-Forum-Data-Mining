import json 

from spellchecker import SpellChecker
from awesome_print import ap 
from tqdm import tqdm 

spell = SpellChecker()
spell.word_frequency.load_words(['priapism','dystaxia'])
text = open('./keywords-symptoms.txt','r').read().splitlines()

dictionary = {}

for word in tqdm(text,'processing text'):
	dictionary[word] = spell.correction(word)


json.dump(dictionary,open('./dictionary-for-symptoms.json','wb'))
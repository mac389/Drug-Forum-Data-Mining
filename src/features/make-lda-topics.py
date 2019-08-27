import numpy as np

from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from awesome_print import ap
from collections import defaultdict
from gensim import corpora, models, similarities

experiences = open('cleaned-snapshot-2015-10-17','rb').read().splitlines()
#Parametrize name later

frequency = defaultdict(int)
for text in experiences:
	for token in text.split():
		frequency[token] += 1

texts = [[''.join(ch for ch in token if ord(ch)<128) 
			for token in text.split() if frequency[token] > 1]
			for text in experiences]
#Ignore words that occur only once

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
#This corpus is small enough to reside in RAM. Use Corpus class for larger corpora. 
#Class doesn't (yet) remove hapaxes.

num_topics =100
model = models.ldamodel.LdaModel(corpus=corpus,id2word=dictionary, num_topics=num_topics)

with open('topics','w') as outfile:
	for i in xrange(num_topics):
		print>>outfile,model.print_topic(i)


#Must compare topics to junk distribution to provide a ranking of topics

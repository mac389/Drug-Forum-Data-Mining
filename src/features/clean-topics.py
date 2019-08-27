import itertools

import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist

from matplotlib import rcParams
from collections import namedtuple 
from scipy.stats import entropy 

'''
   Al-Sumait et al (2009) used three distance measures
    1. Kullbach-Liebler divergences
    2. Cosine Similarity
    3. Correlation (less clear on how they used this)

   They used these measures to answer three questions:
     1. What topics have a nonuniform distribution of words?
	 2. What words are not distributed uniformly over topics?
	 3. What topics are not distributed uniformly over documents?
'''

rcParams['text.usetex'] = True
Word = namedtuple('Word',['text','weight'])

def make_named_tuple(word):
	weight,text = word.split('*')
	return 

def parse_topics(filename):
	return [{word.split('*')[1]:float(word.split('*')[0]) for word in topic.split(' + ')} 
				for topic in open(filename,'r').read().splitlines()]

filename = 'topics'
topics = parse_topics(filename)
all_words = list(set(list(itertools.chain.from_iterable([topic.keys() for topic in topics]))))

#Asked for 1000, gensim LDA only uncovered 10. Taking 10 as upper limit
for topic in topics:
	for citerion in : #words over topics, words within topics, topics over documents:
		for distance in : #cosine,kullbach liebler, correlation
			#compute distance for criterion for topic

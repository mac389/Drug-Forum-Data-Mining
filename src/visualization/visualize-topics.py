import itertools

import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist

from matplotlib import rcParams
from collections import namedtuple 

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
#List to fix order. Will iterate over all_words many times later.


#Construct vectors
data_for_heatmap = np.array([[topic[word] if word in topic else 0 
					  for word in all_words]
					  for topic in topics])

fig = plt.figure()
ax = fig.add_subplot(111)
#data_for_heatmap = data_for_heatmap[data_for_heatmap[:,1].argsort()[::-1]]
cax = ax.imshow(data_for_heatmap,interpolation='nearest',aspect='auto',cmap=plt.cm.bone_r,vmax=0.2)
artist.adjust_spines(ax)
ax.set_ylabel(artist.format('Topic'))
ax.set_xlabel(artist.format('Word'))
cbar = plt.colorbar(cax,ticks=[0,0.1,0.2])
cbar.set_label(artist.format('Contribution'))
plt.savefig('topics.png')
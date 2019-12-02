import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist 

from awesome_print import ap 
from collections import Counter
from matplotlib import rcParams

rcParams['text.usetex'] = True

drug_names = open('drug_names','r').read().splitlines()
interaction_matrix = np.load('small-interaction_matrix-2015-11-13.npy')

def diagonal_key(key):
	#Takes key structured as %s-%s. Returns True if %s equals %s
	one,two = key.split('-',1)
	return one == two

def split_on_nth_occurence(text,n):
	groups = text.split('_')
	return ('_'.join(groups[:(n-1)]), '_'.join(groups[(n-1):]))

#Zip together both data structures
frequencies = {}
for row in xrange(interaction_matrix.shape[0]):
	for col in xrange(interaction_matrix.shape[1]):
		key = '%s-%s'%(drug_names[row],drug_names[col])
		flipped_key = '%s-%s'%(drug_names[col],drug_names[row])
		if key not in frequencies and flipped_key not in frequencies:
			frequencies['%s-%s'%(drug_names[row],drug_names[col])] = interaction_matrix[row][col]

frequencies_of_combinations = {key:value for key,value in frequencies.iteritems() if not diagonal_key(key)}

dikal = ['5-meo-dipt']

name, frequency = zip(*sorted(frequencies_of_combinations.items())[::-1])
with open('drug-combination-frequency-from-interaction-matrix.csv','w') as fid:
	for n,f in zip(name,frequency):
		one,two = n.split('-',1)
		if len(one) == 1:
			for drug in dikal:
				if drug in n:
					one = drug
					two = n.replace(one+'-',"")
		print>>fid,'%s,%s,%d'%(one,two,int(f))

''' idx = range(len(frequency))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(idx,frequency, color='k')

artist.adjust_spines(ax)
ax.set_ylabel(artist.format('No. of mentions'))
ax.set_xticks(range(len(name)))
ax.set_xticklabels(map(artist.format,name), rotation=90)
plt.tight_layout()
plt.savefig('drug-combination-frequency-from-interaction-matrix.png')
'''

'''
#Checking that diagonal frequencies agree with earlier calculation of drug frequencies. 
#Overall drug frequencies
frequencies = {key:value for key,value in frequencies.iteritems() if diagonal_key(key)}

cutoff=20
name, frequency = zip(*sorted(frequencies.items())[::-1][:cutoff])
idx = range(len(frequency))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(idx,frequency, color='k')

artist.adjust_spines(ax)
ax.set_ylabel(artist.format('No. of mentions'))
ax.set_xticks(range(len(name)))
ax.set_xticklabels(map(artist.format,name), rotation=90)
'''
'''
a = plt.axes([.65, .6, .2, .2])
full_frequencies = frequencies.values()
a.hist(full_frequencies, color='k')
artist.adjust_spines(a)
a.set_xlabel(artist.format('No. of mentions'))
a.set_ylabel(artist.format('No. of substances'))
plt.yscale('log', nonposy='clip')
for label in a.get_xticklabels()[1::2]:
    label.set_visible(False)
'''
'''
plt.tight_layout()
plt.savefig('drug-name-frequency-from-interaction-matrix.png')
'''
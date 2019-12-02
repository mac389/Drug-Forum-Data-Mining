import couchdb, json

import numpy as np 
import matplotlib.pyplot as plt 

from nltk import word_tokenize
from pprint import pprint 
from string import punctuation
from nltk.stem.wordnet import WordNetLemmatizer

'''
lmtzr = WordNetLemmatizer()
punkt = set(punctuation)
stopwords = open('stopwords','r').read().splitlines()
filename = 'snapshot-2015-11-13'
text = [word_tokenize(experience.decode('utf-8').encode('ascii','ignore'))
			for experience in open(filename,'rb').read().splitlines()]

text = [[word.lower() for word in experience if not all([ch in punkt for ch in word])] 
			for experience in text]

text = [[lmtzr.lemmatize(word) for word in experience if word not in stopwords] for experience in text]

with open('-'.join(['tokenized','lemmatized','snapshot-2015-11-13']),'w') as fid:
	for experience in text:
		print>>fid,' '.join(experience)
'''

filename ='tokenized-lemmatized-snapshot-2015-11-13'
text = open(filename,'r').read().splitlines()

drug_names = open('drug_names','r').read().splitlines()

#interaction_matrix = np.zeros((len(drug_names),len(drug_names)))

interaction_matrix = np.zeros((50,50))

for i in xrange(50):
	for j in xrange(i+1):
		if (i*len(drug_names)+j) % 1000 == 0:
			print (i*len(drug_names)+j)/float(0.5*len(drug_names)*(len(drug_names)-1))
		interaction_matrix[i,j] = sum([drug_names[i] in experience and drug_names[j] in experience 
										for experience in text]) 

interaction_matrix = interaction_matrix + interaction_matrix.T
#np.save('small-interaction_matrix-2015-11-13.npy',interaction_matrix)
np.save('small-interaction_matrix-2015-11-13.npy',interaction_matrix)

'''
#Could make this more efficient,
interaction_matrix = np.array([[sum([drug_one in experience and drug_two in experience for experience in text]) 
						for drug_one in drug_names] 
					   for drug_two in drug_names])
'''

print 'Now plotting'
#Visualization code here
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(interaction_matrix,aspect='auto',interpolation='nearest')
plt.show()

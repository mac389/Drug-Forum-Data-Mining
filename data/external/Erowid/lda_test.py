# -*- coding: utf-8 -*-
from __future__ import print_function


import lda
import numpy as np
import textmining
swag = "../archive/2c-b/Accidental Overdose Panic.txt"
# Create some very short sample documents
with open (swag, "r") as fid:
    doc1 = fid.read().replace('\n', '')



print("\n**These are the 'documents', making up our 'corpus':")
for n, doc in enumerate([doc1]):
    
    print("document {}: {}".format(n+1, doc))

# make a titles tuple 
# -- these should be the "titles" for the "documents" above
titles = [(swag[8:-4])]

print("\n**These are the 'document titles':")
for n, title in enumerate(titles):
    print("title {}: {}".format(n+1, title))

print("\n** The textmining packages is one tool for creating the "
      "'document-term' matrix, 'vocabulary', etc."
      "\n   You can write your own, if needed.")
tdm = textmining.TermDocumentMatrix()

tdm.add_doc(doc1)
temp = list(tdm.rows(cutoff=1))
vocab = tuple(temp[0])
X = np.array(temp[1:])

print("\n** Output produced by the textmining package...")

# document-term matrix
print("* The 'document-term' matrix")
print("type(X): {}".format(type(X)))
print("shape: {}".format(X.shape))
#print("X:", X, sep="\n" )

# the vocab
print("\n* The 'vocabulary':")
print("type(vocab): {}".format(type(vocab)))
print("len(vocab): {}".format(len(vocab)))
#print("vocab:", vocab, sep="\n")

# Titles
print("\n* Again, the 'titles' for this 'corpus':")
print("type(titles): {}".format(type(titles)))
print("len(titles): {}".format(len(titles)))
print("titles:", titles, sep="\n", end="\n\n")

model = lda.LDA(n_topics=20, n_iter=500, random_state=1)
model.fit(X)









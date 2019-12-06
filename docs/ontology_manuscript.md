### Introduction 


### Methods

  We analyze the contents of Lycaeum from X to Y. Lycaeum is an online forum devoted to providing information about substances to encourage safe and informed use. Please see [candyflipping article] for a detailed description of the acquisition of text from Lycaeum. 
    
#### Creation of Ontology.

  We had created an ontology of novel psychoactive substances for two purposes, to provide a tool to acceleratee the processing of unstructured text that describes the use of novel psychoactive substance and to provide a systematic interface to the data in that manuscript and developing a system to coregister these data with those contained in databases about molecular function. These goals correspond to two different ontologies, one that describes the pattern of appearance of tokens and one that links those tokens to the physical object to which they refer. This corresponds to the _use-mention_ distinction [Arp reference]. We termed the ontologies _ops-use_ and _ops-mention_.

  We, following [Arp reference] created an ontology by first identifying all nouns from all posts using part-of-speech tagging. Author MC then manually successively extracted from this list any token that appeared to describe effects and then any token that appeared to describe a substance.  

  We excluded from the ontology strings that were uninterpretable. Seee Supplement X for the lsit of excluded strings.   


#### Creation of Markov Logic Statements.

A Markov logic statement has the general form, _p f(x,y,...)_, where _p_ is a fraction between _0_ and _1_ and _f(x,y,..)_ is a logical statement about _x,y,..._. For example the Markov logic statment _0.4 hasToxidrome(cholinergic, X)_ represents the idea that X has a cholinergic toxidrome in 40% of possible worlds. We derived the logical statements from the ontology and probabilities from the frequency with which the terms used in the ontology appeared in theh Lycaeum corpus. In the preceding example Markov logic statement, _0.4_ would represent the fraction of times cholinergic was mentioned as a toxidrome. 

   There are many Markov logic statements needed to represent the knowledge in the Lycaeum database. Here we describe the derivation of two types of statements, expressing which substances have which effects and the pattern of coingestion. The following Problog goal demonstrates the Markov logic statements associated with describing drug-effect relationship. 

     p has_effect(X,e) :-
          person(X),
          substance_ingested(X,s1).

This goal expresses the knowledge that individual _X_ has a likelihood of _p_ of manifesting effect _e_ if we know that he ingested substance _s1_. For this goal we calculate the conditional probability of manifesting effect _e_ given ingestion of substance _s1_. We only created an instantion of Figure X for substance-effect pairs whose conditional probability was statistically significantly greater than chance, after adjusting the false discovery rate using the Benjamini-Hochberg correction. We calculated the likelihood that a conditional probability associated with a substance-effect pair was significantly greater than change by 


The following Problog goal demonstrates the Markov logic statements associated with describing the pattern of coingestion.

    p also_ingested(X,s1) :-
         person(X),
         substance_ingested(X,s2)

This goal expresses the knowledge that individual _X_ has a likelihood of _p_ of ingesting  substance _s1_ if we know that he ingested substance _s2_. For this goal we calculate the conditional probability of ingesting _s1_ given ingestion of _s2_.  

### Results 

#### Ontology.  
 We identified X unique effects and Y unique substances. 

#### Markov Logic Statements.

#### Evaluation of Ontology. 

### Conclusions




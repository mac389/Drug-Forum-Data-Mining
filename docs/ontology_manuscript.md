### Introduction 


### Methods

 We analyze the contents of Lycaeum from X to Y. Lycaeum is an online forum devoted to providing information about substances to encourage safe and informed use. Please see [candyflipping article] for a detailed description of the acquisition of text from Lycaeum. 
    
#### Creation of Ontology.

 We created an ontology of novel psychoactive substances for two purposes, to provide a tool to acceleratee the processing of unstructured text that describes the use of novel psychoactive substance and to provide a systematic interface to the data in that manuscript and developing a system to coregister these data with those contained in databases about molecular function. These goals correspond to two different ontologies, one that describes the pattern of appearance of tokens and one that links those tokens to the physical object to which they refer. This corresponds to the _use-mention_ distinction [Arp reference]. We termed the ontologies _ops-use_ and _ops-mention_.

  We, following [Arp reference] created an ontology by first identifying all nouns from all posts using part-of-speech tagging. Author MC then manually successively extracted from this list any token that appeared to describe effects and then any token that appeared to describe a substance.  

  We excluded from the ontology strings that were uninterpretable. Seee Supplement X for the lsit of excluded strings.   


#### Creation of Markov Logic Statements.

   A Markov Logic statement has the general form, _p f(x,y,...)_, where _p_ is a fraction between _0_ and _1_ and _f(x,y,..)_ is a statement about _x,y,..._ that is decidable. The Markov Logic statment _0.4 hasToxidrome(cholinergic, X)_ represents that an individual X has a cholinergic toxidrome in 40% of possible worlds. We derived the logical statements from the ontology and probabilities from the frequency with which the terms used in the ontology appeared in theh Lycaeum corpus. In the preceding example, _0.4_ would represent the fraction of times cholinergic was mentioned as a toxidrome in the Lycaeum corpus. 

Here we describe representation substance-effect, substance-substance, and effect-effect pairs in our Lycaeum corpus. Code block X states, in Problog, the Markov logic statement describing substance-effect pairs. 

```prolog
 p substance_effect(X,s1,e).
```

This goal states that if individual $X$ ingested substance $s_1$, then $X$ has a likelihood of $p$ of experiencing effect $e$.  We calculated $p$ as the conditional probability, $p\left(e|s_1\right)$, by counting all posts that mentioned effect $e$ and substance $s_1$ and dividing that quantity by the count of all posts mentioning substance $e$. We instantiated the goal in Figure X only for substance-effect pairs whose corresponding conditional probability was statistically significantly greater than chance, after adjusting the false disccovery rate to $0.05$ using the Benjamini-Hochberg correction. We calculated the inverse goal `p effect_substance(X,e,s1)`and probability, $p\left(s_1\right|e)$ analogouosly.  


The Problog goal. in Figure X identifies substance-substance comentions. 

```prolog
p ingested(X,s2,s1).
```

This goal states that if  individual _$X$_ ingested substance $s_1$, then $X$ has a likelihood $p$ of having also ingested substance $s_2$. We calculated $p\left(s_2|s_1\right)$ by counting all posts that mentioned both substances and then dividing that quantity by the count of all posts that mentioned $s_1$. The order of arguments is important. In general, for any different occurrences $x$ or $y$,  $p\left(x|y\right) \neq p\left(y | x\right)$.  

### Results 

#### Ontology.  
 We identified X unique effects and Y unique substances. 

#### Markov Logic Statements.

#### Evaluation of Ontology. 

### Conclusions




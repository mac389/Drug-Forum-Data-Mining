### Introduction 


### Methods

 We analyze the contents of Lycaeum from X to Y. Lycaeum is an online forum devoted to providing information about substances to encourage safe and informed use. Please see [candyflipping article] for a detailed description of the acquisition of text from Lycaeum. 
    
#### Creation of Ontology.

 We created an ontology of novel psychoactive substances for two purposes, to provide a tool to acceleratee the processing of unstructured text that describes the use of novel psychoactive substance and to provide a systematic interface to the data in that manuscript and developing a system to coregister these data with those contained in databases about molecular function. These goals correspond to two different ontologies, one that describes the pattern of appearance of tokens and one that links those tokens to the physical object to which they refer. This corresponds to the _use-mention_ distinction [Arp reference]. We termed the ontologies _ops-use_ and _ops-mention_.

  We, following [Arp reference] created an ontology by first identifying all nouns from all posts using part-of-speech tagging. Author MC then manually successively extracted from this list any token that appeared to describe effects and then any token that appeared to describe a substance.  

  We excluded from the ontology strings that were uninterpretable. See Supplement X for the list of excluded strings.   


#### Creation of Markov Logic Statements.

   A Markov Logic statement has the general form, $p\; f\left(x,y,\ldots\right)$, where $p \in \left(0,1\right)$  represents the chance that the statement is true and $f\left(x,y,\ldots\right)$ is a decidable statement about entities $x,y,\ldots$. The Markov Logic statment $0.4 \; \textrm{hasToxidrome}\left(X,\textrm{cholinergic}\right)$ represents that an individual X has a cholinergic toxidrome in 40% of possible worlds. We derived the logical statements from the ontology and probabilities from the frequency with which the terms used in the ontology appeared in theh Lycaeum corpus. In the preceding example, _0.4_ would represent the fraction of times the cholinergic toxidrome was mentioned in the Lycaeum corpus. 

Code block X states, in a variant of Prolog called Problog, the three Markov lgoic statements that  represent the probabilistic relationships between all significantly co-occurring substance-effect, substance-substance, and effect-effect pairs in our Lycaeum corpus. 

```prolog
 p1 substance_effect(X,s1,e).
 p2 effect_substance(X,e,s1).
 p2 substance_substance(X,s2,s1).
 p3 effect_effect(X,s2,s1).
```

The first goal states that if individual $X$ ingested substance $s_1$, then $X$ has a likelihood $p_1$ of experiencing effect $e$.  We calculated $p_1$ as the conditional probability, $p\left(e|s_1\right)$, by counting all posts that mentioned effect $e$ and substance $s_1$ and dividing that quantity by the count of all posts mentioning substance $e$. We instantiated this goal only for substance-effect pairs whose conditional probability was statistically significantly greater than chance, after using the Benjamini-Hochberg correction to adjust the false disccovery rate to $0.05$ . We calculated the second goal, which is the inverse of the first, and probability, $p\left(s_1\right|e)$ analogouosly.  The order of arguments is important. In general, for any different occurrences $x$ or $y$,  $p\left(x|y\right) \neq p\left(y | x\right)$.   

The third goal states that if  individual _$X$_ ingested substance $s_1$, then $X$ has a likelihood $p$ of having also ingested substance $s_2$. We calculated $p\left(s_2|s_1\right)$ by counting all posts that mentioned both substances and then dividing that quantity by the count of all posts that mentioned $s_1$. The fourth goal is the third goal but stated for effects. 

### Results. 

#### Ontology.  
 We identified $33$ unique effects (Supplemental Table 1) and $637$ unique substances 
(Supplemental Table 2).  This yielded $1056=33\cdot\left(33-1\right)$ effect-effect pairs, $405,132 = 637\cdot\left(637-1\right)$  substance-substance-pairs, and $21,021 = 637 \cdot 33$ substance-effect paris. 

#### Markov Logic Statements.

#### Evaluation of Ontology. 

### Conclusions



---

# Supplementary Material 

 

| emotion                   | property of  toxin  |      |      |      |
| ------------------------- | ------------------- | ---- | ---- | ---- |
| global  nervous system    | somatic sensation   |      |      |      |
| immunologic               | neurologic disorder |      |      |      |
| motor                     | perception          |      |      |      |
| misclassified             | endocrine           |      |      |      |
| gastrointestinal          | sense of self       |      |      |      |
| song  references          | use of substance    |      |      |      |
| cardiovascular            | sexual activity     |      |      |      |
| genitourinary             | uninterpretable     |      |      |      |
| oncologic                 | respiratory         |      |      |      |
| written  media references | activity references |      |      |      |
| chemical  process         | renal               |      |      |      |
| metabolic                 | esp                 |      |      |      |
| hematologic               | infectious          |      |      |      |
| musculoskeletal           | cognitive ability   |      |      |      |
| place  references         | behavior            |      |      |      |
|                           | integumentary       |      |      |      |
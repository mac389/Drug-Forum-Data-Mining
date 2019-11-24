### Calculation of Probabilities for Markov Logic Statements 

 The probabilities for each statement are calculated as conditional properties of experiencing effect $e_j$ after ingesting substance $s_i$, _i.e._ $p\left(s_i | e_j\right)$. The general approach is:

1. Calculate an empiric probability distribution function for each condition (substance-substance, effect-effect,substance-effect, and effect-substance)
2. Calculate the $p$-value associated with each condition probability. 
3. Merge all conditional probabilities into one file. 
4. Adjust the false discovery rate to $0.05$ with the Benjamini-Yueteli correction. 
5. Create Problog Statements for only those pairs with conditional probabilities significantly greater than $0$ after setting the FDR to $5\%$. 

#### Step 1: Calculate an empiric probability distribution for each function. 


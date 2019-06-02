### Suggesting Mechanisms of Interaction. 

Having identified two substances of interest from online discussions, the goal is to now assess whether the combined ingestion of these two substances has any plausible biological effect. The underlying hypothesis is that a person ingests a combination of substances to potentiate intended effects, mitigate unintended effects, or create novel effects. 

Overall approach
1. Identify mentions of substances from social media. 
1. Extract substance-substance pairs that are significantly co-mentioned
1. For each substance in each pair, identify the signal transduction pathways in which it is reported to participate and the substance's reported role 
1. Determine whether the combination of pathways implied by the substance-substance correlation is plausible

We assume that we have associated a ChEBI code with each substance. (Description of ChEBI, link, here.)

Let us take amphetamine and alcohol (ethanol) in this example
```
import libchebipy as chebi

substances = {'ethanol':{'CHEBI ID':16236}, 'amphetamine':{'CHEBI ID':2679}}
for substance in substances:
  substances[substance]['CHEBI record'] = chebi.ChebiEntity('CHEBI:%d'%(substances[substance]['CHEBI ID']))

for substance in substances 
  print substances[substance]['CHEBI records'].get_outgoings()

```

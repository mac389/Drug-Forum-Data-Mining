import os

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

from collections import Counter 

df = pd.read_csv(os.path.join('..','..','data','processed','drug-drug-frequency.csv'),index_col=0)

print {key:value for key,value in dict(Counter(df.index)).items() if value > 1}

'''
g = sns.clustermap(df,annot=False, cmap = "bone_r")
g.savefig(os.path.join('..','..','reports','figures','drug-drug-frequency.png'),dpi=400)
'''

'''

{'dialkyltryptamine': 2, 'ephedrine': 5, 'epinephrine': 3, 'cannabinoid': 5, 'anxiolytic': 2, 'myristicin': 2, 'oxycodone': 7, 'thebaine': 3, 'phytosteroid': 2, 'beta-blocker': 2, 'MDMA': 7, 'cannabinol': 4, 'bufotenin': 4, 'entheogen': 7, 'guanfacine': 4, 'hormone': 2, 'diphenhydramine': 10, 'pseudoephedrine': 9, 'psychotogen': 2, 'bromocriptine': 2, 'antiseptic': 2, 'THC': 3, 'tegretol': 2, 'ayahuasca': 12, 'benzoylecgonine': 2, 'delusiongen': 2, 'acetylcholinesterase': 2, 'dextromethorphan': 12, 'clozapine': 2, 'benzylpiperazine': 3, 'dimenhydrinate': 3, 'nicotine': 2, 'triterpene': 2, 'kratom': 6, 'LSD': 4, 'benzodiazepine': 21, 'barbiturate': 3, 'caffeine': 3, 'cannabimimetic': 2, 'triazolobenzodiazepines': 2, 'sevoflorane': 2, 'methamphetamine': 7, 'anticholinergic': 5, 'empathogen': 2, 'illusinogen': 2, 'hepatotoxin': 3, 'sympathomimetic': 2, 'heroin': 3, 'deliriant': 5, 'venlafaxine': 3, 'z-drug': 2, 'hyoscyamine': 8, 'morphinans': 2, 'phenelzine': 2, 'valproic acid': 2, 'psychonaut': 2, 'bronchodilator': 2, 'bupropion': 3, 'piper methysticum': 3, 'phenylephrine': 2, 'cathinone': 2, 'cocaine': 2, 'risperidone': 3, 'yohimbol': 2, 'mystagogue': 2, 'mescaline': 3, 'phenethylamine': 11, 'psilocybin': 19, 'buprenorphine': 9, 'opioids': 3, 'hydroxyindole': 2, 'scopalamine': 5, 'secretagogue': 2, 'thienobenzodiazapine': 3, 'propoxyphene': 4, 'trifluoromethylbenzylpiperazine': 2, 'GABAergic': 3, 'marijuana': 8, 'hydrocodone': 6, 'hydromorphone': 6, 'entheobotanical': 2, 'mephedrone': 7, 'salvia': 8, 'other': 20, 'suboxone': 2, 'acetaminophen': 13, 'doxylamine': 3, 'tryptamine': 4, 'methylphenidate': 4, 'hallucinogen': 5, 'hydroxyzine': 2, 'chorpheniramine': 5, 'norepinephrine': 3, 'dihydrocodeine': 4, 'terpinoid': 2, 'amphetamine': 12, 'grayanotoxin': 2, 'antidepressant': 2, 'piperanzine': 2, 'coricidin': 8, 'cannabidiol': 5, 'methadone': 2, 'phenylpropanolamine': 4, 'phenylmethylpiperazine': 4, 'olanzapine': 3}
'''

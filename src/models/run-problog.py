import os 

import pandas as pd 
import matplotlib.pyplot as plt 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

#from awesome_print import ap 
from pprint import pprint

DATA_PATH = os.path.join('..','..','data')

kb = open(os.path.join(DATA_PATH,'processed','kb.txt'),'r').read()

p = PrologString(kb+ '\n'+ """\n	
:- use_module(library(lists)).

%query(substance_effect(lsd,behavior)).
query(substance_substance(lsd,_)).
""")

def get_last_two(axiom_args):
	_,one,two = axiom_args
	one = one.signature.split('/')[0]
	two = two.signature.split('/')[0]
	return [one,two]

res = get_evaluatable().create_from(p).evaluate()
print res 

import seaborn as sns

df = pd.DataFrame([get_last_two(axiom.args)+[probability] for axiom,probability in res.items()], columns = ['effect','substance','probability'])


fig = plt.figure()
ax = fig.add_subplot(111)
sns.barplot(y='entity',x='probability', data=df)
#ax.set_title('Relative Efficacy for Altering Perception')
sns.despine(offset=10)
plt.show()

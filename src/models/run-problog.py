import os 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

#from awesome_print import ap 
from pprint import pprint

DATA_PATH = os.path.join('..','..','data')

kb = open(os.path.join(DATA_PATH,'processed','symptom-symptom--kb.txt'),'r').read()

p = PrologString(kb+ '\n'+ """\n	
:- use_module(library(lists)).

person(1).
query(comanifests(1,immunologic,_)).
""")

res = get_evaluatable().create_from(p).evaluate()
pprint(res)

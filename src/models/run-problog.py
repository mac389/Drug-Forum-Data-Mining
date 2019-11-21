import os 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

#from awesome_print import ap 
from pprint import pprint

DATA_PATH = os.path.join('..','..','data')

kb = open(os.path.join(DATA_PATH,'processed','for-problog.txt'),'r').read()

p = PrologString(kb+ '\n'+ """\n	
:- use_module(library(lists)).

person(1).
query(ingested(1,cobalt,_)).
""")

res = get_evaluatable().create_from(p).evaluate()
pprint(res)

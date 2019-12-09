import numpy as np 

x = np.array([1,2,3,4,5,6],dtype=float)

x /= x.sum()

print x 
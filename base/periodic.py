from __future__ import division, print_function, unicode_literals
import numpy as np

# Generates xtilde from x in P periods;
def periodic(x, P):    
    xtilde = x
    for _ in range(P-1):
        xtilde = np.concatenate((xtilde, x))
    return xtilde


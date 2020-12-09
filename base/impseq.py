from __future__ import division, print_function, unicode_literals
import numpy as np

# Generates x(n) = delta(n-n0); n1 <= n <= n2
# x(n) = 1 if n = n0, else x(n) = 0
def impseg(n0, n1, n2):
    n = np.arange(n1, n2+1, dtype=int)
    x = np.zeros((len(n)), dtype=int)
    x[n0-n1] = 1

    return x,n

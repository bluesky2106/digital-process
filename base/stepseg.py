from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt

# Generates x(n) = u(n-n0); n1 <= n <= n2
# x(n) = 0 if n < n0
# x(n) = 1 if n >= n0
def stepseg(n0, n1, n2):
    n = np.arange(n1, n2+1)
    x1 = np.zeros((n0 - n1), dtype=int)
    x2 = np.ones(n2 - n0 + 1)
    x = np.concatenate((x1, x2))

    return x,n
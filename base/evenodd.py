from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt

def evenodd(x, n):
    m = -np.flip(n)
    m1 = min(min(m), min(n))
    m2 = max(max(m), max(n))
    m = np.arange(m1, m2+1)
    x1 = np.zeros(len(m))
    i = 0
    for j in np.arange(m1, min(n)):
        i += 1
    for j in np.arange(min(n), max(n)):
        x1[i] = x[j - min(n)]
        i += 1
    x = x1
    xe = 0.5 * (x + np.flip(x))
    xo = 0.5 * (x - np.flip(x))
    return xe, xo, m
import numpy as np

# Generates x(n) = a^n,  n1 <= n <= n2, a is real
def real_valued(a, n1, n2):
    n = np.arange(n1, n2+1, dtype=int)
    x = np.power(a, n)
    return x,n
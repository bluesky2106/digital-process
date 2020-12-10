import numpy as np 

# implements y(n) = x(n-k)
def sigshift(x, m, k):
    n = m + k
    y = x
    return y, n
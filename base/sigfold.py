import numpy as np 

# implements y(n) = x(-n)
def sigfold(x, n):
    y = np.flip(x)
    n = -1 * np.flip(n)
    return y, n
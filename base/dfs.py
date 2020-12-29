import numpy as np

# discrete time fourier transform
# x, n and w are vector
def dfs(xn, N):    
    n = np.arange(0, N)
    k = np.arange(0, N)
    WN = np.exp(-1j * 2 * np.pi / N)    
    nk = np.matmul(n.reshape(N, 1), k.reshape(1, N))
    WNnk = np.power(WN, nk)
    X = np.matmul(xn.reshape(1, len(xn)), WNnk)
    return X
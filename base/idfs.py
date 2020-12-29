import numpy as np

# discrete time fourier transform
# x, n and w are vector
def idfs(Xk, N):    
    n = np.arange(0, N)
    k = np.arange(0, N)
    WN = np.exp(-1j * 2 * np.pi / N)    
    nk = np.matmul(n.reshape(N, 1), k.reshape(1, N))
    WNnk = np.power(WN, -1*nk)
    xn = np.matmul(Xk, WNnk)/N
    xn = xn.reshape(N)
    return xn
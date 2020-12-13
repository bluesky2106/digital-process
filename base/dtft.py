import numpy as np

# discrete time fourier transform
# x, n and w are vector
def dtft(x, n, w):    
    w_mtr = w.reshape(1, len(w))
    X = np.matmul(x , np.exp(-1j * (np.transpose(n) * w_mtr)))

    # X = np.dot(x, np.exp(-1j*w*n))
    return X
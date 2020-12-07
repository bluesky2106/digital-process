import numpy as np

# Generates x(n) = e^(sigma+jomega0)n,  n1 <= n <= n2, sigma is real
def complex_valued(sigma, omega, n1, n2):
    n = np.arange(n1, n2+1, dtype=int)
    x = np.exp((sigma + 1j*omega) * n)
    return x,n
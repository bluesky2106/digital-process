import numpy as np

# Generates x(n) = A*sin(omega0*n + phi0),  n1 <= n <= n2
def sin(A, omega0, phi0, n1, n2):
    n = np.arange(n1, n2+1)
    x = A*np.sin(omega0*n+phi0)
    return x, n

# Generates x(n) = A*cos(omega0*n + phi0),  n1 <= n <= n2
def cos(A, omega0, phi0, n1, n2):
    n = np.arange(n1, n2+1)
    x = A*np.cos(omega0*n+phi0)
    return x, n
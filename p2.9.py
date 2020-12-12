import matplotlib.pyplot as plt
import numpy as np
from base.conv_m import *

n = np.arange(0,21)
x = np.power(0.9, n)

y = np.power(0.8, -1*n)

rxx, n_rxx = conv_m(x, n, x, n)
rxy, n_rxy = conv_m(x, n, y, n)

# x, n
plt.subplot(2, 2, 1)    
plt.bar(n, x, width = 0.1)
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n)')

# rxx, n_rxx
plt.subplot(2, 2, 2)    
plt.bar(n_rxx, rxx, width = 0.1)
plt.xlabel('n_rxx')
plt.ylabel('rxx')
plt.title('autocorrelation')

# y, n
plt.subplot(2, 2, 3)    
plt.bar(n, y, width = 0.1)
plt.xlabel('n')
plt.ylabel('y')
plt.title('y(n)')

# rxy, n_rxy
plt.subplot(2, 2, 4)    
plt.bar(n_rxy, rxy, width = 0.1)
plt.xlabel('n_rxy')
plt.ylabel('rxy')
plt.title('crosscorrelation')


plt.show()
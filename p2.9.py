import matplotlib.pyplot as plt
import numpy as np
from base.conv_m import *
from base.sigfold import *

nx = np.arange(0,21)
x = np.power(0.9, nx)
x_flip, nx_flip = sigfold(x, nx)

y, ny = sigfold(np.power(0.8, nx), nx)

rxx, n_rxx = conv_m(x, nx, x_flip, nx_flip)
rxy, n_rxy = conv_m(x, nx, y, ny)

# x, nx
plt.subplot(2, 2, 1)    
plt.bar(nx, x, width = 0.1)
plt.xlabel('nx')
plt.ylabel('x')
plt.title('x(nx)')

# rxx, n_rxx
plt.subplot(2, 2, 2)    
plt.bar(n_rxx, rxx, width = 0.1)
plt.xlabel('n_rxx')
plt.ylabel('rxx')
plt.title('autocorrelation')

# y, ny
plt.subplot(2, 2, 3)    
plt.bar(ny, y, width = 0.1)
plt.xlabel('ny')
plt.ylabel('y')
plt.title('y(nx)')

# rxy, n_rxy
plt.subplot(2, 2, 4)    
plt.bar(n_rxy, rxy, width = 0.1)
plt.xlabel('n_rxy')
plt.ylabel('rxy')
plt.title('crosscorrelation')


plt.show()
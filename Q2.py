import matplotlib.pyplot as plt
import numpy as np
from base.conv_m import *
from base.sigfold import *

nx = np.arange(0,10)
x = np.exp(0.2*nx)*np.cos(0.4*np.pi*nx)
x_flip, nx_flip = sigfold(x, nx)


ny = np.arange(-5,6)
y = 2*np.sin(0.3*np.pi*ny)*np.cos(0.15*np.pi*ny)

rxx, n_rxx = conv_m(x, nx, x_flip, nx_flip)
rxy, n_rxy = conv_m(x, nx, y, ny)

# x, nx
plt.subplot(2, 2, 1)    
plt.bar(nx, x, width = 0.1)
# plt.xticks(range(np.amin(nx), np.amax(nx)+1))
plt.xlim(np.amin(nx), np.amax(nx)+1)
plt.xlabel('nx')
plt.ylabel('x')
plt.title('x(nx)')

# rxx, n_rxx
plt.subplot(2, 2, 2)    
plt.bar(n_rxx, rxx, width = 0.1)
# plt.xticks(range(np.amin(n_rxx), np.amax(n_rxx)+1))
plt.xlim(np.amin(n_rxx), np.amax(n_rxx)+1)
plt.xlabel('n_rxx')
plt.ylabel('rxx')
plt.title('autocorrelation')

# y, ny
plt.subplot(2, 2, 3)    
plt.bar(ny, y, width = 0.1)
plt.xlim(np.amin(ny), np.amax(ny)+1)
plt.xlabel('ny')
plt.ylabel('y')
plt.title('y(nx)')

# rxy, n_rxy
plt.subplot(2, 2, 4)    
plt.bar(n_rxy, rxy, width = 0.1)
plt.xlim(np.amin(n_rxy), np.amax(n_rxy)+1)
plt.xlabel('n_rxy')
plt.ylabel('rxy')
plt.title('crosscorrelation')


plt.show()
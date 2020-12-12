import matplotlib.pyplot as plt
import numpy as np
from base.conv_m import *

nx = np.arange(-3, 4)
x = np.array([2, -4, 5, 3, -1, -2, 6])

nh = np.arange(-1, 4)
h = np.array([1, -1, 1, -1, 1])

y, ny = conv_m(x, nx, h, nh)

# x, nx
plt.subplot(2, 2, 1)    
plt.bar(nx, x, width = 0.1)
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n)')

# h, nh
plt.subplot(2, 2, 2)    
plt.bar(nh, h, width = 0.1)
plt.xlabel('nh')
plt.ylabel('h')
plt.title('h(nh)')

# y, ny
plt.subplot(2, 2, 3)    
plt.bar(ny, y, width = 0.1)
plt.xlabel('ny')
plt.ylabel('y')
plt.title('conv_m')


plt.show()
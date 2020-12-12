import matplotlib.pyplot as plt
import numpy as np
from base.evenodd import *

x = np.arange(0,10)
n = np.arange(0,10)
xe, xo, m = evenodd(x,n)    

# xe, m
plt.subplot(2, 2, 1)    
plt.bar(m, xe, width = 0.1)
plt.xlabel('m')
plt.ylabel('xe')
plt.title('even')

# xo, m
plt.subplot(2, 2, 2)    
plt.bar(m, xo, width = 0.1)
plt.xlabel('m')
plt.ylabel('xo')
plt.title('odd')

# x, m
plt.subplot(2, 2, 3)    
plt.bar(n, x, width = 0.1)
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n)')

plt.show()
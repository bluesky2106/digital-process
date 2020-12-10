import matplotlib.pyplot as plt
import numpy as np
from base.impseq import *
from base.conv_m import *

delta, m = impseg(0, -10, 10)
h = np.exp(0.5 * m)
x, n = conv_m(delta, m, h, m)

# delta, m
plt.subplot(2, 2, 1)    
plt.bar(m,delta, width = 0.1)
plt.xticks(range(np.amin(m), np.amax(m)))
plt.xlabel('m')
plt.ylabel('delta')
plt.title('delta')

# h, m
plt.subplot(2, 2, 2)    
plt.bar(m,h, width = 0.1)
plt.xticks(range(np.amin(m), np.amax(m)+1))
plt.xlabel('m')
plt.ylabel('h')
plt.title('h(m)')

plt.subplot(2, 2, 3)
plt.bar(n,x, width = 0.1)
plt.xticks(range(np.amin(m), np.amax(m)+1))
plt.xlim(np.amin(m), np.amax(m)+1)
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n)')

plt.show()
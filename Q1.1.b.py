import matplotlib.pyplot as plt
import numpy as np
from base.impseq import *
from base.sigshift import *
from base.sigadd import *

begin = -150
end = 150
n = np.arange(begin, end+1)
x = 4*np.multiply(np.cos(0.36*np.pi*n), np.sin(0.62*np.pi*n)) - 2*(np.cos(0.15*np.pi*n) + np.sin(0.35*np.pi*n))

plt.plot(n,x)
plt.xticks(range(begin, end, 10))
plt.xlim(begin, end + 1)
plt.xlabel('n')
plt.ylabel('x2')
plt.title('x2(n)')

plt.show()
import matplotlib.pyplot as plt
import numpy as np
from base.sinusoidal import *

begin = 0
end = 100

x1, n = sin(1, np.pi * 0.1, np.pi/3, begin, end)
x2 = np.exp(-0.05 * n)
x = np.multiply(x1, x2)

# x, n
plt.plot(n,x)
plt.xlim(begin, end)
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n)')

plt.show()
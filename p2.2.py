import matplotlib.pyplot as plt
import numpy as np
from base.sigshift import *
from base.sigadd import *

num1 = 100000
n1 = np.arange(0, num1)
x1 = 2*np.random.rand(num1)

num2 = 10000
n2 = np.arange(0, num2)
x2 = np.random.normal(loc=10, scale=10, size=num2)

x11, n11 = sigshift(x1, n1, 1)
x3, n3 = sigadd(x1, n1, x11, n11)

num4 = 10000
n4 = np.arange(0, num4)
y1 = np.random.uniform(low=-0.5, high=0.5, size=num1)
y2 = np.random.uniform(low=-0.5, high=0.5, size=num1)
y3 = np.random.uniform(low=-0.5, high=0.5, size=num1)
y4 = np.random.uniform(low=-0.5, high=0.5, size=num1)
x4 = y1 + y2 + y3 + y4

# x1, n1
plt.subplot(2,2,1)
plt.hist(x1, bins=100)
plt.title('x1 histogram')

# x2, n2
plt.subplot(2,2,2)
plt.hist(x2, bins=100)
plt.title('x2 histogram')

# x3, n3
plt.subplot(2,2,3)
plt.hist(x3, bins=100)
plt.title('x3 histogram')

# x4, n4
plt.subplot(2,2,4)
plt.hist(x4, bins=100)
plt.title('x4 histogram')

plt.show()
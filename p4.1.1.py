import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
from base.impseq import *
from base.sigadd import *

nx = np.arange(-2, 3)
x = np.array([3,2,1,-2,-3])

delta, n_delta = impseg(0, 0, 5)
delta = delta.astype('float64')
# left sided sequence
b1 = np.array([0, 2, 3])
a1 = np.array([1])
xb1 = signal.lfilter(b1, a1, delta, axis=0)
xb1 = np.flip(xb1)
n1 = -np.flip(n_delta)

# right sided sequence
b2 = np.array([1, -2, -3])
a2 = np.array([1])
xb2 = signal.lfilter(b2, a2, delta)
n2 = n_delta

xa1, na1 = sigadd(xb1, n1, xb2, n2)
print(xa1)

# x, nx
# plt.subplot(1, 2, 1)
# plt.bar(nx, x, width = 0.01)
# plt.xlabel('nx')
# plt.ylabel('x')
# plt.title('x(nx)')

# delta, n_delta
# plt.subplot(1, 2, 2)
# plt.bar(n_delta, delta, width = 0.01)
# plt.xlabel('n_delta')
# plt.ylabel('delta')
# plt.title('delta(n_delta)')

# plt.show()
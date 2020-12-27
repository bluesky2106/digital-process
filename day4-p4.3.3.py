import control
import matplotlib.pyplot as plt
# plt.style.use('classic')
import numpy as np
import scipy.signal as signal
from base.impseq import *
from base.stepseg import *

b = np.array([0, 0.866, 0.0306, -2.486, 3.2094, -1.62, 0.84])
a = np.array([1,-2.9, 4.8, -4.7, 2.8, -0.9])
R, p, c = signal.residuez(b, a)
# print(R)
print("poles:")
print(p)
# print(c)
print("roots:")
roots = np.roots(b)

# b = np.array([3])
# a = np.array([1,-1])

delta, n1 = impseg(0, 0, 10)
delta = delta.astype('float64')
xb1 = signal.lfilter(b, a , delta)

step, n2 = stepseg(0, 0, 10)
step_minus_2, _ = stepseg(2, 0, 10)
xb2 = n2 * np.sin(np.pi / 3 * n2) * step + np.power(0.9, n2) * step_minus_2

err = xb1 - xb2
print(err)

tfx = control.tf(b,a)
control.pzmap(tfx)
plt.show()
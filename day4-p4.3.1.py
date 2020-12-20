import control
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
from base.impseq import *
from base.stepseg import *

b = np.array([0,0,2,1])
a = np.array([1,-1])
# R, p, c = signal.residuez(b, a)
# print(R)
# print(p)
# print(c)

# b = np.array([3])
# a = np.array([1,-1])

delta, n1 = impseg(0, 0, 10)
delta = delta.astype('float64')
xb1 = signal.lfilter(b, a , delta)

delta_minus_2, _ = impseg(2, 0, 10)
unit_minus_3, _ = stepseg(3, 0, 10)
xb2 = 2*delta_minus_2 + 3*unit_minus_3

err = xb1 - xb2
print(err)

tfx = control.tf(b,a)
control.pzmap(tfx)
plt.show()
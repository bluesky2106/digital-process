import control
import matplotlib.pyplot as plt
# plt.style.use('classic')
import numpy as np
import scipy.signal as signal
from base.impseq import *
from base.stepseg import *

# b = np.array([0.866, -1])
# a = np.array([1, -1.732, 1])
# R, p, c = signal.residuez(b, a)
# print(R)
# print(p)
# print(c)

a1 = np.array([1, -1.081, 1])
a2 = np.array([1, -2.5, 1])
a = np.convolve(a1, a2)
# print(a)

b = np.array([0, -2.104])

R, p, c = signal.residuez(b, a)
print(R)
print(p)
print(c)
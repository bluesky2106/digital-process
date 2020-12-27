import control
import matplotlib.pyplot as plt
# plt.style.use('classic')
import numpy as np
import scipy.signal as signal
from base.impseq import *
from base.stepseg import *

R = np.array([-1, 1])
p = np.array([-2, -0.5])
c = np.array([1])

b, a = signal.invresz(R, p, c)
print(b)
print(a)

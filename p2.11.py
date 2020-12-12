import matplotlib.pyplot as plt
import numpy as np
from base.stepseg import *

n = np.arange(0, 101)
x1 = np.random.rand(101)
x2 = np.random.normal(loc=0.0, scale=10, size=101)

a1 = 2
a2 = 3

################## T1[x(n)] = x(n)u(n) ##################
u, _ = stepseg(0, 0, 100)
T1_1 = np.multiply((a1 * x1 + a2 * x2), u)
T1_2 = np.multiply(a1 * x1, u) + np.multiply(a2 * x2, u)
error = T1_1 - T1_2
print(error)
# since all elements of error array are zero, T1 is Linear
#########################################################


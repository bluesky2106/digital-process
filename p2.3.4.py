import matplotlib.pyplot as plt
import numpy as np
from base.periodic import *
from base.sigadd import *

n = np.arange(0, 25)
x1 = np.arange(1, 4)
x2 = np.arange(1, 5)
P = 6
xtilde1 = periodic(x1, 9)
ntilde1 = np.arange(0, len(xtilde1))
xtilde2 = periodic(x2, 7)
ntilde2 = np.arange(0, len(xtilde2))
xtilde, ntilde = sigadd(xtilde1, ntilde1, xtilde2, ntilde2)

plt.bar(ntilde, xtilde, width = 0.1)
# plt.xlim(begin, end)
plt.xlabel('ntilde')
plt.ylabel('xtilde')
plt.title('periodic')

plt.show()
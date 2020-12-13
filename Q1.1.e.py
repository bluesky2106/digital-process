import matplotlib.pyplot as plt
import numpy as np
from base.periodic import *
from base.sigadd import *

n1 = np.arange(-1, 3)
x1 = np.array([-4, 0, 2, 8])

n2 = np.arange(-1, 4)
x2 = np.array([-1, 1, 3, 7, 5])

n3 = np.arange(-1, 1)
x3 = np.array([7, 2])
# x3 = np.array([2, 7])

xtilde1 = periodic(x1, 10)
ntilde1 = np.arange(np.amin(n1), np.amin(n1) + len(n1)*10)

xtilde2 = periodic(x2, 8)
ntilde2 = np.arange(np.amin(n2), np.amin(n2) + len(n2)*8)

xtilde3 = periodic(x3, 20)
ntilde3 = np.arange(np.amin(n3), np.amin(n3) + len(n3)*20)

xtilde, ntilde = sigadd(xtilde1, ntilde1, xtilde2, ntilde2)
xtilde, ntilde = sigadd(xtilde, ntilde, xtilde3, ntilde3)

plt.bar(ntilde, xtilde, width = 0.1)
plt.xticks(range(np.amin(ntilde), np.amax(ntilde)+1))
plt.xlabel('ntilde')
plt.ylabel('xtilde')
plt.title('periodic')

plt.show()
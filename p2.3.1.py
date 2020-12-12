import matplotlib.pyplot as plt
import numpy as np
from base.periodic import *

n = np.arange(-2, 3)
x = np.arange(-2, 3)
P = 5
xtilde = periodic(x, 5)
ntilde = np.arange(np.amin(n), np.amin(n) + len(n)*P)

plt.bar(ntilde, xtilde, width = 0.1)
# plt.xlim(begin, end)
plt.xlabel('ntilde')
plt.ylabel('xtilde')
plt.title('periodic')

plt.show()
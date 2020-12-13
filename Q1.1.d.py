import matplotlib.pyplot as plt
import numpy as np
from base.periodic import *

n = np.arange(-2, 4)
x = np.array([-5, -3, -1, 1, 3, 5])
P = 5
xtilde = periodic(x, 5)
ntilde = np.arange(np.amin(n), np.amin(n) + len(n)*P)

plt.bar(ntilde, xtilde, width = 0.1)
plt.xticks(range(np.amin(ntilde), np.amax(ntilde)+1))
plt.xlabel('ntilde')
plt.ylabel('xtilde')
plt.title('periodic')

plt.show()
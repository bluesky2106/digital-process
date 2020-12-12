import matplotlib.pyplot as plt
import numpy as np
from base.sigadd import *
from base.sigshift import *

m_begin = -3
m_end = 3
x = np.array([2, 4, -3, 1, -5, 4, 7])
m = np.arange(m_begin, m_end+1)

x_minus_3, m_minus_3 = sigshift(x, m, 3)
x_minus_3 = np.concatenate((x[0:3], x_minus_3))
m_minus_3 = np.concatenate((m[0:3], m_minus_3))

x_plus_4, m_plus_4 = sigshift(x, m, -4)

x1, n1 = sigadd(2*x_minus_3, m_minus_3, 3*x_plus_4, m_plus_4)
x1, n1 = sigadd(x1, n1, -1*x, m)

plt.bar(n1,x1, width = 0.1)
plt.xticks(range(np.amin(n1) - 1, np.amax(n1) + 1))
plt.xlabel('n1')
plt.ylabel('x1')
plt.title('x1(n1)')

plt.show()
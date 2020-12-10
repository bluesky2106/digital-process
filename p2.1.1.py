import matplotlib.pyplot as plt
import numpy as np
from base.impseq import *
from base.sigshift import *
from base.sigadd import *

delta, m = impseg(0, -5, 15)
delta_plus_2, m_plus_2 = sigshift(delta, m, -2)
delta_minus_3, m_minus_3 = sigshift(delta, m, 3)
delta_minus_7, m_minus_7 = sigshift(delta, m, 7)

# plt.subplot(2, 4, 1)    
# plt.bar(m,delta, width = 0.1)
# plt.xticks(range(np.amin(m) - 1, np.amax(m) + 1))
# plt.xlabel('m')
# plt.ylabel('delta')
# plt.title('delta')

# plt.subplot(2, 4, 2)    
# plt.bar(m_plus_2,delta_plus_2, width = 0.1)
# plt.xticks(range(np.amin(m_plus_2) - 1, np.amax(m_plus_2) + 1))
# plt.xlabel('m_plus_2')
# plt.ylabel('delta_plus_2')
# plt.title('delta_plus_2')

# plt.subplot(2, 4, 3)    
# plt.bar(m_minus_3,delta_minus_3, width = 0.1)
# plt.xticks(range(np.amin(m_minus_3) - 1, np.amax(m_minus_3) + 1))
# plt.xlabel('m_minus_3')
# plt.ylabel('delta_minus_3')
# plt.title('delta_minus_3')

# plt.subplot(2, 4, 4)    
# plt.bar(m_minus_7,delta_minus_7, width = 0.1)
# plt.xticks(range(np.amin(m_minus_7) - 1, np.amax(m_minus_7) + 1))
# plt.xlabel('m_minus_7')
# plt.ylabel('delta_minus_7')
# plt.title('delta_minus_7')

delta = delta * 2
delta_plus_2 = delta_plus_2 * 3
delta_minus_3 = (-1) * delta_minus_3
delta_minus_7 = 5 * delta_minus_7

x, n = sigadd(delta_plus_2, m_plus_2, delta, m)
x, n = sigadd(x, n, delta_minus_3, m_minus_3)
x, n = sigadd(x, n, delta_minus_7, m_minus_7)

# plt.subplot(2, 4, 5)
plt.bar(n,x, width = 0.1)
plt.xticks(range(np.amin(m) - 1, np.amax(m) + 1))
plt.xlim(np.amin(m) - 1, np.amax(m) + 1)
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n')

plt.show()
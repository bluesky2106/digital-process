import matplotlib.pyplot as plt
import numpy as np
from base.stepseg import *
from base.sigshift import *
from base.sigadd import *
from base.sigmult import *

begin = -25
end = 20

step, m = stepseg(0, begin, end+20)
step_minus_10, m_minus_10 = sigshift(step, m, 10)
step_plus_20, m_plus_20 = sigshift(step, m, -20)

u, n = sigadd(step_plus_20, m_plus_20, -1*step_minus_10, m_minus_10)
h = np.exp(0.1 * n)
x, n = sigmult(h, n, u, n)

# u, n
plt.subplot(2, 2, 1)
plt.bar(n,u, width = 0.1)
# plt.xticks(range(begin, end))
plt.xlim(begin, end)
plt.ylim(0, 2)
plt.xlabel('n')
plt.ylabel('u')
plt.title('u(n)')

# h, n
plt.subplot(2, 2, 2)
plt.bar(n,h, width = 0.1)
plt.xlim(begin, end)
plt.ylim(0, 8)
# plt.xticks(range(begin, end))
plt.xlabel('n')
plt.ylabel('h')
plt.title('h(n)')

# x, n
plt.subplot(2, 2, 3)
plt.bar(n,x, width = 0.1)
# plt.xticks(range(begin-1, end+1))
plt.xlim(begin, end)
plt.ylim(0, 8)
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n)')

plt.show()
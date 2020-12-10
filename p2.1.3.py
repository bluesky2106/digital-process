import matplotlib.pyplot as plt
import numpy as np
from base.stepseg import *
from base.sigshift import *
from base.sigadd import *

begin = -5
end = 25

delta, m = stepseg(0, begin, end)
delta_minus_5, m_minus_5 = sigshift(delta, m, 5)
delta_minus_10, m_minus_10 = sigshift(delta, m, 10)
delta_minus_15, m_minus_15 = sigshift(delta, m, 15)

x, n = sigadd(10 * delta, m, -5 * delta_minus_5, m_minus_5)
x, n = sigadd(x, n, -10 * delta_minus_10, m_minus_10)
x, n = sigadd(x, n, 5 * delta_minus_15, m_minus_15)

plt.bar(n,x, width = 0.1)
plt.xticks(range(begin - 1, end + 1))
plt.xlim(begin - 1, end + 1)
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n)')

plt.show()
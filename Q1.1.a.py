import matplotlib.pyplot as plt
import numpy as np
from base.impseq import *
from base.sigshift import *
from base.sigadd import *

begin = -20
end = 20

delta, m = impseg(0, begin, end)
delta_plus_2, m_plus_2 = sigshift(delta, m, -2)
delta_plus_3, m_plus_3 = sigshift(delta, m, -3)

x1, nx1 = sigadd(delta_plus_2, m_plus_2, -1*delta, m)
x1 = np.exp(0.2)*x1
x1, nx1 = sigadd(2*delta_plus_3, m_plus_3, -1*x1, nx1)

plt.bar(nx1,x1, width = 0.1)
plt.xticks(range(begin, end))
plt.xlim(begin, end + 1)
plt.xlabel('nx1')
plt.ylabel('x1')
plt.title('x1(nx1)')

plt.show()
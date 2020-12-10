import matplotlib.pyplot as plt
import numpy as np
from base.sinusoidal import *
from base.sigshift import *
from base.sigadd import *
from base.sigmult import *

begin = -200
end = 200

x1, n = cos(5, np.pi * 0.49, 0, begin, end)
x2, _ = cos(5, np.pi * 0.51, 0, begin, end)
x = x1 + x2

# x, n
plt.plot(n,x)
plt.xlim(begin, end)
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n)')

plt.show()
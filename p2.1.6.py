import matplotlib.pyplot as plt
import numpy as np
from base.sinusoidal import *
from base.sigshift import *
from base.sigadd import *
from base.sigmult import *

begin = -200
end = 200

x1, n = sin(2, np.pi * 0.01, 0, begin, end)
x2, _ = cos(1, np.pi * 0.5, 0, begin, end)
x = np.multiply(x1, x2)

# x, n
plt.plot(n,x)
plt.xlim(begin, end)
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n)')

plt.show()
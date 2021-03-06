import matplotlib.pyplot as plt
import numpy as np

begin = 0
end = 150
n = np.arange(begin, end+1)
x = np.exp(0.005*n) * np.cos(0.02*np.pi*n) * np.sin(0.16*np.pi*n)

plt.plot(n,x)
plt.xticks(range(begin, end, 10))
plt.xlim(begin, end + 1)
plt.xlabel('n')
plt.ylabel('x3')
plt.title('x3(n)')

plt.show()
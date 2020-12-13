import matplotlib.pyplot as plt
import numpy as np

n = np.arange(-10, 11)
x = np.zeros(len(n))
j = 0
for i in n:
    if i % 2 == 0:
        x[j] = np.exp(-0.5 * abs(i/2))
    j += 1


plt.bar(n,x, width = 0.1)
plt.xticks(range(np.amin(n), np.amax(n)+1))
plt.xlabel('n')
plt.ylabel('x')
plt.title('x(n)')

plt.show()
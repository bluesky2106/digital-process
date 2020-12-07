from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt

def evenodd(x, n):
    m = -np.flip(n)
    m1 = min(min(m), min(n))
    m2 = max(max(m), max(n))
    m = np.array(list(range(m1, m2+1)))
    xe = 0.5 * (x + np.flip(x))
    xo = 0.5 * (x - np.flip(x))
    return xe, xo
    

# n = list(range(-5, 6))
# n = np.array(list(range(-5, 4)))
# x = np.array([1,2,3,4,5,6,7,8,9,10,11])
# evenodd(x, n)



# x = np.array(x)
# n = np.array(n)
# plt.bar(n,x, width = 0.1)
# plt.show()

# plt.plot(n, x, 'ro')
# plt.axis([n1, n2, 0, 1])
# plt.xlabel('n')
# plt.ylabel('x')
# plt.title('impseg')
# plt.show()

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a.shape)
# print(a)

x = [3, 11, 7, 0, -1, 4, 2]
h = [2, 3, 0, -5, 2, 1]
y = np.convolve(x, h)
print(y)
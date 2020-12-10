import matplotlib.pyplot as plt
import numpy as np
from sigadd import *

def test_sigadd():
    x1 = np.arange(1, 12)
    x2 = np.arange(1, 8)    
    n1 = np.arange(-5, 6)
    n2 = np.arange(-3, 4)
    minN = min(np.amin(n1), np.amin(n2))
    maxN = max(np.amax(n1), np.amax(n2))
    x, n = sigadd(x1, n1, x2, n2)
    print(x)
    print(n)

    # x1, n1
    plt.subplot(2, 2, 1)    
    plt.bar(n1,x1, width = 0.1)
    plt.xlim(minN, maxN)
    plt.xlabel('n1')
    plt.ylabel('x1')
    plt.title('x1(n1)')

    # x2, n2
    plt.subplot(2, 2, 2)    
    plt.bar(n2,x2, width = 0.1)
    plt.xlim(minN, maxN)
    plt.xlabel('n2')
    plt.ylabel('x2')
    plt.title('x2(n2)')
    
    # x, n
    plt.subplot(2, 2, 3)
    plt.bar(n,x, width = 0.1)
    plt.xlim(minN, maxN)
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('sigadd')

    plt.show()

test_sigadd()
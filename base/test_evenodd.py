import matplotlib.pyplot as plt
import numpy as np
from evenodd import *

def test_evenodd():
    x = np.arange(1, 7)
    n = np.arange(-2, 4)
    xe, xo, m = evenodd(x,n)    

    print(xe)
    print(xo)
    # xe, m
    plt.subplot(2, 2, 1)    
    plt.bar(m, xe, width = 0.1)
    plt.xlabel('m')
    plt.ylabel('xe')
    plt.title('even')

    # xo, m
    plt.subplot(2, 2, 2)    
    plt.bar(m, xo, width = 0.1)
    plt.xlabel('m')
    plt.ylabel('xo')
    plt.title('odd')

    # x, m
    plt.subplot(2, 2, 3)    
    plt.bar(n, x, width = 0.1)
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('x(n)')

    plt.show()

test_evenodd()
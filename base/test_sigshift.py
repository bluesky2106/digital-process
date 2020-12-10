import matplotlib.pyplot as plt
import numpy as np
from sigshift import *
from stepseg import *

def test_sigshift():
    x, m = stepseg(1, -5, 5)
    y, n = sigshift(x, m, 3)    

    # x, m
    plt.subplot(1, 2, 1)    
    plt.bar(m,x, width = 0.1)
    plt.xticks(range(np.amin(m) - 1, np.amax(m) + 1))
    plt.xlabel('m')
    plt.ylabel('x')
    plt.title('x(m)')
    
    # x, n
    plt.subplot(1, 2, 2)
    plt.bar(n,y, width = 0.1)
    plt.xticks(range(np.amin(n) - 1, np.amax(n) + 1))
    plt.xlabel('n')
    plt.ylabel('y')
    plt.title('sigshift')

    plt.show()

test_sigshift()
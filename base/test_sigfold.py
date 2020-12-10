import matplotlib.pyplot as plt
import numpy as np
from sigfold import *

def test_sigfold():
    n = np.arange(1, 4)
    x = np.arange(1, 4)
    y, n = sigfold(x, n)

    # x, m
    plt.bar(n,y, width = 0.1)
    plt.xticks(range(np.amin(n) - 1, np.amax(n) + 1))
    plt.xlim(np.amin(n) - 1, np.amax(n) + 1)
    plt.xlabel('n')
    plt.ylabel('y')
    plt.title('y(n)')
    plt.show()

test_sigfold()
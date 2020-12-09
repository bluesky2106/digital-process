import matplotlib.pyplot as plt
from real_valued import *

def test_real_valued():
    x, n = real_valued(0.9, 0, 10)
    plt.bar(n,x, width = 0.1)
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('real value')
    plt.show()

test_real_valued()
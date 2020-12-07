import matplotlib.pyplot as plt
from base.complex_valued import *

def test_complex_valued():
    x, n = complex_valued(2, 3, 0, 10)
    plt.bar(n,x, width = 0.1)
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('real value')
    plt.show()

test_complex_valued()
import matplotlib.pyplot as plt
from stepseg import *

def test_stepseg():
    n0 = 1
    n1 = -5
    n2 = 5
    x , n = stepseg(n0, n1, n2)
    plt.bar(n,x, width = 0.1)
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('stepseg')
    plt.show()

test_stepseg()
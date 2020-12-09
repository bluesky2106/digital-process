import matplotlib.pyplot as plt
from sinusoidal import *

def test_sinusoidal():
    x1, n = sin(2, 0.5*np.pi, 0, 0, 10)
    x2, n = cos(3, 0.1*np.pi, np.pi/3, 0, 10)
    x = x1 + x2
    # n = np.arange(0, 11)
    # x = 3*np.cos(0.1*np.pi*n + np.pi /3) + 2*np.sin(0.5*np.pi*n)
    plt.bar(n,x, width = 0.1)
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('sinusoidal')
    plt.show()

test_sinusoidal()
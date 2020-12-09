import matplotlib.pyplot as plt
from base.periodic import *

def test_periodic():
    x = np.array([1,2,3,4,5])
    P = 3
    xtilde = periodic(x, P)
    n = np.arange(0, len(x)*P)

    plt.bar(n,xtilde, width = 0.1)
    plt.xlabel('n')
    plt.ylabel('xtilde')
    plt.title('periodic')
    plt.show()

test_periodic()
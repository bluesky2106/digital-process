import matplotlib.pyplot as plt
from impseq import *

def test_impseg():
    n0 = 1
    n1 = -5
    n2 = 5
    x , n = impseg(n0, n1, n2)
    plt.bar(n,x, width = 0.1)
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('impseg')
    plt.show()

test_impseg()
import matplotlib.pyplot as plt
from conv_m import *
from stepseg import *
from sigshift import *
from sigadd import *

def test_conv_m():
    u, m = stepseg(0, -15, 40)
    u_minus_10, m_minus_10 = sigshift(u, m, 10)
    u, m = stepseg(0, m_minus_10[0], m_minus_10[len(m_minus_10)-1])
    x, n = sigadd(u, m, -1*u_minus_10, m_minus_10)
    h = np.power(0.9, n) * u
    y, ny = conv_m(x, n, h, n)
    print(len(y))
    print(len(ny))

    # x, m
    plt.subplot(2, 2, 1)    
    plt.bar(n,x, width = 0.1)
    plt.xticks(range(np.amin(n) - 1, np.amax(n) + 1))
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('x(n)')

    # h, m
    plt.subplot(2, 2, 2)    
    plt.bar(n,h, width = 0.1)
    plt.xticks(range(np.amin(n) - 1, np.amax(n) + 1))
    plt.xlabel('n')
    plt.ylabel('h')
    plt.title('h(n)')

    # y, ny
    plt.subplot(2, 2, 3)    
    plt.bar(ny,y, width = 0.1)
    plt.xticks(range(np.amin(ny) - 1, np.amax(ny) + 1))
    plt.xlabel('ny')
    plt.ylabel('y')
    plt.title('y(ny)')

    
    plt.show()

test_conv_m()
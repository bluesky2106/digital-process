import numpy as np 
import matplotlib.pyplot as plt

def sigmul(x1, n1, x2, n2):
    y = []
    n = []
    minN = min(n1[0], n2[0])
    maxN = max(n1[len(n1)-1], n2[len(n2)-1])
    for i in np.arange(minN, maxN+1):
        v = 1
        try:
            idx = n1.index(i)
            if idx >= 0:
                v *= x1[idx]
        
            idx = n2.index(i)
            if idx >= 0:
                v *= x2[idx]
        except:
            v = 0

        y.append(v)
        n.append(i)
    return y, n

x1 = [1,2,3,4,6,7,8,9,10,11]
x2 = [1,2,3,4,5,6,7]
n1 = list(range(-5, 6))
n2 = list(range(-3, 4))
y, n = sigmul(x1, n1, x2, n2)
print(y)
print(n)
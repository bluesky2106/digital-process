import numpy as np 

# implements y(n) = x1(n)+x2(n)
# y=sum sequence over n, which includes n1 and n2
# x1=first sequence over n1
# x2=second sequence over n2 (n2 can be different from n1)
def sigadd(x1, n1, x2, n2):
    minN = min(np.amin(n1), np.amin(n2))
    maxN = max(np.amax(n1), np.amax(n2))
    n = np.arange(minN, maxN+1)
    y = np.zeros((len(n)))
    j = 0
    for i in n:
        idx1 = np.where(n1==i)
        idx2 = np.where(n2==i)
        if len(idx1[0]) > 0:            
            y[j] += x1[idx1[0]]
        if len(idx2[0]) > 0:
            y[j] += x2[idx2[0]]
        j += 1
    return y, n
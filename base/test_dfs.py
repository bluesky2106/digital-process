import numpy as np
from dfs import *
from idfs import *

def test_dfs():
    xn = np.array([0, 1, 2, 3])
    N = 4
    X = dfs(xn, N)
    print(X)
    
    x = idfs(X, N)
    print(x)

test_dfs()
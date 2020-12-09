import matplotlib.pyplot as plt
import numpy as np

def test_random():
    x = np.random.rand(2, 10)
    print(x)

    x = np.random.randint(2, 10)
    print(x)

test_random()
import numpy as np


def do_something(x):
    y = x
    x = np.arange(15, dtype=np.int64).reshape(3, 5)
    return y + 1

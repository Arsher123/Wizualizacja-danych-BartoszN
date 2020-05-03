import numpy as np
def funkcja(n):
    b=np.arange(n*n).reshape((n,n))
    return b
n=funkcja(5)
print(n)
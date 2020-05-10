import numpy as np 
import math 
macierz=np.array([3,4,5,6,7,8],dtype=float).reshape(2,3)
macierz2=np.array([3,4,5,6,7,8])
print(macierz)
a=np.zeros(6)
a1=np.zeros(6).reshape(2,3)
print(a1)
for i in range(6):
    a[i]=math.sin(macierz2[i])
print(np.array([a]).reshape(2,3))
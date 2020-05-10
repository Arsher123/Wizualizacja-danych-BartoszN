import numpy as np 
import math
macierz=np.array([5,4,3,8,7,6],dtype=float).reshape(2,3)
macierz2=np.array([5,4,3,8,7,6])
print(macierz)
b=np.zeros(6)
b1=np.zeros(6).reshape(2,3)
print(b1)
for i in range(6):
    b[i]=math.cos(macierz2[i])
print(np.array([b]).reshape(2,3))

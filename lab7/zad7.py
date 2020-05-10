import numpy as np 
import math
#macierz a 
macierz=np.array([3,4,5,6,7,8],dtype=float).reshape(2,3)
macierz2=np.array([3,4,5,6,7,8])
print(macierz)
a0=np.zeros(6)
a1=np.zeros(6).reshape(2,3)
print(a1)
for i in range(6):
    a0[i]=math.sin(macierz2[i])
a=np.array([a0]).reshape(2,3)
#macierz b 
macierzb=np.array([5,4,3,8,7,6],dtype=float).reshape(2,3)
macierzb2=np.array([5,4,3,8,7,6])
print(macierzb)
b0=np.zeros(6)
b1=np.zeros(6).reshape(2,3)
print(b1)
for i in range(6):
    b0[i]=math.cos(macierzb2[i])
b=np.array([b0]).reshape(2,3)
print(a)
print(b)
print(a+b)
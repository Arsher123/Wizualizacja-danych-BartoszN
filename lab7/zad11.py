import numpy as np 
a=np.arange(12)
print(a)
e=a.ravel()
print(e)

b = a.reshape((3,4))
print(b)
f=b.ravel()
print(f)

c=a.reshape((4,3))
print(c)
g=c.ravel()
print(g)

d=a.reshape((2,6))
print(d)
h=d.ravel()
print(h)
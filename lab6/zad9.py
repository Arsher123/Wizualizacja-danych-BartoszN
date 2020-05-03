import numpy as np
m=np.arange(25)
m[0]=1
m[1]=1
for i in range(2,25):
    m[i]=m[i-1]+m[i-2]
m=m.reshape((5,5))
print(m)
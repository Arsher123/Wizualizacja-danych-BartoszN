from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
a=fig.gca(projection='3d')

t=np.linspace(0,2*np.pi,100)
z=t
x=np.sin(z)
y=2*np.cos(z)
a.plot(x,y,z,label='zadanie1')
a.legend()
plt.show()
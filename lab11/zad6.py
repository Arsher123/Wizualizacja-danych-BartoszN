import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ustawiamy seed by za każdym razem wyglądało identycznie
np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 121 , projection = '3d' )
n = 20
for c, m, zlow, zhigh in [( 'r' , 'o' , 0 , -20 )]:
    xs = randrange(n, 1 , 21 )
    ys = randrange(n, 0 , 20 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c =c, marker =m)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )

ax = fig.add_subplot( 122, projection = '3d' )
n=5
for c,m,zlow,zhigh in [('b','D',0,-30)]:
    xs=randrange(n,1,5)
    ys=randrange(n,1,5)
    zs=randrange(n,zlow,zhigh)
plt.show()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure(figsize=plt.figaspect(0.5))


# generuj dane.
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)

# rysuj powierzchnię.
#1 powierzchnia
ax=fig.add_subplot(1,1,1,projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap =cm.coolwarm,linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )
#2 powierzchnia 
ax = fig.add_subplot( 1 , 2 , 1 , projection = '3d' )
phoenix = ax.plot_surface(X, Y, Z, cmap =cm.inferno,linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(phoenix,shrink =0.5,aspect=5)
#3powierzchnia
ax = fig.add_subplot( 1 , 2 , 2 , projection = '3d' )
plasma = ax.plot_surface(X, Y, Z, cmap =cm.plasma,linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(plasma,shrink=0.5,aspect=5)
#4powierzchnia
ax = fig.add_subplot( 1 , 2 , 1.5 , projection = '3d' )
flag = ax.plot_surface(X, Y, Z, cmap =cm.flag,linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(flag,shrink=0.5,aspect=5)
#5powierzchnia
ax = fig.add_subplot( 3 , 1 , 1 , projection = '3d' )
magma = ax.plot_surface(X, Y, Z, cmap =cm.magma,linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(magma,shrink=0.5,aspect=5)


plt.show()

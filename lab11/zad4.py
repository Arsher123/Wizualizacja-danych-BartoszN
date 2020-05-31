import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
fig = plt.figure( figsize =( 8 , 3 ))
ax1 = fig.add_subplot( 121 , projection = '3d' )
ax2 = fig.add_subplot( 122 , projection = '3d' )
# fikcyjne dane
x = np.arange( 4 )
y = np.arange( 5 )
xx, yy = np.meshgrid(x, y)
x, y = xx.ravel(), yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade = True )
ax1.set_title('Wykres zacieniony')
ax2.bar3d(x, y, bottom, width, depth, top, shade = False )
ax2.set_title('Wykres nie zacieniony')
plt.show()
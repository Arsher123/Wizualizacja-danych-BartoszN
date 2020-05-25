import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
s = np.sin(x)
plt.plot(x , s+2 , label = 'sin(x)')
plt.plot(x , s/-1 , label = 'sin(x)')
plt.ylabel('jakieś liczby')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.show()
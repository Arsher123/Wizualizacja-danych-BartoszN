import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x, s, label='sin(x)')
plt.plot(x,c,label='cos(x)')

# etykiety osi
plt.xlabel('x')
plt.ylabel('sin(x)/cos(x)')

# tytuł wykresu
plt.title("Wykres sin(x) i cos(x)")

# umieszczamy legendę na wykresie
plt.legend()

plt.show()
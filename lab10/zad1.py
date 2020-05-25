import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 20, 1)
s=1/x
plt.plot(x, s, label='f(x)=1/x')


# etykiety osi
plt.xlabel('x')
plt.ylabel('f(x)')

# tytuł wykresu
plt.title("wykres funkcji f(x) dla x[1,20]")

# włączamy pokazywanie legendy
plt.legend()

plt.show()
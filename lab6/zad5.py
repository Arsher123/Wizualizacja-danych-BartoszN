import numpy as np
def wketor(d):
    mat=np.linspace(1,d,d)
    mat_diag=np.diag(mat)
    return mat_diag
d=input("podaj dlugosc wektora: ")
d=int(d)
m=wketor(d)
print(m)

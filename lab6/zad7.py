import numpy as np 
def funkcja(n):
    macierz=np.zeros((n,n))
    #tworzymy przekatne 
    for i in range(n):
        macierz=macierz+np.diag(np.linspace(2*(i+1),2*(i+1),n-i),i)
        if (i!=0):
            macierz=macierz+np.diag(np.linspace(2*(i+1),2*(i+1),n-i),-i)
    return macierz
n=input("podaj rozmiar tablicy:")
n=int(n)
print(funkcja(n))
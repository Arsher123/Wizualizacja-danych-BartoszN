import numpy as np
def Funkcja(tablica,kierunek):
    h,x=tablica.shape
    m=tablica
    if(kierunek in (4,6)):
        if(x%2!=0):
            return("ilosc kolumn nie pozwala na dzialanie")
        else:
            if(kierunek==6):
                m=tablica[:,int(x/2):]
            else:
                m=tablica[:,:int(x/2)]

    else:
        if(h%2!=0):
            return("Ilosc wierszx nie pozwala na dzialanie")
        else:
            if(kierunek==2):
                m=tablica[int(h/2):]
            else:
                m=tablica[:int(h/2)]

    return m
def kierunek():
    n=input("Wybierz jak podzielic:\n8-gora,\n2-dol,\n4-lewo,\n6-prawo\n")
    print(n)
    if(int(n) in (2,4,6,8)):
        return int(n)
    else:
        print("blad ")
        kierunek()

h=input("Podaj wysokosc: ")
h=int(h)
x=input("Podaj szerokosc: ")
x=int(x)
tab=np.arange((h*x))
tab=tab.reshape((h,x))
print(tab)
n=kierunek()
print(Funkcja(tab,n))
import math 
def suma(a1=1,r=1,ile=10):
    wynik1=2*a1
    wynik2=(ile-1)*r
    wynik3=wynik1+wynik2
    wynik4=wynik3*r
    wynik5=wynik4/2
    wynik6=wynik5*ile
    return(wynik6)
print(suma())
import math
from ciagi.arytmetyczne import*
from ciagi.geometryczne import*
print("co chcesz obliczyc?")
print("ciag arytmetyczny:1")
print("ciag geometryczny:2")
x=input()
x=int(x)
if x==1:
    print("wzor na n-ty wyraz wybierz: 1")
    print("wzor na sume n pierwszych wyrazow ciagu wybierz:2 ")
    liczba1=input()
    liczba1=int(liczba1)
    if liczba1==1:
        a=input("podaj wyraz pierwszy: ")
        a=int(a)
        n=input("podaj ile jest wyraz ktory chcesz obliczyc(n): ")
        n=int(n)
        r=input("podaj jaka jest roznica ciagu(r): ")
        r=int(r)
        arytmetyczne1(a,n,r)
        print(arytmetyczne1(a,n,r))
    if liczba1==2:
        a1=input("podaj pierwszy wyraz ciagu: ")
        a1=float(a1)
        a2=input("podaj ostatni wyraz ciagu: ")
        a2=float(a2)
        n=input("podaj ile jest wyrazow(n): ")
        n=float(n)
        arytmetyczne2(a1,a2,n)
        print(arytmetyczne2(a1,a2,n))
if x==2:
    print("wzor na n-ty wyraz wybierz:1 ")
    print("wzor na sume n wyrazow ciagu: 2")
    liczba1=input()
    liczba1=int(liczba1)
    if liczba1==1:
        a=input("podaj pierwszy wyraz ciagu : ")
        a=int(a)
        q=input("podaj iloraz ciagu: ")
        q=int(q)
        n=input("podaj n wyrazow: ")
        n=int(n)
        geometryczne1(a,q,n)
        print(geometryczne1(a,q,n))
    if liczba1==2:
        a=input("podaj pierwszy wyraz ciagu: ")
        a=float(a)
        q=input("podaj iloraz tego ciagu: ")
        q=float(q)
        n=input("podaj n wyrazow: ")
        n=float(n)
        geometryczne2(a,q,n)
        print(geometryczne2(a,q,n))
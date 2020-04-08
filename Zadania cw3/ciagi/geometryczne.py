def geometryczne1(a,q,n):
    wynik=a*q**(n-1)
    return wynik
def geometryczne2(a,q,n):
    if q != 1:
        wynik=a*1-q**n/1-q
        return wynik
    if q == 1:
        wynik=a*n
        return wynik
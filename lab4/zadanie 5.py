import math
class ciagi:
    def pobierz_elementy(self,n):
        self.lista=[]
        for i in range(0,n):
            a=input("podaj wartosc: ")
            self.lista.append(a)
    def pobierz_parametry(self,a1,r,n):
        self.a1=a1
        self.r=r
        self.n=n
    def wyswietl_dane(self):
        print(self.lista)
    def policz_sume(self):
        self.suma=((2*self.a1+(self.n-1)*self.r)/2)*self.n
        return self.suma
    #def policz_elementy nie potrafie

#przykladowy ciag: a1=2,a2=5,a3=8,a4=12,a5=15
ciag = ciagi()
n=input("podaj ilu elementowy jest ciag: ")
n=int(n)
ciag.pobierz_elementy(n)
ciag.wyswietl_dane()
a1=input("podaj a1: ")
a1=int(a1)
r=input("podaj roznice: ")
r=int(r)
ciag.pobierz_parametry(a1,r,n)
print(ciag.policz_sume())
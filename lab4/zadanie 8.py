import math
class Robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ile_krokow):
        wynik=ile_krokow * self.krok
        self.y=self.y+wynik
        return self.y
    def idz_w_dol(self,ile_krokow):
        wynik=ile_krokow * self.krok
        self.y=self.y-wynik
        return self.y
    def idz_w_lewo(self,ile_krokow):
        wynik=ile_krokow * self.krok
        self.x=self.x-wynik
        return self.x
    def idz_w_prawo(self,ile_krokow):
        wynik=ile_krokow * self.krok
        self.x=self.x + wynik
        return self.x
    def pokaz_gdzie_jestes(self):
        return print(f"twoje wspolrzedne to : ({self.x},{self.y})") 
    def __del__(self):
        print("zabity obiekt")
        
robak=Robaczek(1,1,1)
robak.idz_w_gore(4)
robak.idz_w_lewo(3)
robak.idz_w_dol(2)
robak.idz_w_prawo(5)
print(robak.pokaz_gdzie_jestes())
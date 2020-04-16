import math
class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietlanie(self):
        print(f"{self.nazwa_produktu}")
        print(f"ilosc: {self.ilosc}")
        print(f"jednostka miary: {self.jednostka_miary}")
        print(f"cena {self.cena_jed} zlote")
    def ile_produktu(self):
        self.ilosc=str(self.ilosc)
        return print(f"produktu jest: {self.ilosc} {self.jednostka_miary}")
    def ile_kosztuje(self):
        self.ilosc=int(self.ilosc)
        self.wynik=self.ilosc * self.cena_jed
        return print(f"kosztuje:{self.wynik}zlote")
#obiekty
chleb=NaZakupy("chleb",2,"sztuki",2)
pomidor=NaZakupy("pomidor",3,"kg",3)
ziemniaki=NaZakupy("ziemniaki",5,"kg",2)

pomidor.wyswietlanie() 
pomidor.ile_produktu()
pomidor.ile_kosztuje()

chleb.wyswietlanie()
chleb.ile_produktu()
chleb.ile_kosztuje()

ziemniaki.wyswietlanie()
ziemniaki.ile_produktu()
ziemniaki.ile_kosztuje()
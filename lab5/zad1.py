class Material():
    def __init__(self,nazwa,rodzaj,dlugosc,szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.nazwa = nazwa
    def wyswietl_nazwe(self):
        return print(self.nazwa)
class Ubrania(Material):
    def __init__(self,nazwa,rodzaj,dlugosc,szerokosc,kolor,dla_kogo,rozmiar):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.nazwa = nazwa
    def wyswietl_dane1(self):
        return print(self.rozmiar,self.kolor,self.dla_kogo,self.rodzaj,self.dlugosc)
class Sweter(Ubrania):
    def wyswietl_dane2(self):
        return print(self.rodzaj)
#tworzymy obiekty:
sweter_rozpinany=Sweter("sweter_rozpinany","bawelniany",30,40,"niebieski","mezczyzna","xxl")
sweter_rozpinany.wyswietl_nazwe()
sweter_rozpinany.wyswietl_dane1()
sweter_rozpinany.wyswietl_dane2()


